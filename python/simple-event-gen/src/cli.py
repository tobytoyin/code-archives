import asyncio
import importlib
import importlib.util
from argparse import ArgumentParser
from functools import partial
from typing import Callable

from . import eventsgen
from .eventsend import SENDERS


def get_module_config(module_path: str) -> eventsgen.EventConfig:
    path, classname = module_path.split(":")

    # use this to get instanciate a custom EventConfig interface class
    spec = importlib.util.spec_from_file_location("config", path)
    if spec is None:
        raise AttributeError(f"{path} is not a correct python file")

    custom_config = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(custom_config)
    return getattr(custom_config, classname)()


def get_sender_callback(args):
    # use ArgParser args to create a sender callback
    sender_fnc = SENDERS.get(args.sender)
    if sender_fnc is None:
        raise KeyError(f"{args.sender} is not a valid sender key")

    return partial(
        sender_fnc,
        host=args.host,
        port=args.port,
        encoding="utf-8",
    )


async def main(
    sender: Callable[[str], None],
    config_class: eventsgen.EventConfig,
    count: int,
):
    results = eventsgen.eventsgen(config_class, count=count)
    async for value in results:
        print("-" * 20, "\n")
        sender(value)


def eventsgen_cli():
    cli = ArgumentParser(prog="eventsgen")
    # events gen related
    cli.add_argument(
        "--location",
        type=str,
        required=True,
        help="PythonScriptPath:ClassName to indicate where the config class is stored",
    )
    cli.add_argument(
        "--count",
        type=int,
        default=100,
        help="Number of events to generate",
    )
    # log target related
    cli.add_argument(
        "--sender",
        type=str,
        default="tcp",
        help="sender protocol listed in `eventsend.SENDERS`",
    )
    cli.add_argument(
        "--host",
        type=str,
        default="localhost",
    )
    cli.add_argument(
        "--port",
        type=int,
        default=514,
    )

    # parse cli args and start logics
    args = cli.parse_args()
    config = get_module_config(module_path=args.location)

    sender_callback = get_sender_callback(args)  # some kind of log sender partial(str)

    asyncio.run(
        main(
            sender=sender_callback,
            config_class=config,
            count=args.count,
        )
    )
