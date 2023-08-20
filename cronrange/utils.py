import logging
import sys
from datetime import datetime

log = logging.getLogger("cronrange.utils")

DATETIME_FORMAT = "%d.%m.%Y. %H:%M"
WEEKDAYS = {
    "SUN": 1,
    "MON": 2,
    "TUE": 3,
    "WED": 4,
    "THU": 5,
    "FRI": 6,
    "SAT": 7,
}


def convert_string_to_datetime(datetime_string):
    log.debug(f"Converting '{datetime_string}' to datetime object")
    try:
        return datetime.strptime(datetime_string, DATETIME_FORMAT)

    except ValueError as val_ex:
        log.error(f"{val_ex}, defaulting to current datetime")
        sys.exit(1)


def _convert_day_of_week_to_aws_format(day_of_week: str):
    """
    Converts AWS day_of_week format (1-7) to cron format (0-6)
    :param day_of_week:
    :return: `day_of_week` formatted in 0-6 notation
    """
    start, end = day_of_week.split("-")

    if start in WEEKDAYS:
        start = WEEKDAYS[start]

    if end in WEEKDAYS:
        end = WEEKDAYS[end]

    return f"{int(start)-1}-{int(end)-1}"


def handle_eventbridge_expression(cron_expression):
    # EventBridge cron expression composition
    # min	hour	day-of-month	month	day-of-week	year
    # 0/5	8-17	? 				*		MON-FRI 	*

    # logger.info(f"Received EventBridge style cron expression '{cron_expression}'")
    minute, hour, day_of_month, month, day_of_week, year = cron_expression.split()

    # if the day of week is presented as a range such as 1-3 or MON-FRI
    if "-" in day_of_week:
        day_of_week = _convert_day_of_week_to_aws_format(day_of_week)
    # or if it is a single number, like 1 (Monday UNIX-style, Sunday AWS-style)
    elif day_of_week.isdigit():
        day_of_week = int(day_of_week) - 1

    # remove '?' and omit the year so that the `croniter` library accepts the expression
    compatible_expression = (
        f"{minute} {hour} {day_of_month} {month} {day_of_week}".replace("?", "*")
    )
    # logger.debug(f"Converted to '{compatible_expression}'")

    return compatible_expression
