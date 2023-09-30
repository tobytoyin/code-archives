# common Protocol for factory
import fnmatch
import importlib
from functools import cache
from importlib import resources
from typing import Dict, Generic, TypeVar

T = TypeVar("T")


# Inhere, we have a more generalised version of the Registry pattern


class Registry(Generic[T]):
    """
    Container of available build-in `T`s under `import_loc` path
    which satisfy the name of `import_name_pattern`

    Usages:

    ```python
    # subclass a registry to store registered `MyInterface` subclasses
    class MyRegistry(Registry[MyInterface]):
        _map = {}
        import_loc = "src.somepath"
        import_name_pattern = "*.py"   # for all kinds of py files


    # At component class directory, e.g., src/somepath/my_mod.py
    @MyRegistry.register(name="my_module")
    class MyModule(MyInterface):
        ...
    ```
    """

    _map: Dict[str, T] = {}
    import_loc: str  # the python directory to register for
    import_name_pattern: str  # the glob pattern of files to look for

    @classmethod
    def register(cls, name: str):
        """A register decorator to register Interface object

        Args:
            name (str): the key value for this to be used by the Factory
        """

        def _register_decorator(interface: T):
            cls._map.update({name: interface})
            return interface

        return _register_decorator

    @classmethod
    def get(cls, name: str) -> T:
        cls.register_from_adapters()

        return cls._map.get(name, None)

    @classmethod
    @cache
    def register_from_adapters(cls) -> int:
        """run import once to invoke all the registration of the class"""
        modules = resources.contents(cls.import_loc)  # get all modules under /plugins
        print(f"Found Modules at {modules}")

        for mod in fnmatch.filter(modules, cls.import_name_pattern):
            importlib.import_module(f"{cls.import_loc}.{mod[:-3]}")

        return len(modules)  # return cached when no diff
