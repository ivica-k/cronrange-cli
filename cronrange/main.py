#!/usr/bin/env python3
import logging
import argparse
from os import getenv

from datetime import datetime
from cronrange.utils import convert_string_to_datetime, handle_eventbridge_expression
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
DATETIME_FORMAT = "%d.%m.%Y. %H:%M"
OUTPUT_CHOICES = ["column", "text", "json"]


class BadCronException(Exception):
    pass


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("-e", "--expression", help="A valid cron expression", required=True)
    parser.add_argument(
        "-n",
        "--executions",
        default=10,
        help="Number of next executions to show. Defaults to 10.",
        required=False,
    )
    parser.add_argument(
        "-d",
        "--start-date",
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
    num_items: int, cron_expression: str, start_datetime: str=datetime.now().strftime(DATETIME_FORMAT)
) -> list:
    cron_executions = []
    if isinstance(start_datetime, str):
        start_datetime = convert_string_to_datetime(start_datetime)
    log.debug(
        f"Getting {num_items} iterations for expression '{cron_expression}' starting at '{start_datetime}'"
    )

    if len(cron_expression.split()) == 6 and "?" in cron_expression:
        cron_expression = handle_eventbridge_expression(cron_expression)

    try:
        croniter_object = croniter(cron_expression, start_datetime)

        for _ in range(int(num_items)):
            cron_executions.append(str(croniter_object.get_next(datetime)))

        return cron_executions

    except (CroniterBadDateError, CroniterNotAlphaError, CroniterBadCronError) as exc:
        message = f"Bad cron expression: '{cron_expression}'. {exc}"
        log.error(f"{message}. {exc}")

        raise BadCronException(message)

    except Exception as ex:
        log.exception(ex)


def cli():
    args = parse_args()

    try:
        executions = get_cron_range(args.executions, args.expression, args.start_date)

        CronrangeOutput(
            executions=executions, expression=args.expression, format=args.output.lower()
        )

    except Exception as ex:
        exit(ex)


if __name__ == "__main__":
    cli()
