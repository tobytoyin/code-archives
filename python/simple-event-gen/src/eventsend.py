import socket
from typing import Callable, TypeAlias

Message: TypeAlias = str
Host: TypeAlias = str
Port: TypeAlias = int
Encoding: TypeAlias = str

# new send functions should fllow the below signature
fnc_sign = Callable[[Message, Host, Port, Encoding], None]


def test_send(
    message: Message,
    host: Host = None,
    port: Port = None,
    encoding: Encoding = None,
):
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
    s.close()


SENDERS: dict[str, fnc_sign] = {
    "test": test_send,
    "tcp": tcp_send,
}
