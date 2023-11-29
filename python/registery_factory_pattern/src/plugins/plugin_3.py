from src.factory import Registry


@Registry.register(name="plugin-3")
class Plugin3:
    def run(self):
        res = "hello world from plugin 3"
        print(res)
        return res
