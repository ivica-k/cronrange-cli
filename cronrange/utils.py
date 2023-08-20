import logging
import sys
from datetime import datetime

log = logging.getLogger("cronrange.utils")

DATETIME_FORMAT = "%d.%m.%Y. %H:%M"


def convert_string_to_datetime(datetime_string: str) -> datetime:
    log.debug(f"Converting '{datetime_string}' to datetime object")

    try:
        return datetime.strptime(datetime_string, DATETIME_FORMAT)

    except ValueError as val_ex:
        # message = f"{val_ex}, defaulting to current datetime"
        message = f"Datetime '{datetime_string}' does not match the format 'DD.MM.YYYY. HH:MM'."
        # log.error(message)
        sys.exit(message)


def handle_eventbridge_expression(cron_expression: str) -> str:
    # EventBridge cron expression composition
    # min	hour	day-of-month	month	day-of-week	year
    # 0/5	8-17	? 				*		MON-FRI 	*

    log.debug(f"Received EventBridge-style cron expression '{cron_expression}'")
    minute, hour, day_of_month, month, day_of_week, year = cron_expression.split()

    # remove '?' and omit the year so that the `croniter` library accepts the expression
    compatible_expression = (
        f"{minute} {hour} {day_of_month} {month} {day_of_week}".replace("?", "*")
    )
    log.debug(f"Converted expression '{cron_expression}' to '{compatible_expression}'")

    return compatible_expression
