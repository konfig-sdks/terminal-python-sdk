import typing_extensions

from terminal_python_sdk.apis.tags import TagValues
from terminal_python_sdk.apis.tags.vehicles_api import VehiclesApi
from terminal_python_sdk.apis.tags.connections_api import ConnectionsApi
from terminal_python_sdk.apis.tags.data_management_api import DataManagementApi
from terminal_python_sdk.apis.tags.hours_of_service_api import HoursOfServiceApi
from terminal_python_sdk.apis.tags.drivers_api import DriversApi
from terminal_python_sdk.apis.tags.issues_api import IssuesApi
from terminal_python_sdk.apis.tags.trailers_api import TrailersApi
from terminal_python_sdk.apis.tags.authentication_api import AuthenticationApi
from terminal_python_sdk.apis.tags.groups_api import GroupsApi
from terminal_python_sdk.apis.tags.ifta_api import IFTAApi
from terminal_python_sdk.apis.tags.providers_api import ProvidersApi
from terminal_python_sdk.apis.tags.safety_api import SafetyApi
from terminal_python_sdk.apis.tags.trips_api import TripsApi
from terminal_python_sdk.apis.tags.devices_api import DevicesApi
from terminal_python_sdk.apis.tags.webhook_events_api import WebhookEventsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.VEHICLES: VehiclesApi,
        TagValues.CONNECTIONS: ConnectionsApi,
        TagValues.DATA_MANAGEMENT: DataManagementApi,
        TagValues.HOURS_OF_SERVICE: HoursOfServiceApi,
        TagValues.DRIVERS: DriversApi,
        TagValues.ISSUES: IssuesApi,
        TagValues.TRAILERS: TrailersApi,
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.GROUPS: GroupsApi,
        TagValues.IFTA: IFTAApi,
        TagValues.PROVIDERS: ProvidersApi,
        TagValues.SAFETY: SafetyApi,
        TagValues.TRIPS: TripsApi,
        TagValues.DEVICES: DevicesApi,
        TagValues.WEBHOOK_EVENTS: WebhookEventsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.VEHICLES: VehiclesApi,
        TagValues.CONNECTIONS: ConnectionsApi,
        TagValues.DATA_MANAGEMENT: DataManagementApi,
        TagValues.HOURS_OF_SERVICE: HoursOfServiceApi,
        TagValues.DRIVERS: DriversApi,
        TagValues.ISSUES: IssuesApi,
        TagValues.TRAILERS: TrailersApi,
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.GROUPS: GroupsApi,
        TagValues.IFTA: IFTAApi,
        TagValues.PROVIDERS: ProvidersApi,
        TagValues.SAFETY: SafetyApi,
        TagValues.TRIPS: TripsApi,
        TagValues.DEVICES: DevicesApi,
        TagValues.WEBHOOK_EVENTS: WebhookEventsApi,
    }
)
