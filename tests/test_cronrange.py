import unittest
from datetime import datetime, timezone
from typing import List, Union

from cronrange import get_cron_range
from cronrange.utils import convert_string_to_datetime, DATETIME_FORMAT

from parameterized import parameterized
from freezegun import freeze_time

from tests.event_bridge import EVENTBRIDGE_OUTPUTS, EVENTBRIDGE_DATETIME_FMT


class TestCronRange(unittest.TestCase):
    def assertAllDatesEqual(
        self, cronrange_values: List[str], eventbridge_values: List[str]
    ):
        for pair in zip(cronrange_values, eventbridge_values):

            self.assertEqual(
                datetime.fromisoformat(pair[0]),
                datetime.strptime(pair[1], EVENTBRIDGE_DATETIME_FMT),
            )

    @parameterized.expand(
        [
            ("28.10.2018. 17:20", datetime(2018, 10, 28, 17, 20, 00)),
            ("04.04.2018. 19:30", datetime(2018, 4, 4, 19, 30, 00)),
            ("31.12.1999. 23:52", datetime(1999, 12, 31, 23, 52, 00)),
        ]
    )
    def test_datetime_string_can_convert_to_datetime_object(
        self, input_string: str, expected_result: datetime
    ):
        actual_result = convert_string_to_datetime(input_string)

        self.assertEqual(actual_result, expected_result)

    @parameterized.expand(
        [("17:20 28.1.2018",), ("19:30 04.4.2018",), ("23:52 31.12.1999",)]
    )
    def test_datetime_string_can_not_convert_to_datetime_object(
        self, input_string: str
    ):
        self.assertRaises(SystemExit, convert_string_to_datetime, input_string)

    @parameterized.expand(
        [
            (20, "*/5 * * * *"),
            (6, "15 14 1 * *"),
            (100, "0 0 1,15 * *"),
            (10, "0 0 1,15 * *"),
            ("20", "59 0/12 * * ? *"),  # EventBridge-style
            (30, "0/50 8-17 ? * THU-FRI *"),  # EventBridge-style
            (50, "0/50 8-17 ? * THU-FRI *"),  # EventBridge-style
            (42, "0/50 8-17 ? * THU-FRI *"),  # EventBridge-style
            (1000, "0 8 1 * ? *"),  # EventBridge-style
        ]
    )
    def test_number_of_returned_executions_is_the_same_as_number_of_requested(
        self, num_ranges: Union[str, int], cron_expression: str
    ):
        ranges = get_cron_range(num_ranges, cron_expression)

        self.assertEqual(int(num_ranges), len(ranges))

    @parameterized.expand(
        [
            ("*/5 * * * 100",),
            ("*,5 * * *",),
            ("*/a * * * *",),
            ("*/5 * * , *",),
        ]
    )
    def test_invalid_cron_expression_raises_an_exception(self, cron_expression: str):
        self.assertRaises(Exception, get_cron_range, 1, cron_expression)

    @parameterized.expand(
        [
            ("0 10 * * ? *",),
            ("15 12 * * ? *",),
            ("0 18 ? * MON-FRI *", "2024-5-26 22:20:00"),
            ("0 8 1 * ? *",),
            ("59 0/12 * * ? *",),
            ("0/50 8-17 ? * THU-FRI *",),
            ("*/5 * L * ? *",),
            ("0 10 1 JAN,FEB,MAR ? *",),
            ("0 16 ? * 1-5 *", "2024-5-23 12:00:00"),
            ("0 5 ? * 1-5 *", "2024-5-23 18:00:00"),
            ("0 18 ? * 2 *", "2024-5-26 22:20:00"),
        ]
    )
    def test_get_cron_range_returns_the_same_datetime_as_eventbridge_ui(
        self, cron_expression: str, time_to_freeze: str = "2023-3-12 18:00:00"
    ):
        with freeze_time(time_to_freeze):
            expected_values = EVENTBRIDGE_OUTPUTS.get(cron_expression)
            actual_values = get_cron_range(
                num_items=10,
                cron_expression=cron_expression,
                start_datetime=datetime.now(timezone.utc).strftime(DATETIME_FORMAT),
            )

            self.assertAllDatesEqual(actual_values, expected_values)


if __name__ == "__main__":
    unittest.main()
