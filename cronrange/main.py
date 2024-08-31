#!/usr/bin/env python3
import logging
import argparse
from os import getenv

from datetime import datetime
from typing import Union, List

from cronrange.utils import (
    convert_string_to_datetime,
    handle_eventbridge_expression,
    DATETIME_FORMAT,
)
from cronrange.output import CronrangeOutput

from croniter import (
    croniter,
    CroniterBadCronError,
    CroniterBadDateError,
    CroniterNotAlphaError,
)

LOG_LEVEL = getenv("CRONRANGE_LOG", "ERROR")
log = logging.getLogger("cronrange")
log.setLevel(LOG_LEVEL)
log_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(log_format)
log.addHandler(stream_handler)
OUTPUT_CHOICES = ["column", "text", "json"]


def parse_args() -> argparse.Namespace:
    """
    Parses CLI arguments.
    :return: Parsed arguments
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("-c", "--cron", help="A valid cron expression", required=True)
    parser.add_argument(
        "-n",
        "--executions",
        default=10,
        help="Number of next executions to show. Defaults to 10",
        required=False,
    )
    parser.add_argument(
        "-d",
        "--start_date",
        default=datetime.now().strftime(DATETIME_FORMAT),
        help="Date and time in DD.MM.YYYY. HH:MM format from which to calculate cron executions."
        " Defaults to current date and time.",
        required=False,
    )
    parser.add_argument(
        "--output",
        "-o",
        default="column",
        required=False,
        choices=OUTPUT_CHOICES,
    )

    return parser.parse_args()


def get_cron_range(
    num_items: Union[str, int],
    cron_expression: str,
    start_datetime: Union[datetime, str] = datetime.now().strftime(DATETIME_FORMAT),
) -> List[str]:
    """
    :param num_items: Number of cron executions to generate.
    :param cron_expression: Valid cron expression.
    :param start_datetime: Datetime from which to calculate the executions.
    :return: List of datetime strings starting from `start_datetime`.
    """
    cron_executions = []

    if isinstance(start_datetime, str):
        start_datetime = convert_string_to_datetime(start_datetime)

    log.debug(
        f"Getting {num_items} iterations for '{cron_expression}' starting at '{start_datetime}'"
    )

    if len(cron_expression.split()) == 6 and "?" in cron_expression:
        cron_expression = handle_eventbridge_expression(cron_expression)

    try:
        croniter_object = croniter(cron_expression, start_datetime)

        for _ in range(int(num_items)):
            cron_executions.append(str(croniter_object.get_next(datetime)))

        return cron_executions

    except (CroniterBadDateError, CroniterNotAlphaError, CroniterBadCronError):
        message = f"Bad cron expression: '{cron_expression}'. Expected 5 or 6 elements, got {len(cron_expression.split())}"

        log.warning(message)
        raise Exception(message)

    except Exception as ex:
        log.exception(ex)


def cli() -> None:
    """
    Provides a CLI interface to `get_cron_range`
    :return: None
    """
    args = parse_args()

    try:
        ranges = get_cron_range(args.executions, args.cron, args.start_date)

        if args.output.lower() == "column":
            print(CronrangeOutput(executions=ranges).to_column())

        elif args.output.lower() == "json":
            print(CronrangeOutput(executions=ranges).to_json())

        else:
            print(CronrangeOutput(executions=ranges))

    except Exception as ex:
        exit(ex)


if __name__ == "__main__":
    log.setLevel(logging.DEBUG)
    cli()
