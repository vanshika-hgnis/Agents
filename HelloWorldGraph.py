# Objectives 
# 1. undestand define  AgentState 
# 2. create simple node function to process and update state
# 3. Set up a basic Langraph Structure
# 4. Compile and invoke a Langraph graph
# 5. Understand how data flows


## create AgentState - shared data strucutre that keeps  track of information as our application runs


## Stategraph is a framework that designs and manages the flow of data in a graph structure.
from typing import TypedDict
from langgraph.graph import StateGraph

# state schema
class AgentState(TypedDict):
    message: str

def greeting_node(state: AgentState) -> AgentState:
    state["message"] = "Hey " + state["message"] + " How is your day going?"
    return state

graph = StateGraph(AgentState)
graph.add_node("greeter", greeting_node)
graph.set_entry_point("greeter")
graph.set_finish_point("greeter")

app = graph.compile()

# Execute the graph
final_state = app.invoke({"message": "there!"})
print(final_state)

# Save graph visualization to file
with open("graph.png", "wb") as f:
    f.write(app.get_graph().draw_mermaid_png())
print("Graph image saved as graph.png")

result = app.invoke({"message": "Hello!"})
print(result)
