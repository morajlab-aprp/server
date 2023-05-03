from src import index


def test_index():
    assert index.hello() == "Hello server-packages-logic"
