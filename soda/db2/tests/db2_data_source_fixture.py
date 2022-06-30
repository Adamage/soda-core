from __future__ import annotations

import logging
import os

from helpers.data_source_fixture import DataSourceFixture

logger = logging.getLogger(__name__)


class Db2DataSourceFixture(DataSourceFixture):
    def __init__(self, test_data_source: str):
        super().__init__(test_data_source=test_data_source)
        is_local_dev = os.getenv("GITHUB_ACTIONS") is None

    def _build_configuration_dict(self, schema_name: str | None = None) -> dict:
        return {
            "data_source db2": {
                "type": "db2",
                "host": "localhost",
                "port" "50000"
                "username": os.getenv("DB2_USERNAME", "db2inst1"),
                "password": os.getenv("DB2_PASSWORD", "password"),
                "database": os.getenv("DB2_DATABASE", "testdb"),
            }
        }

    def _create_schema_if_not_exists_sql(self):
        return f"CREATE SCHEMA IF NOT EXISTS {self.schema_name} AUTHORIZATION CURRENT_USER"

    def _drop_schema_if_exists_sql(self):
        return f"DROP SCHEMA IF EXISTS {self.schema_name} CASCADE"
