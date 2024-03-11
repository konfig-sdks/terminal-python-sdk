# coding: utf-8

"""
    Terminal API

    Terminal is a unified API that makes it easy to integrate with the leading telematics service providers.  Contact Support:  Name: Terminal  Email: connect@withterminal.com

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from terminal_python_sdk.paths.ifta_summary.get import GetMonthlyReports
from terminal_python_sdk.apis.tags.ifta_api_raw import IFTAApiRaw


class IFTAApi(
    GetMonthlyReports,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: IFTAApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = IFTAApiRaw(api_client)