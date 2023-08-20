# cronrange-cli
Displays the next N number of executions for a given cron expression, with an optional start datetime.
Now with support for [AWS EventBridge expressions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html)!

Based on [croniter](https://github.com/kiorky/croniter)

For a web experience visit [cronrange.info](https://cronrange.info/).

### Installation

```bash
pip install cronrange
```

### Usage
```text
cronrange -h
usage: cronrange [-h] -e EXPRESSION [-n EXECUTIONS] [-d START_DATE] [--output {column,text,json}]

options:
  -h, --help            show this help message and exit
  -e EXPRESSION, --expression EXPRESSION
                        A valid cron expression
  -n EXECUTIONS, --executions EXECUTIONS
                        Number of next executions to show. Defaults to 10
  -d START_DATE, --start-date START_DATE
                        Date and time in DD.MM.YYYY. HH:MM format from which to calculate cron executions. Defaults to current date and time.
  --output {column,text,json}, -o {column,text,json}
```

##### Examples
```bash
cronrange -e "*/5 * * * *"
cronrange -e "5 * * * *" -d "23.11.1999. 19:30"
cronrange -e "5 * * * *" -d "23.11.1999. 19:30" -n 50
cronrange -e "5 * * * *" -d "23.11.1999. 19:30" -n 20 -o json

# AWS EventBridge compatible expressions
cronrange -e "15 12 * * ? *"
cronrange -e "0 10 1 JAN,FEB,MAR ? *" -d "28.11.2021. 20:00"
cronrange -e "0/50 8-17 ? * THU-FRI *" -d "27.11.2021. 19:30" -n 50
cronrange -e "0/50 8-17 ? * THU-FRI *" -d "27.11.2021. 19:30" -n 20 -o text
```

#### As a Python module
```python
from cronrange import get_cron_range

get_cron_range(num_items=5, cron_expression="* * * * *")
```

## For developers
```bash
python -m venv venv
source venv/bin/activate
pip install -e .
pip install -r dev_requirements.txt
# OR
make venv
```

### Running tests
```bash
python -m unittest discover
....................................................................
----------------------------------------------------------------------
Ran 24 tests in 0.086s

OK
# OR
make test
```

## License

[Mozilla Public License 2.0](https://www.mozilla.org/en-US/MPL/2.0/)
or
[in short](https://www.tldrlegal.com/l/mpl-2.0)