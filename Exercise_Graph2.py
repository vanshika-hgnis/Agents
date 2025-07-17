# create a graph , pass in a  single list of ints along with a name and an operation is a "+", you add the elements and if its is a "*", mutliply the elements within the same node

# ip: {"name","values","operations"}
#op

from typing import List, Dict, TypedDict
from langgraph.graph import StateGraph
import math

class AgentState(TypedDict):
    name:str
    values:List[int]
    operation:str
    result:str

def process_values(state:AgentState) -> AgentState:
    if state["operation"] == "+":
        state["result"] = f"Hi {state['name']} , ans is {sum(state["values"])}"

    elif state["operation"] == "*":
        state["result"] = f"Hi {state['name']} , ans is {math.prod(state['values'])}"

    else:
        state["result"] = "Invalid"

    return state



graph = StateGraph(AgentState)

graph.add_node("processor", process_values)
graph.set_entry_point("processor") 
graph.set_finish_point("processor") 

app = graph.compile() 

with open("operation.png","wb") as f:
    f.write(app.get_graph().draw_mermaid_png())
print("Graph image saved as operation.png")


ans = app.invoke({"name":"Vanshika","values":[1,2,3,4],"operation":"*"})


print(ans)
