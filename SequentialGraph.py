# create mutliples nodes that sequentially process and update parts of the state
# connect nodes in a graph
# invoke the graph and see how the state is transformed step by step

from typing import List, Dict, TypedDict
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    name:str
    age:str
    final:str

def first_node(state:AgentState) -> AgentState:
    """ this is 1st node of our sequence"""

    state["final"] = f"Hi {state["name"]}"
    return state

def second_node(state:AgentState) -> AgentState:
    """ Second node of our sequence"""
    state["final"] += f"You are {state["age"]} years old"
    return state

