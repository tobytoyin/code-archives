import pytest

from src.factory import get_plugin


def test_get_plugin1():
    res = get_plugin("plugin-1", _id=100).run()
    assert res == "hello world from plugin 1 (100)"


def test_get_plugin2():
    res = get_plugin("plugin-2").run()
    assert res == "hello world from plugin 2"


def test_get_no_plugin():
    with pytest.raises(ValueError):
        res = get_plugin("wrong-plugin")
