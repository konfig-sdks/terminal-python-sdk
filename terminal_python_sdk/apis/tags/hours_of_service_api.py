# coding: utf-8

"""
    Terminal API

    Terminal is a unified API that makes it easy to integrate with the leading telematics service providers.  Contact Support:  Name: Terminal  Email: connect@withterminal.com

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from terminal_python_sdk.paths.hos_available_time.get import GetAvailableTime
from terminal_python_sdk.paths.hos_daily_logs.get import GetDailyLogs
from terminal_python_sdk.paths.hos_logs.get import ListHosLogs
from terminal_python_sdk.apis.tags.hours_of_service_api_raw import HoursOfServiceApiRaw


class HoursOfServiceApi(
    GetAvailableTime,
    GetDailyLogs,
    ListHosLogs,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: HoursOfServiceApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = HoursOfServiceApiRaw(api_client)