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


def parse_args():
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
    num_items, cron_expression, start_datetime=datetime.now().strftime(DATETIME_FORMAT)
):
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


def cli():
    args = parse_args()

    try:
        ranges = get_cron_range(args.executions, args.cron, args.start_date)

        if args.output.lower() == "column":
            print(
                CronrangeOutput(
                    executions=ranges, expression=args.cron, count=len(ranges)
                ).to_column()
            )

        elif args.output.lower() == "json":
            print(
                CronrangeOutput(
                    executions=ranges, expression=args.cron, count=len(ranges)
                ).to_json()
            )

        else:
            print(
                CronrangeOutput(
                    executions=ranges, expression=args.cron, count=len(ranges)
                )
            )

    except Exception as ex:
        exit(ex)


if __name__ == "__main__":
    log.setLevel(logging.DEBUG)
    cli()
