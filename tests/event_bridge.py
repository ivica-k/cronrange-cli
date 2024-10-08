# examples taken from https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html
# actual outputs obtained from AWS EventBridge rules https://eu-central-1.console.aws.amazon.com/events/home?region=eu-central-1#/rules/create

EVENTBRIDGE_DATETIME_FMT = "%a, %d %b %Y %H:%M:%S"

EVENTBRIDGE_OUTPUTS = {
    "0 8 1 * ? *": [
        "Sat, 01 Apr 2023 08:00:00",
        "Mon, 01 May 2023 08:00:00",
        "Thu, 01 Jun 2023 08:00:00",
        "Sat, 01 Jul 2023 08:00:00",
        "Tue, 01 Aug 2023 08:00:00",
        "Fri, 01 Sep 2023 08:00:00",
        "Sun, 01 Oct 2023 08:00:00",
        "Wed, 01 Nov 2023 08:00:00",
        "Fri, 01 Dec 2023 08:00:00",
        "Mon, 01 Jan 2024 08:00:00",
    ],
    "0/50 8-17 ? * THU-FRI *": [
        "Thu, 16 Mar 2023 08:00:00",
        "Thu, 16 Mar 2023 08:50:00",
        "Thu, 16 Mar 2023 09:00:00",
        "Thu, 16 Mar 2023 09:50:00",
        "Thu, 16 Mar 2023 10:00:00",
        "Thu, 16 Mar 2023 10:50:00",
        "Thu, 16 Mar 2023 11:00:00",
        "Thu, 16 Mar 2023 11:50:00",
        "Thu, 16 Mar 2023 12:00:00",
        "Thu, 16 Mar 2023 12:50:00",
    ],
    "59 0/12 * * ? *": [
        "Mon, 13 Mar 2023 00:59:00",
        "Mon, 13 Mar 2023 12:59:00",
        "Tue, 14 Mar 2023 00:59:00",
        "Tue, 14 Mar 2023 12:59:00",
        "Wed, 15 Mar 2023 00:59:00",
        "Wed, 15 Mar 2023 12:59:00",
        "Thu, 16 Mar 2023 00:59:00",
        "Thu, 16 Mar 2023 12:59:00",
        "Fri, 17 Mar 2023 00:59:00",
        "Fri, 17 Mar 2023 12:59:00",
    ],
    "0 18 ? * MON-FRI *": [
        "Mon, 27 May 2024 18:00:00",
        "Tue, 28 May 2024 18:00:00",
        "Wed, 29 May 2024 18:00:00",
        "Thu, 30 May 2024 18:00:00",
        "Fri, 31 May 2024 18:00:00",
        "Mon, 03 Jun 2024 18:00:00",
        "Tue, 04 Jun 2024 18:00:00",
        "Wed, 05 Jun 2024 18:00:00",
        "Thu, 06 Jun 2024 18:00:00",
        "Fri, 07 Jun 2024 18:00:00",
    ],
    "0 10 * * ? *": [
        "Mon, 13 Mar 2023 10:00:00",
        "Tue, 14 Mar 2023 10:00:00",
        "Wed, 15 Mar 2023 10:00:00",
        "Thu, 16 Mar 2023 10:00:00",
        "Fri, 17 Mar 2023 10:00:00",
        "Sat, 18 Mar 2023 10:00:00",
        "Sun, 19 Mar 2023 10:00:00",
        "Mon, 20 Mar 2023 10:00:00",
        "Tue, 21 Mar 2023 10:00:00",
        "Wed, 22 Mar 2023 10:00:00",
    ],
    "15 12 * * ? *": [
        "Mon, 13 Mar 2023 12:15:00",
        "Tue, 14 Mar 2023 12:15:00",
        "Wed, 15 Mar 2023 12:15:00",
        "Thu, 16 Mar 2023 12:15:00",
        "Fri, 17 Mar 2023 12:15:00",
        "Sat, 18 Mar 2023 12:15:00",
        "Sun, 19 Mar 2023 12:15:00",
        "Mon, 20 Mar 2023 12:15:00",
        "Tue, 21 Mar 2023 12:15:00",
        "Wed, 22 Mar 2023 12:15:00",
    ],
    "*/5 * L * ? *": [
        "Fri, 31 Mar 2023 00:00:00",
        "Fri, 31 Mar 2023 00:05:00",
        "Fri, 31 Mar 2023 00:10:00",
        "Fri, 31 Mar 2023 00:15:00",
        "Fri, 31 Mar 2023 00:20:00",
        "Fri, 31 Mar 2023 00:25:00",
        "Fri, 31 Mar 2023 00:30:00",
        "Fri, 31 Mar 2023 00:35:00",
        "Fri, 31 Mar 2023 00:40:00",
        "Fri, 31 Mar 2023 00:45:00",
    ],
    "0 10 1 JAN,FEB,MAR ? *": [
        "Mon, 01 Jan 2024 10:00:00",
        "Thu, 01 Feb 2024 10:00:00",
        "Fri, 01 Mar 2024 10:00:00",
        "Wed, 01 Jan 2025 10:00:00",
        "Sat, 01 Feb 2025 10:00:00",
        "Sat, 01 Mar 2025 10:00:00",
        "Thu, 01 Jan 2026 10:00:00",
        "Sun, 01 Feb 2026 10:00:00",
        "Sun, 01 Mar 2026 10:00:00",
        "Fri, 01 Jan 2027 10:00:00",
    ],
    "0 16 ? * 1-5 *": [
        "Mon, 23 May 2024 16:00:00",
        "Tue, 26 May 2024 16:00:00",
        "Wed, 27 May 2024 16:00:00",
        "Thu, 28 May 2024 16:00:00",
        "Thu, 29 May 2024 16:00:00",
        "Thu, 30 May 2024 16:00:00",
        "Sun, 02 Jun 2024 16:00:00",
        "Mon, 03 Jun 2024 16:00:00",
        "Tue, 04 Jun 2024 16:00:00",
        "Wed, 05 Jun 2024 16:00:00",
    ],
    "0 5 ? * 1-5 *": [
        "Mon, 26 May 2024 05:00:00",
        "Tue, 27 May 2024 05:00:00",
        "Wed, 28 May 2024 05:00:00",
        "Thu, 29 May 2024 05:00:00",
        "Sun, 30 May 2024 05:00:00",
        "Tue, 02 Jun 2024 05:00:00",
        "Wed, 03 Jun 2024 05:00:00",
        "Thu, 04 Jun 2024 05:00:00",
        "Sun, 05 Jun 2024 05:00:00",
        "Sun, 06 Jun 2024 05:00:00",
    ],
    "0 18 ? * 2 *": [
        "Mon, 27 May 2024 18:00:00",
        "Mon, 03 Jun 2024 18:00:00",
        "Mon, 10 Jun 2024 18:00:00",
        "Mon, 17 Jun 2024 18:00:00",
        "Mon, 24 Jun 2024 18:00:00",
        "Mon, 01 Jul 2024 18:00:00",
        "Mon, 08 Jul 2024 18:00:00",
        "Mon, 15 Jul 2024 18:00:00",
        "Mon, 22 Jul 2024 18:00:00",
        "Mon, 29 Jul 2024 18:00:00",
    ],
}
