import socket
from typing import Any, Callable, ParamSpec, Protocol, TypeAlias

Message: TypeAlias = str
Host: TypeAlias = str
Port: TypeAlias = int
Encoding: TypeAlias = str
P = ParamSpec("P")


# new send functions should fllow the below signature
class Func(Protocol):
    def __call__(
        self,
        message: Message,
        host: Host,
        port: Port,
        encoding: Encoding,
    ) -> None:
        ...


fnc_sign = Callable[[Message, Host, Port, Encoding], None]


def test_send(
    message: Message,
    host: Host = None,
    port: Port = None,
    encoding: Encoding = None,
):
    print(message)
    return


def tcp_send(
    message: Message,
    host: Host = "localhost",
    port: Port = 514,
    encoding: Encoding = "utf-8",
):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(message.encode(encoding))
    print(message)
    s.close()


SENDERS: dict[str, Func] = {
    "test": test_send,
    "tcp": tcp_send,
}
