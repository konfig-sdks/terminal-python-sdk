# coding: utf-8

"""
    Terminal API

    Terminal is a unified API that makes it easy to integrate with the leading telematics service providers.  Contact Support:  Name: Terminal  Email: connect@withterminal.com

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from terminal_python_sdk.paths.connections.post import CreateCustomConnection
from terminal_python_sdk.paths.connections_current.get import GetCurrentDetails
from terminal_python_sdk.paths.connections.get import ListAll
from terminal_python_sdk.paths.connections_current.patch import UpdateCurrentConnectionDetails
from terminal_python_sdk.apis.tags.connections_api_raw import ConnectionsApiRaw


class ConnectionsApi(
    CreateCustomConnection,
    GetCurrentDetails,
    ListAll,
    UpdateCurrentConnectionDetails,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ConnectionsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ConnectionsApiRaw(api_client)
