<h1 align="center">🧠 LangGraph Multi-Agent Architectures with RAG Integration</h1>

<p align="center">
  <b>A production-ready implementation of modular AI agents with intelligent routing, LLM-driven logic, and RAG integration.</b><br>
  <i>Explore how real-world AI workflows are composed using LangGraph — with deterministic logic, dynamic decisioning, and contextual memory.</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/LangGraph-AI%20Workflows-blue" />
  <img src="https://img.shields.io/badge/Multi--Agent-System-brightgreen" />
  <img src="https://img.shields.io/badge/RAG-Enabled-important" />
  <img src="https://img.shields.io/badge/LLM-Integrated-lightgrey" />
  <img src="https://img.shields.io/github/languages/top/mandeep-ray/langgraph-agents?logo=python&logoColor=white&color=blue" />
</p>


---

## ✨ Overview

This repository demonstrates the **design, orchestration, and execution of multi-agent workflows** using [LangGraph](https://www.langgraph.dev/), a graph-based AI orchestration library.

We go beyond toy examples and showcase how to:
- 🔁 Compose **modular agents** with memory-aware state
- 🧠 Combine **deterministic logic and LLM-based intelligence**
- 🔎 Integrate **Retrieval-Augmented Generation (RAG)** workflows
- 🚦 Route intelligently via **conditional edge logic**

Whether you're a **GenAI enthusiast**, **LangChain user**, or preparing for **AI interviews**, this repo will help you demonstrate **real-world agent orchestration skills**.

---

## 🧠 Agent Types

| Agent Type                  | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| 🧮 Deterministic Agents     | Add, subtract, and route based on user input or static logic                |
| 🤖 AI Decision Agents       | LLM-driven nodes making context-based decisions                             |
| 🔀 Multi-step Agent Chains  | Nested routing through multiple processing layers                          |
| 📚 RAG Agents (optional)    | Combine external knowledge with LLM reasoning for factual outputs           |

All agents use a **shared, strongly-typed state** (`AgentState`) based on `Pydantic`.

---

## 🧱 Architecture & Methodology

Each agent/node in the workflow adheres to this clean, scalable pattern:

1. ✅ **Define the shared state** (e.g., `operation`, `num1`, `num2`, `final`)
2. 🔧 **Create modular functions** for each task
3. ➰ **Use conditional routing** to determine the next node
4. 🧠 **Inject LLMs** for intelligent behavior where needed
5. 📊 **Compile & visualize the flow** using `StateGraph`

---

## 🚀 Quick Highlights

- ✅ Reusable nodes: Write once, route many times
- 🔁 Multi-stage flows: Chains of conditional agents
- 🧠 Prompt-based LLM control for agents
- 🧠 Memory-safe shared state mutation
- 🛠️ Ideal for interview demos, project portfolios, and hackathons

---

## ⚙️ Tech Stack

| Tool / Library | Purpose                                |
|----------------|----------------------------------------|
| 🐍 Python 3.10+ | Primary language                       |
| 🔁 LangGraph    | Agent orchestration and routing        |
| 🔡 Pydantic     | Type-safe state definition             |
| 🧠 Ollama Mistral   |  for intelligent agent nodes |
| 🧠 Vector Search| (optional) for RAG agents              |

---

## 💻 Recommended VSCode Setup

To get the best DX (developer experience), use the following VSCode extensions:

| Extension       | Purpose                                       |
|-----------------|-----------------------------------------------|
| ✅ Python        | Core Python support                          |
| 🔎 Pylance       | IntelliSense + type checking                 |
| 🔧 Black         | Auto-formatting for clean code               |
| 🌱 dotenv        | Environment variable management              |
| 🧪 Jupyter       | Interactive testing for node logic           |
| ⚡ Error Lens    | Inline error visualization                   |

### Bonus: VSCode `settings.json` snippet

json
{
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "python.analysis.typeCheckingMode": "basic"
}


---

<details open>
<summary><strong>🚧 Constraints Handled & Architectural Highlights</strong></summary>

<div align="left">

> This project proactively addresses several real-world system design constraints through a composable, scalable agent-based architecture.

- 🔄 <b>Robust state propagation</b> across nested and recursive agents  
- 🧠 <b>Token-safe LLM usage</b> via minimal, prompt-driven control nodes  
- 🔀 <b>Routing logic abstracted</b> from agent identity for flexible paths  
- 🧩 <b>Modular, testable function nodes</b> with strong separation of concerns  
- 🛡️ <b>Graceful fallbacks</b> for invalid conditions or operations  
- 🧬 <b>Plug-and-play extensibility</b> for adding new agents or branches  

</div>
</details>

---

<details open>
<summary><strong>🎯 Ideal Use Cases</strong></summary>

<div align="left">

This repository is an excellent fit for the following:

- 🧑‍💻 Practicing <b>LangGraph / LangChain orchestration patterns</b>  
- 🧠 Learning how <b>LLMs + functions co-exist</b> in intelligent workflows  
- 📋 Building a <b>GenAI project for your portfolio or GitHub showcase</b>  
- 💼 Preparing for <b>AI-centric software engineering or DevRel interviews</b>  
- 🧪 Creating <b>interactive AI learning tools or agent demos</b>  

</div>
</details>

---

<details open>
<summary><strong>🙌 Acknowledgments</strong></summary>

<div align="left">

- 💡 Special thanks to <strong>freeCodeCamp.org</strong> for curating the foundational course and knowledge flow.
- 🧭 Architectural alignment with real-world <strong>GenAI system design</strong> best practices — from structured routing to memory-driven state propagation.

</div>
</details>

