# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from terminal_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    VEHICLES = "Vehicles"
    CONNECTIONS = "Connections"
    DATA_MANAGEMENT = "Data Management"
    HOURS_OF_SERVICE = "Hours of Service"
    DRIVERS = "Drivers"
    ISSUES = "Issues"
    TRAILERS = "Trailers"
    AUTHENTICATION = "Authentication"
    GROUPS = "Groups"
    IFTA = "IFTA"
    PROVIDERS = "Providers"
    SAFETY = "Safety"
    TRIPS = "Trips"
    WEBHOOK_EVENTS = "Webhook Events"
