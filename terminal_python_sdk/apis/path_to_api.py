import typing_extensions

from terminal_python_sdk.paths import PathValues
from terminal_python_sdk.apis.paths.public_token_exchange import PublicTokenExchange
from terminal_python_sdk.apis.paths.connections import Connections
from terminal_python_sdk.apis.paths.connections_current import ConnectionsCurrent
from terminal_python_sdk.apis.paths.syncs import Syncs
from terminal_python_sdk.apis.paths.syncs_id import SyncsId
from terminal_python_sdk.apis.paths.passthrough import Passthrough
from terminal_python_sdk.apis.paths.drivers import Drivers
from terminal_python_sdk.apis.paths.drivers_id import DriversId
from terminal_python_sdk.apis.paths.groups import Groups
from terminal_python_sdk.apis.paths.hos_available_time import HosAvailableTime
from terminal_python_sdk.apis.paths.hos_logs import HosLogs
from terminal_python_sdk.apis.paths.hos_daily_logs import HosDailyLogs
from terminal_python_sdk.apis.paths.ifta_summary import IftaSummary
from terminal_python_sdk.apis.paths.issues import Issues
from terminal_python_sdk.apis.paths.issues_issue_id_resolve import IssuesIssueIdResolve
from terminal_python_sdk.apis.paths.providers import Providers
from terminal_python_sdk.apis.paths.safety_events import SafetyEvents
from terminal_python_sdk.apis.paths.trailers import Trailers
from terminal_python_sdk.apis.paths.trailers_locations import TrailersLocations
from terminal_python_sdk.apis.paths.vehicles import Vehicles
from terminal_python_sdk.apis.paths.vehicles_id import VehiclesId
from terminal_python_sdk.apis.paths.vehicles_locations import VehiclesLocations
from terminal_python_sdk.apis.paths.vehicles_vehicle_id_locations import VehiclesVehicleIdLocations
from terminal_python_sdk.apis.paths.vehicles_vehicle_id_stats_historical import VehiclesVehicleIdStatsHistorical
from terminal_python_sdk.apis.paths.trips import Trips

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.PUBLICTOKEN_EXCHANGE: PublicTokenExchange,
        PathValues.CONNECTIONS: Connections,
        PathValues.CONNECTIONS_CURRENT: ConnectionsCurrent,
        PathValues.SYNCS: Syncs,
        PathValues.SYNCS_ID: SyncsId,
        PathValues.PASSTHROUGH: Passthrough,
        PathValues.DRIVERS: Drivers,
        PathValues.DRIVERS_ID: DriversId,
        PathValues.GROUPS: Groups,
        PathValues.HOS_AVAILABLETIME: HosAvailableTime,
        PathValues.HOS_LOGS: HosLogs,
        PathValues.HOS_DAILYLOGS: HosDailyLogs,
        PathValues.IFTA_SUMMARY: IftaSummary,
        PathValues.ISSUES: Issues,
        PathValues.ISSUES_ISSUE_ID_RESOLVE: IssuesIssueIdResolve,
        PathValues.PROVIDERS: Providers,
        PathValues.SAFETY_EVENTS: SafetyEvents,
        PathValues.TRAILERS: Trailers,
        PathValues.TRAILERS_LOCATIONS: TrailersLocations,
        PathValues.VEHICLES: Vehicles,
        PathValues.VEHICLES_ID: VehiclesId,
        PathValues.VEHICLES_LOCATIONS: VehiclesLocations,
        PathValues.VEHICLES_VEHICLE_ID_LOCATIONS: VehiclesVehicleIdLocations,
        PathValues.VEHICLES_VEHICLE_ID_STATS_HISTORICAL: VehiclesVehicleIdStatsHistorical,
        PathValues.TRIPS: Trips,
    }
)

path_to_api = PathToApi(
    {
        PathValues.PUBLICTOKEN_EXCHANGE: PublicTokenExchange,
        PathValues.CONNECTIONS: Connections,
        PathValues.CONNECTIONS_CURRENT: ConnectionsCurrent,
        PathValues.SYNCS: Syncs,
        PathValues.SYNCS_ID: SyncsId,
        PathValues.PASSTHROUGH: Passthrough,
        PathValues.DRIVERS: Drivers,
        PathValues.DRIVERS_ID: DriversId,
        PathValues.GROUPS: Groups,
        PathValues.HOS_AVAILABLETIME: HosAvailableTime,
        PathValues.HOS_LOGS: HosLogs,
        PathValues.HOS_DAILYLOGS: HosDailyLogs,
        PathValues.IFTA_SUMMARY: IftaSummary,
        PathValues.ISSUES: Issues,
        PathValues.ISSUES_ISSUE_ID_RESOLVE: IssuesIssueIdResolve,
        PathValues.PROVIDERS: Providers,
        PathValues.SAFETY_EVENTS: SafetyEvents,
        PathValues.TRAILERS: Trailers,
        PathValues.TRAILERS_LOCATIONS: TrailersLocations,
        PathValues.VEHICLES: Vehicles,
        PathValues.VEHICLES_ID: VehiclesId,
        PathValues.VEHICLES_LOCATIONS: VehiclesLocations,
        PathValues.VEHICLES_VEHICLE_ID_LOCATIONS: VehiclesVehicleIdLocations,
        PathValues.VEHICLES_VEHICLE_ID_STATS_HISTORICAL: VehiclesVehicleIdStatsHistorical,
        PathValues.TRIPS: Trips,
    }
)
