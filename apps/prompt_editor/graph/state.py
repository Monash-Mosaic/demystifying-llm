from typing import TypedDict


class PromptEditorState(TypedDict, total=False):
    original_prompt: str
    improved_prompt: str

    task_family: str
    task_subtype: str

    rubric: dict
    slot_analysis: dict

    questions: list[dict]
    user_answers: dict

    original_response: str
    improved_response: str
