from langgraph.graph import StateGraph
from typing import TypedDict, List

class AgentState(TypedDict):
    goal: str
    plan: List[str]
    results: List[str]

def planner(state: AgentState):
    # Call LLM
    return {"plan": ["search docs", "summarize results"]}

def executor(state: AgentState):
    step = state["plan"].pop(0)
    return {"results": state["results"] + [f"Executed {step}"]}

def validator(state: AgentState):
    if not state["plan"]:
        return "end"
    return "executor"

graph = StateGraph(AgentState)
graph.add_node("planner", planner)
graph.add_node("executor", executor)
graph.add_node("validator", validator)

graph.set_entry_point("planner")
graph.add_edge("planner", "executor")
graph.add_conditional_edges("executor", validator)