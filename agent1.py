from typing import TypedDict, List
from langchain_core.messages import HumanMessage
from langchain_community.chat_models import ChatOllama
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv

load_dotenv()

# Define state
class AgentState(TypedDict):
    messages: List[HumanMessage]

# Load local Ollama model (must be running)
llm = ChatOllama(model="mistral")  # You can change this to 'llama3', 'phi', etc.

# Node function
def process(state: AgentState) -> AgentState:
    res = llm.invoke(state["messages"])
    print(f"\nAI: {res.content}")
    return state

# Create graph
graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END)

# Compile
agent = graph.compile()

# REPL Loop
user_input = input("Enter: ")
while user_input != "exit":
    agent.invoke({"messages": [HumanMessage(content=user_input)]})
    user_input = input("Enter: ")
