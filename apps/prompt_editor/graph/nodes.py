from .state import PromptEditorState


def initialise_prompt(state: PromptEditorState) -> dict:

    return {"improved_prompt": state["original_prompt"]}
