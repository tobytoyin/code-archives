from src.factory import Registery


@Registery.register(name="plugin-2")
class Plugin2:
    def run(self):
        res = "hello world from plugin 2"
        print(res)
        return res
