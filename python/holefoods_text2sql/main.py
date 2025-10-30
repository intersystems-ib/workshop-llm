from fastapi import FastAPI, Query
from typing import Dict

app = FastAPI(
    title="Sample Holefoods schema Text to SQL API",
    description="This is an example of a Text to SQL API using OpenAI LLM and IRIS Vector Database",
    version="1.0.0"
)

# load OpenAI APIKEY from env
from dotenv import load_dotenv
load_dotenv()

# database connection to extract information
from langchain_community.utilities import SQLDatabase
db = SQLDatabase.from_uri("iris://superuser:SYS@localhost:51774/LLMRAG", sample_rows_in_table_info=3, schema='Holefoods')
    
# openai model
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4o-mini")

from langchain_core.prompts import PromptTemplate

# define the custom prompt template
template = '''
You are an InterSystems IRIS SQL expert. 
Given an input question, first create a syntactically correct InterSystems IRIS SQL query to run and return the answer to the input question.
Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the TOP as defined in InterSystems IRIS syntax: ```SELECT [DISTINCT] TOP int select-item, select-item,...```
Always specify table names using schema as prefix.
Always add alias for tables.
Always refer to column using the table alias and the column name to avoid ambiguity.
Do not use LIMIT clause as it is not correct in IRIS dialect.
If using TOP, use it always right after SELECT. Never at the end of the query.
Do not end SQL sentences with an ;
Do not enclose fields in quotes or double quotes.
Do not enclose table names in quotes or double quotes.
You can order the results to return the most informative data in the database.
Never query for all columns from a table. You must query only the columns that are needed to answer the question.
Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
Pay attention to use CAST(CURRENT_DATE as date) function to get the current date, if the question involves "today".

Return only plain SQL without any formatting.

Only use the following tables:

{table_info}.
Question: {input}'''

# provide some examples to improve the results
examples = [
    { 
        "input": "List all regions.", 
        "query": "SELECT ID, Name FROM HoleFoods.Region;"
    },
    {
        "input": "List all countries.",
        "query": "SELECT c.ID, c.Name, r.Name Region FROM HoleFoods.Country c JOIN HoleFoods.Region r on c.Region=r.ID"
    },
    {
        "input": "What are the different product categories ?",
        "query": "SELECT DISTINCT(Category) Categories FROM HoleFoods.Product"
    },
    {
        "input": "How many pasta products where sold online in 2023 ?",
        "query": "SELECT SUM(UnitsSold) FROM HoleFoods.SalesTransaction st JOIN HoleFoods.Product p ON st.Product=p.ID WHERE st.Channel='Online' AND YEAR(st.DateOfSale) = 2023 AND p.Category = 'Pasta'"
    },
    {
        "input": "Find all snack products",
        "query": "SELECT SKU, Name, Price FROM HoleFoods.Product p WHERE p.Category='Snack'"
    },
    {
        "input": "Find all candy products",
        "query": "SELECT SKU, Name, Price FROM HoleFoods.Product p WHERE p.Category='Candy'"
    },
    {
        "input": "How many products were sold in Europe in 2022 ?",
        "query": "SELECT SUM(UnitsSold) FROM HoleFoods.SalesTransaction st JOIN HoleFoods.Outlet o ON st.Outlet=o.ID JOIN HoleFoods.Country c ON o.Country=c.ID JOIN HoleFoods.Region r ON c.Region=r.ID WHERE r.Name='Europe' AND YEAR(st.DateOfSale) = 2022"
    }
]

from langchain_iris import IRISVector
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_openai import OpenAIEmbeddings

example_selector = SemanticSimilarityExampleSelector.from_examples(
    examples,
    OpenAIEmbeddings(),
    IRISVector,
    k=3,
    input_keys=["input"],
    connection_string='iris://superuser:SYS@localhost:51774/LLMRAG',
    collection_name="sql_samples",
    pre_delete_collection=True
)

from langchain_core.prompts import FewShotPromptTemplate

example_prompt = PromptTemplate.from_template("User input: {input}\nSQL query: {query}")

prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix=template,
    suffix="User input: {input}\nSQL query: ",
    input_variables=["input", "top_k", "table_info"],
)

from langchain.chains import create_sql_query_chain
chain = create_sql_query_chain(llm, db, prompt)

from pydantic import BaseModel, Field
class Text2SQLResponse(BaseModel):
    sql: str  # the generated SQL query

@app.get("/text2sql")
async def text2sql(text: str = Query(..., description="Natural language text about Holefoods schema to convert to SQL")) -> Text2SQLResponse:
    """
    Convert input text to a SQL query.

    Parameters:
    - text: The input natural language string.

    Returns:
    - JSON object containing the generated SQL query.
    """
    query = chain.invoke({"question": text})
    return {"sql": query}