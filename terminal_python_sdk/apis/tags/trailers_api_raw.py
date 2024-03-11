# coding: utf-8

"""
    Terminal API

    Terminal is a unified API that makes it easy to integrate with the leading telematics service providers.  Contact Support:  Name: Terminal  Email: connect@withterminal.com

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from terminal_python_sdk.paths.trailers.get import GetAllTrailersRaw
from terminal_python_sdk.paths.trailers_locations.get import ListLatestLocationsRaw


class TrailersApiRaw(
    GetAllTrailersRaw,
    ListLatestLocationsRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
