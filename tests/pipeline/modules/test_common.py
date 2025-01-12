from src.pipeline.modules.common import to_list


def test_to_list():
    assert to_list("item") == ["item"]
    assert to_list(["item"]) == ["item"]
    assert to_list(range(3)) == [0, 1, 2]
