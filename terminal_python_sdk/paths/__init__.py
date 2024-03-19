# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from terminal_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    PUBLICTOKEN_EXCHANGE = "/public-token/exchange"
    CONNECTIONS = "/connections"
    CONNECTIONS_CURRENT = "/connections/current"
    SYNCS = "/syncs"
    SYNCS_ID = "/syncs/{id}"
    PASSTHROUGH = "/passthrough"
    DRIVERS = "/drivers"
    DRIVERS_ID = "/drivers/{id}"
    GROUPS = "/groups"
    HOS_AVAILABLETIME = "/hos/available-time"
    HOS_LOGS = "/hos/logs"
    HOS_DAILYLOGS = "/hos/daily-logs"
    IFTA_SUMMARY = "/ifta/summary"
    ISSUES = "/issues"
    ISSUES_ISSUE_ID_RESOLVE = "/issues/{issueId}/resolve"
    PROVIDERS = "/providers"
    SAFETY_EVENTS = "/safety/events"
    TRAILERS = "/trailers"
    TRAILERS_LOCATIONS = "/trailers/locations"
    VEHICLES = "/vehicles"
    VEHICLES_ID = "/vehicles/{id}"
    VEHICLES_LOCATIONS = "/vehicles/locations"
    VEHICLES_VEHICLE_ID_LOCATIONS = "/vehicles/{vehicleId}/locations"
    VEHICLES_VEHICLE_ID_STATS_HISTORICAL = "/vehicles/{vehicleId}/stats/historical"
    TRIPS = "/trips"
    DEVICES = "/devices"
