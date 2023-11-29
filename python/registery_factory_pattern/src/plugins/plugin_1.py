from src.factory import Registry


@Registry.register(name="plugin-1")
class Plugin1:
    def __init__(self, _id) -> None:
        self.id = _id

    def run(self):
        res = f"hello world from plugin 1 ({self.id})"
        print(res)
        return res
