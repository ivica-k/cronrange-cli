from json import dumps


class CronrangeOutput:
    def __init__(self, executions, expression, format):
        self.executions = executions
        self.expression = expression
        self.count = len(self.executions)
        self.format = format

        if self.format == "column":
            print(self.to_column())

        elif self.format == "json":
            print(self.to_json())

        else:
            print(self.to_text())

    def __str__(self):
        return self.to_text()

    def to_json(self) -> str:
        return dumps(self.executions)

    def to_text(self) -> str:
        return ", ".join([elem for elem in self.executions])

    def to_column(self) -> str:
        return "\n".join([elem for elem in self.executions])
