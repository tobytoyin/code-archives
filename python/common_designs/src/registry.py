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
    import_pattern: str  # the glob pattern of files to look for

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
        import src

        # since this will be installed at python/libs as root directory
        # it needs to find the other modules relative to this root
        root_module = src.__path__[0]
        found_modules = glob.glob(cls.import_pattern, root_dir=root_module)
        print("Found: ", found_modules)

        for path in found_modules:
            # create the in-module package path
            module_name = f"{src.__name__}/{path}"
            module_name = module_name.replace("/", ".")
            module_name = module_name.replace(".py", "")
            print(module_name)

            importlib.import_module(module_name)

            print(f"Registered {module_name}")

        return len(found_modules)  # return cached when no diff
