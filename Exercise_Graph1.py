# Task: Personalised Compliment Agent using Langgraph 
# input : name : bob
# output : bob u are awesome
from typing import Dict , TypedDict
from langgraph.graph import StateGraph


# create an agent state - shared ds that keeps track of info as the app runs

class AgentState(TypedDict):
    name:str

def compliment_node(state:AgentState) -> AgentState:
    """ Simple node that compliments the user"""
    state["name"] = state["name"] +  "Amazing job of learning how to use Langgraph to make Complex agents"

    return state


graph = StateGraph(AgentState)
graph.add_node("complimenter",compliment_node)
graph.set_entry_point("complimenter")
graph.set_finish_point("complimenter")

app = graph.compile()

# Execute the graph
final_state = app.invoke({"name": "Vanshika"})
print(final_state)

# Save graph visualization to file
with open("compliment.png", "wb") as f:
    f.write(app.get_graph().draw_mermaid_png())
print("Graph image saved as graph.png")

result = app.invoke({"name": "Vanshika"})
print(result['name'])

