from typing import Protocol


class TargetInterface(Protocol):
    """A TargetInterface needs to implement for Client to use
    - request
    """

    def request(self):
        ...


class Client:
    def make_request(self, adapter: TargetInterface):
        adapter.request()


class Adapatee:
    """Adaptee contains
    - special_request, which is incompatible for the Client
    """

    def special_request(self):
        print("request method inside Adaptee")


# create a contractual interface for class that has `special_request` method
# there might be multiple classes share the same incompatible interface
class AdapeeTypeA(Protocol):
    def special_request(self):
        ...


class Adapter(TargetInterface):
    def __init__(self, adaptee: AdapeeTypeA) -> None:
        self.adaptee = adaptee

    def request(self):
        print("request method inside Adapter")
        self.adaptee.special_request()


if __name__ == "__main__":
    client = Client()

    adaptee = Adapatee()  # incompatible cls object
    adapter = Adapter(adaptee)

    # client can now run Adaptee in a compatible way
    client.make_request(adapter)
