from __future__ import annotations

from airflow.models.baseoperator import BaseOperator
from airflow.utils.context import Context


class SnowflakeAuditLogOperator(BaseOperator):
    """
    Operator that prints a sql string.
    """

    ui_color = "#e8f7e4"
    inherits_from_empty_operator = True

    def execute(self, context: Context, sql: str):
        print(sql)
