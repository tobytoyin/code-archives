import asyncio
import importlib
import importlib.util
import random
import time
from argparse import ArgumentParser
from functools import partial
from pathlib import Path
from typing import Callable

from . import eventsgen
from .eventsend import SENDERS


def get_module_config(
    path: Path,
    config_class: str,
) -> type[eventsgen.EventConfig]:
    # use this to get instanciate a custom EventConfig interface class
    spec = importlib.util.spec_from_file_location("config", path)
    if spec is None:
        raise AttributeError(f"{path} is not a correct python file")

    custom_config = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(custom_config)
    return getattr(custom_config, config_class)


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


def get_blocktime_range(args) -> tuple:
    blocktime_range = map(float, args.blocktime_range.split(","))
    return tuple(blocktime_range)


async def main(
    sender: Callable[[str], None],
    config_class: eventsgen.EventConfig,
    count: int,
    blocktime_range: tuple,
):
    results = eventsgen.eventsgen(config_class, count=count)
    async for value in results:
        rnd_blocktime = random.uniform(*blocktime_range)
        print("-" * 20, "\n")
        sender(value)
        print(value)
        print(f"Block for {rnd_blocktime:.4f}s")
        time.sleep(rnd_blocktime)


def eventsgen_cli():
    cli = ArgumentParser(prog="eventsgen")
    # events gen related
    cli.add_argument(
        "--path",
        type=Path,
        required=True,
        help="Python script path storing the EventConfig class interface",
    )
    cli.add_argument(
        "--class_name",
        type=str,
        required=True,
        help="Class name of the EventConfig class interface",
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
    cli.add_argument(
        "--blocktime_range",
        type=str,
        default="0.0,10.0",
        help="Random range in seconds of which the sender would block to send msg",
    )

    # parse cli args and start logics
    args = cli.parse_args()
    config = get_module_config(path=args.path, config_class=args.class_name)

    sender_callback = get_sender_callback(args)  # some kind of log sender partial(str)
    blocktime_range = get_blocktime_range(args)

    asyncio.run(
        main(
            sender=sender_callback,
            config_class=config(),
            count=args.count,
            blocktime_range=blocktime_range,
        )
    )


if __name__ == "__main__":
    cli()
