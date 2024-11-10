from langgraph.prebuilt import tools_condition
from langgraph.graph import StateGraph, START, MessagesState

from my_agent.utils.nodes import assistant, tool_node


builder = StateGraph(MessagesState)

builder.add_node('assistant', assistant)
builder.add_node('tools', tool_node)

builder.add_edge(START, 'assistant')
builder.add_conditional_edges(
    'assistant',
    tools_condition
)
builder.add_edge('tools', 'assistant')
graph = builder.compile()
