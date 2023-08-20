# cronrange-cli
Displays the next N number of executions for a given cron expression, with an optional start datetime. Now with support 
for [AWS EventBridge expressions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html)!

Based on [croniter](https://github.com/kiorky/croniter)

For a web experience visit [cronrange.info](https://cronrange.info/).

<!-- TOC -->
* [cronrange-cli](#cronrange-cli)
    * [Installation](#installation)
    * [Usage](#usage)
      * [CLI](#cli)
        * [Basic](#basic)
        * [AWS EventBridge compatible expressions](#aws-eventbridge-compatible-expressions)
        * [Different output formats](#different-output-formats)
      * [As a Python module](#as-a-python-module)
        * [Basic](#basic-1)
        * [AWS EventBridge compatible expressions](#aws-eventbridge-compatible-expressions-1)
  * [For developers](#for-developers)
    * [Running tests](#running-tests)
  * [License](#license)
<!-- TOC -->

### Installation

```bash
git clone REPO
cd REPO
pip install .
```

### Usage

```bash
cronrange -h
usage: cronrange [-h] -c CRON [-n EXECUTIONS] [-d START_DATE] [--output {column,text,json}]

options:
  -h, --help            show this help message and exit
  -c CRON, --cron CRON  A valid cron expression
  -n EXECUTIONS, --executions EXECUTIONS
                        Number of next executions to show. Defaults to 10
  -d START_DATE, --start_date START_DATE
                        Date and time in DD.MM.YYYY. HH:MM format from which to calculate cron executions. Defaults to current date and time.
  --output {column,text,json}, -o {column,text,json}
```

#### CLI

##### Basic

```bash
cronrange -c "*/5 * * * *"
cronrange -c "5 * * * *" -d "23.11.1999. 19:30"
cronrange -c "5 * * * *" -d "23.11.1999. 19:30" -n 50
```

##### AWS EventBridge compatible expressions

```bash
cronrange -c "15 12 * * ? *"
cronrange -c "0 10 1 JAN,FEB,MAR ? *" -d "28.11.2021. 20:00"
cronrange -c "0/50 8-17 ? * THU-FRI *" -d "27.11.2021. 19:30" -n 50
```

##### Different output formats

```bash
cronrange -c "*/5 * * * *" -o json
cronrange -c "5 * * * *" -d "23.11.1999. 19:30" --output text
cronrange -c "5 * * * *" -d "23.11.1999. 19:30" -n 50 -o column
```

#### As a Python module

##### Basic

```pycon
>>> from cronrange import get_cron_range
>>> get_cron_range(num_items=5, cron_expression="* * * * *")
['2022-01-28 21:46:00', '2022-01-28 21:47:00', '2022-01-28 21:48:00', '2022-01-28 21:49:00', '2022-01-28 21:50:00']
```

##### AWS EventBridge compatible expressions

```pycon
>>> from cronrange import get_cron_range
>>> get_cron_range(num_items=5, cron_expression="0/50 8-17 ? * THU-FRI *", start_datetime="11.5.2024. 11:30")
['2024-05-16 08:00:00', '2024-05-16 08:50:00', '2024-05-16 09:00:00', '2024-05-16 09:50:00', '2024-05-16 10:00:00']
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
python -m unittest discover -s cronrange
....................................................................
----------------------------------------------------------------------
Ran XY tests in 0.086s

OK
# OR
make test
```

## License

[Mozilla Public License 2.0](https://www.mozilla.org/en-US/MPL/2.0/)
or
[in short](https://www.tldrlegal.com/l/mpl-2.0)