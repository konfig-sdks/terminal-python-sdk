# coding: utf-8
"""
    Terminal API

    Terminal is a unified API that makes it easy to integrate with the leading telematics service providers.  Contact Support:  Name: Terminal  Email: connect@withterminal.com

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

import typing
import inspect
from datetime import date, datetime
from terminal_python_sdk.client_custom import ClientCustom
from terminal_python_sdk.configuration import Configuration
from terminal_python_sdk.api_client import ApiClient
from terminal_python_sdk.type_util import copy_signature
from terminal_python_sdk.apis.tags.authentication_api import AuthenticationApi
from terminal_python_sdk.apis.tags.connections_api import ConnectionsApi
from terminal_python_sdk.apis.tags.data_management_api import DataManagementApi
from terminal_python_sdk.apis.tags.drivers_api import DriversApi
from terminal_python_sdk.apis.tags.groups_api import GroupsApi
from terminal_python_sdk.apis.tags.hours_of_service_api import HoursOfServiceApi
from terminal_python_sdk.apis.tags.ifta_api import IFTAApi
from terminal_python_sdk.apis.tags.issues_api import IssuesApi
from terminal_python_sdk.apis.tags.providers_api import ProvidersApi
from terminal_python_sdk.apis.tags.safety_api import SafetyApi
from terminal_python_sdk.apis.tags.trailers_api import TrailersApi
from terminal_python_sdk.apis.tags.trips_api import TripsApi
from terminal_python_sdk.apis.tags.vehicles_api import VehiclesApi



class Terminal(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.authentication: AuthenticationApi = AuthenticationApi(api_client)
        self.connections: ConnectionsApi = ConnectionsApi(api_client)
        self.data_management: DataManagementApi = DataManagementApi(api_client)
        self.drivers: DriversApi = DriversApi(api_client)
        self.groups: GroupsApi = GroupsApi(api_client)
        self.hours_of_service: HoursOfServiceApi = HoursOfServiceApi(api_client)
        self.ifta: IFTAApi = IFTAApi(api_client)
        self.issues: IssuesApi = IssuesApi(api_client)
        self.providers: ProvidersApi = ProvidersApi(api_client)
        self.safety: SafetyApi = SafetyApi(api_client)
        self.trailers: TrailersApi = TrailersApi(api_client)
        self.trips: TripsApi = TripsApi(api_client)
        self.vehicles: VehiclesApi = VehiclesApi(api_client)
