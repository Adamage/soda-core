import logging

from soda.common.logs import Logs
from soda.execution.data_source import DataSource

logger = logging.getLogger(__name__)


class Db2Datasource(DataSource):
    def __init__(self, logs: Logs, data_source_name: str, data_source_properties: dict):
        super().__init__(logs, data_source_name, data_source_properties)
