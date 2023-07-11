from __future__ import annotations

from airflow.models.baseoperator import BaseOperator
from airflow.utils.context import Context


class SnowflakeAuditLogOperator(BaseOperator):
    """
    Operator that prints a sql string.
    """

    ui_color = "#e8f7e4"
    inherits_from_empty_operator = True
    def __init__(
        self,
        *,
        sql: str
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.sql = sql

    def execute(self, context: Context):
        print(self.sql)
