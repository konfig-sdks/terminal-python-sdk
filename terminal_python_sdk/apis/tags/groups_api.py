# coding: utf-8

"""
    Terminal API

    Terminal is a unified API that makes it easy to integrate with the leading telematics service providers.  Contact Support:  Name: Terminal  Email: connect@withterminal.com

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from terminal_python_sdk.paths.groups.get import GetAllGroups
from terminal_python_sdk.apis.tags.groups_api_raw import GroupsApiRaw


class GroupsApi(
    GetAllGroups,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: GroupsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = GroupsApiRaw(api_client)
