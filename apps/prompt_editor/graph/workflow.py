from langgraph.graph import StateGraph, START, END

from .state import PromptEditorState
from .nodes import initialise_prompt


def build_workflow():

    graph = StateGraph(PromptEditorState)

    graph.add_node(
        "initialise_prompt",
        initialise_prompt
    )

    graph.add_edge(
        START,
        "initialise_prompt"
    )

    graph.add_edge(
        "initialise_prompt",
        END
    )

    return graph.compile()


workflow = build_workflow()
