from dataclasses import dataclass, asdict
from json import dumps


@dataclass
class CronrangeOutput:
    executions: list

    def __str__(self):
        return self.to_text()

    def to_json(self) -> str:
        return dumps(asdict(self))

    def to_text(self) -> str:
        return ", ".join([elem for elem in self.executions])

    def to_column(self) -> str:
        return "\n".join([elem for elem in self.executions])
