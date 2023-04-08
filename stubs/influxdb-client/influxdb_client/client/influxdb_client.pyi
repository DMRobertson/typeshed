from _typeshed import Incomplete
from types import TracebackType
from typing_extensions import Self

from influxdb_client import HealthCheck, InvokableScriptsApi, Ready
from influxdb_client.client._base import _BaseClient
from influxdb_client.client.authorizations_api import AuthorizationsApi
from influxdb_client.client.bucket_api import BucketsApi
from influxdb_client.client.delete_api import DeleteApi
from influxdb_client.client.labels_api import LabelsApi
from influxdb_client.client.organizations_api import OrganizationsApi
from influxdb_client.client.query_api import QueryApi, QueryOptions
from influxdb_client.client.tasks_api import TasksApi
from influxdb_client.client.users_api import UsersApi
from influxdb_client.client.write_api import PointSettings, WriteApi, WriteOptions

logger: Incomplete

class InfluxDBClient(_BaseClient):
    api_client: Incomplete
    def __init__(
        self,
        url: str,
        token: str | None = None,
        debug: bool | None = None,
        timeout: int = 10000,
        enable_gzip: bool = False,
        org: str | None = None,
        default_tags: dict[Incomplete, Incomplete] | None = None,
        *,
        verify_ssl: bool = ...,
        ssl_ca_cert: Incomplete | None = ...,
        cert_file: Incomplete | None = ...,
        cert_key_file: Incomplete | None = ...,
        cert_key_password: Incomplete | None = ...,
        ssl_context: Incomplete | None = ...,
        proxy: Incomplete | None = ...,
        proxy_headers: Incomplete | None = ...,
        connection_pool_maxsize: int = ...,
        username: Incomplete | None = ...,
        password: Incomplete | None = ...,
        auth_basic: bool = ...,
        retries: bool | Incomplete = ...,
        profilers: Incomplete | None = ...,
    ) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None
    ) -> None: ...
    @classmethod
    def from_config_file(
        cls, config_file: str = "config.ini", debug: Incomplete | None = None, enable_gzip: bool = False, **kwargs
    ): ...
    @classmethod
    def from_env_properties(cls, debug: Incomplete | None = None, enable_gzip: bool = False, **kwargs): ...
    def write_api(self, write_options: WriteOptions = ..., point_settings: PointSettings = ..., **kwargs) -> WriteApi: ...
    def query_api(self, query_options: QueryOptions = ...) -> QueryApi: ...
    def invokable_scripts_api(self) -> InvokableScriptsApi: ...
    def close(self) -> None: ...
    def __del__(self) -> None: ...
    def buckets_api(self) -> BucketsApi: ...
    def authorizations_api(self) -> AuthorizationsApi: ...
    def users_api(self) -> UsersApi: ...
    def organizations_api(self) -> OrganizationsApi: ...
    def tasks_api(self) -> TasksApi: ...
    def labels_api(self) -> LabelsApi: ...
    def health(self) -> HealthCheck: ...
    def ping(self) -> bool: ...
    def version(self) -> str: ...
    def build(self) -> str: ...
    def ready(self) -> Ready: ...
    def delete_api(self) -> DeleteApi: ...
