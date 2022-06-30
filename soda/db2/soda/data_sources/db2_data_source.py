import logging

import ibm_db
from soda.common.logs import Logs
from soda.execution.data_source import DataSource

logger = logging.getLogger(__name__)


class Db2Datasource(DataSource):
    def __init__(self, logs: Logs, data_source_name: str, data_source_properties: dict):
        super().__init__(logs, data_source_name, data_source_properties)
        self.host = data_source_properties.get("host")
        self.port = data_source_properties.get("port")
        self.password = data_source_properties.get("password")
        self.username = data_source_properties.get("username")
        self.database = data_source_properties.get("database")

    def connect(self):
        conn_str = (
            f"DATABASE={self.database};HOSTNAME={self.host};PORT={self.port};UID={self.username};PWD={self.password}"
        )
        self.connection = ibm_db.connect(conn_str, "", "")

        return self.connection

    def validate_configuration(self, logs: Logs) -> None:
        pass
