# 🧠 LLM Workshop with InterSystems IRIS

Welcome to the **Retrieval-Augmented Generation (RAG)** workshop! 🚀 This hands-on experience will teach you how to build intelligent AI applications that combine the power of Large Language Models with vector databases using InterSystems IRIS.

## 🎯 What You'll Learn

In this workshop, you'll become a **RAG wizard** by building three different types of AI applications:

1. **📄 PDF Question-Answering Systems** - Make documents talk! Transform static PDFs into interactive knowledge bases
2. **🔍 Natural Language to SQL** - Speak to databases in plain English (or Spanish!) and get intelligent responses
3. **🤖 Complete AI Agent Architecture** - Understand how to build production-ready AI agents

This workshop is developed in Python 🐍 (Jupyter Notebook) and **InterSystems IRIS** - because why settle for ordinary databases when you can have one that speaks vector? 😉

## 🛠️ Prerequisites 

Make sure you have these tools ready for battle:

* [Git](https://git-scm.com/downloads) 📦
* [Docker](https://www.docker.com/products/docker-desktop) 🐳 (Windows users: enable "Linux containers")
* [Docker Compose](https://docs.docker.com/compose/install/) 🎼
* [Visual Studio Code](https://code.visualstudio.com/download) + [InterSystems ObjectScript Extension](https://marketplace.visualstudio.com/items?itemName=daimor.vscode-objectscript) 🔧

## 🚀 Setup & Launch

Time to bring this beast to life! 💪

**1. Clone the repository:**
```bash
git clone https://github.com/intersystems-ib/workshop-llm
cd workshop-llm
```

**2. Build the image:**
```bash
docker compose build
```

**3. Launch the containers:**
```bash
docker compose up -d
```

**4. Access your AI playground:**
* 🎛️ **InterSystems IRIS Management Portal**: [http://localhost:52774/csp/sys/UtilHome.csp](http://localhost:52774/csp/sys/UtilHome.csp)
  - Login: `superuser` / `SYS`
* 📓 **Jupyter Notebook**: [http://localhost:8888](http://localhost:8888)

## 🧪 Workshop Exercises

### 💊 Medicine Leaflet Q&A (PDF RAG Systems)

Transform boring medical documents into an intelligent assistant! Using Spanish medicine leaflets in [./data](./data), you'll build systems that can answer questions like a knowledgeable pharmacist. 💊

**Choose your adventure:**

* **📄 [PDF-RAG-CloudLLM.ipynb](./jupyter/PDF-RAG-CloudLLM.ipynb)** - Cloud-powered RAG using [Mistral AI](https://mistral.ai) 
  - *Perfect for: Production systems, highest accuracy, API-based*
  
* **🏠 [PDF-RAG-LocalModels.ipynb](./jupyter/PDF-RAG-LocalModels.ipynb)** - Privacy-first with local models
  - *Perfect for: Complete privacy, offline operation, no API costs*

![Jupyter Interface](/images/jupyter.png)

### 🍩 Holefoods Text-to-SQL Adventure

Meet **Holefoods** - a quirky company that sells food with holes in it! 🍩 (Creative, right?)

Build an intelligent SQL assistant that translates natural language into database queries. Ask questions like *"How many donuts did we sell in Europe last month?"* and watch the magic happen! ✨

* **🗣️ [NaturalLanguage-to-SQL.ipynb](./jupyter/NaturalLanguage-to-SQL.ipynb)** - Your multilingual database whisperer
  - *Features: Semantic similarity, few-shot learning, IRIS SQL optimization*

## 🌟 Inspiration: Full AI Agent Demo

Want to see the full power of AI agents in action? Check out this **complete customer support agent** built with **smolagents** and **InterSystems IRIS**:

🔗 **[Customer Support AI Agent Demo](https://github.com/intersystems-ib/customer-support-agent-demo)**

📖 **[Developer Community Article](https://community.intersystems.com/post/build-customer-support-ai-agent-smolagents-intersystems-iris-sql-rag-interoperability)** - Deep dive explanation

This demo showcases:
- 🤖 **Autonomous AI agents** that can reason and take actions
- 📊 **SQL + RAG integration** for comprehensive data access
- 🔄 **InterSystems IRIS interoperability** for enterprise-grade systems
- 🎯 **Production-ready architecture** you can actually deploy

## 🛠️ Advanced: Local Development Environment

Ready to build your own AI applications? Set up a local Python environment:

**For Mac/Linux users:**
```bash
cd python
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

**For Windows users:**
```bash
cd python
python -m venv .venv
./venv/Scripts/Activate.ps1
pip3 install -r requirements.txt
```

**Create your API keys file:**
```bash
# Create .env file
echo 'OPENAI_API_KEY="your-openai-key"' > .env
echo 'MISTRAL_API_KEY="your-mistral-key"' >> .env
```

### 🌐 Text-to-SQL API Service
Want to productionize your SQL skills? Try our FastAPI service based on the notebook:

```bash
cd python/holefoods_text2sql
fastapi dev main.py
```
🌍 **Explore the API**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 💬 Streamlit Chatbot Assistant
Experience a beautiful chat interface:

```bash
cd python/assistant
streamlit run chatbot.py
```
🎨 **Chat away**: [http://localhost:8501](http://localhost:8501)

**Challenge:** Can you integrate the medicine leaflet logic into this assistant? 🤔

## 🎓 Learning Resources

Want to dive deeper into the InterSystems universe?
- 📚 **[InterSystems Learning](https://learning.intersystems.com)** - Your gateway to mastery
- 🏛️ **[InterSystems IRIS Documentation](https://docs.intersystems.com/iris/)** - The sacred texts
- 👥 **[Developer Community](https://community.intersystems.com/)** - Where the magic happens

## 🎉 Ready to Build the Future?

You're now equipped with the knowledge to build:
- 🔮 **Intelligent document systems** that understand context
- 🗣️ **Natural language database interfaces** that feel like magic
- 🤖 **Complete AI agents** that can reason and act autonomously

**Go forth and create amazing AI applications!** The only limit is your imagination! 🚀✨

---