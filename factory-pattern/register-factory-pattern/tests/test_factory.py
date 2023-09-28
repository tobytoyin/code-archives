from src.factory import get_plugin


def test_get_plugin1():
    res = get_plugin("plugin-1")().run()
    assert res == "hello world from plugin 1"


def test_get_plugin2():
    res = get_plugin("plugin-2")().run()
    assert res == "hello world from plugin 2"


def test_get_no_plugin():
    res = get_plugin("wrong-plugin")
    assert res is None
