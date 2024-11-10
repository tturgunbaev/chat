from functools import lru_cache

from langchain_openai import ChatOpenAI
from langgraph.graph import MessagesState
from langgraph.prebuilt import ToolNode

from my_agent.utils.tools import tools
from my_agent.utils.constants import sys_msg


@lru_cache(maxsize=4)
def _get_model():
    model = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")
    model = model.bind_tools(tools)
    return model


def assistant(state: MessagesState):
    model = _get_model()
    return {'messages': model.invoke([sys_msg] + state['messages'])}

tool_node = ToolNode(tools)
