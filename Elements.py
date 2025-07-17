# Nodes - functions
# Graphs - entire workflow
# Edges - connects nodes,determines executions
#       -- Conditional Edges
# Start - virtual entry point (node)
# End  - conclusion of workflow
# Tools - nodes to perform specific tasks  such as API calls.
# ToolNode -- special node whose main job is to run a  tool
# StateGraph - use to build and compile graph structure
# manages nodes,edges , state and overflow is unified
# Runnable -- executable  components that performs a speficic   tasks withing an AI workflow
# Messages 
#   - Human Message(ip from user)
#   - System Message(instr or context to the model)
#   - Function Message ( represents the res of function call)
#   - AI Message (response from the model)
# - Tool Message(similar to function message but specific to tool usage)





