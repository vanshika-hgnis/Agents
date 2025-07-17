# Multiple Inputs Graph

# Objectives:
# 1. define a more complex AgentState
# 2. Create a processing node that performs operations on list data
# 3. Set up a Langgraph with multiple inputs
# 4. Invoke the graph with a list of inputs

from typing import List , Dict,TypedDict
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    values: List[int]
    name:str
    result: int

def process_values(state: AgentState) -> AgentState:
    """ This function handles multiple diff inputs"""
    state["result"] = f"Hi there {state["name"]}! Your sum = {sum(state["values"])}"
    print(state)
    return state

graph = StateGraph(AgentState)
graph.add_node("processor",process_values)

graph.set_entry_point("processor")
graph.set_finish_point("processor")

app = graph.compile()



# Save graph visualization to file
with open("processor.png", "wb") as f:
    f.write(app.get_graph().draw_mermaid_png())
print("Graph image saved as graph.png")

answers = app.invoke({"values":[1,2,3,4],"name":"Vanshika"})
print(answers)