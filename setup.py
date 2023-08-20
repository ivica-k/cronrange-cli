# !/usr/bin/env python

__version__ = "1.0.0"

from distutils.core import setup
from pathlib import Path


current_dir = Path(__file__).parent

setup(
    name="cronrange",
    version=__version__,
    description="Displays the next N number of executions for a given cron expression, with an optional start datetime.",
    long_description=(current_dir / "README.md").read_text(),
    long_description_content_type="text/markdown",
    author="Ivica Kolenkaš",
    author_email="ivica.kolenkas@gmail.com",
    url="https://github.com/ivica-k/cronrange-cli",
    python_requires=">=3.6",
    packages=["cronrange"],
    license="MPL2.0",
    setup_requires=["wheel"],
    package_dir={"cronrange": "cronrange"},
    entry_points={
        "console_scripts": ["cronrange=cronrange.main:cli"],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)