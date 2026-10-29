from apps.prompt_editor.graph.workflow import workflow


def test_initial_workflow():

    result = workflow.invoke({"original_prompt": "Write an email"})

    assert result["improved_prompt"] == "Write an email"
