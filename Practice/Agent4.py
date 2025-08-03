from langgraph.graph import StateGraph, START, END
from typing import TypedDict


class AgentState(TypedDict):
    number1: int
    operation: str
    number2: int
    finalNumber: int


def adder(state: AgentState) -> AgentState:
    state["finalNumber"] = state["number1"] + state["number2"]
    return state


def substractor(state: AgentState) -> AgentState:
    state["finalNumber"] = state["number1"] - state["number2"]
    return state


def decide_next_node(state: AgentState) -> AgentState:
    # router decides ops
    if state["operation"] == "+":
        return "addition_operation"

    if state["operation"] == "-":
        return "subtraction_operation"


graph = StateGraph(AgentState)
graph.add_node("add_node", adder)
graph.add_node("subtract_node", substractor)
# graph.add_node("router", decide_next_node)
graph.add_edge("router", lambda state: state)  # passthrough function

graph.add_edge(START, "router")
graph.add_conditional_edges(
    "router",
    decide_next_node,
    {"additional_operation": "add_node", "subtraction_operation": "subtract_node"},
)

graph.add_edge("add_node", END)
graph.add_edge("subtract_node", END)

app = graph.compile()

from IPython.display import display

display(app.get_graph().draw_mermaid_png())
