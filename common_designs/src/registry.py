# common Protocol for factory
import glob
import importlib
from functools import cache
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
        root_dir = "src"
        found_modules = glob.glob(cls.import_pattern, root_dir=root_dir)
        for path in found_modules:
            fullpath = f"{root_dir}/{path}"
            module_name = fullpath.replace("/", ".")
            module_name = module_name.replace(".py", "")
            importlib.import_module(module_name)

        return len(found_modules)  # return cached when no diffiff
