import importlib
from functools import cache
from importlib import resources
from typing import Any, Dict

PLUGIN_DIR = "src.plugins"


class Registry:
    registry: Dict[str, Any] = {}

    @classmethod
    def register(cls, name: str):
        """A register decorator to register Interface object

        Args:
            name (str): the key value for this to be used by the Factory
        """

        def _register_decorator(interface):
            print(f"registered: {interface} with {name}")
            cls.registry.update({name: interface})
            return interface

        return _register_decorator

    @classmethod
    def get_plugin(cls, name: str):
        plugin = cls.registry.get(name, None)
        return plugin


@cache
def register_all():
    """run import once to invoke all the registration of the class"""
    print("registering all plugin modules")
    modules = resources.contents(PLUGIN_DIR)  # get all modules under /plugins

    for mod in filter(lambda f: f.endswith(".py"), modules):
        importlib.import_module(f"{PLUGIN_DIR}.{mod[:-3]}")


def get_plugin(name: str, *args, **kwargs):
    """factory to create a class object that is registered in Registry

    Args:
        name (enum): registered key for the class
        *args, **kwargs: arguments for the class for initialisation

    Returns:
        the registered object
    """

    register_all()  # invoke all registration
    plugin = Registry.get_plugin(name)
    if not plugin:
        raise ValueError

    return plugin(*args, **kwargs)
