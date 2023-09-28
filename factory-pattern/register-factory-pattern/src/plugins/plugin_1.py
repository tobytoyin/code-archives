from src.factory import Registery


@Registery.register(name="plugin-1")
class Plugin1:
    def run(self):
        res = "hello world from plugin 1"
        print(res)
        return res
