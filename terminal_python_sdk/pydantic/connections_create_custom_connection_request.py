# coding: utf-8

"""
    Terminal API

    Terminal is a unified API that makes it easy to integrate with the leading telematics service providers.  Contact Support:  Name: Terminal  Email: connect@withterminal.com

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel

from terminal_python_sdk.pydantic.connections_create_custom_connection_request_backfill import ConnectionsCreateCustomConnectionRequestBackfill
from terminal_python_sdk.pydantic.connections_create_custom_connection_request_company import ConnectionsCreateCustomConnectionRequestCompany
from terminal_python_sdk.pydantic.connections_create_custom_connection_request_credentials import ConnectionsCreateCustomConnectionRequestCredentials
from terminal_python_sdk.pydantic.connections_create_custom_connection_request_tags import ConnectionsCreateCustomConnectionRequestTags

class ConnectionsCreateCustomConnectionRequest(BaseModel):
    tags: typing.Optional[ConnectionsCreateCustomConnectionRequestTags] = Field(None, alias='tags')

    backfill: typing.Optional[ConnectionsCreateCustomConnectionRequestBackfill] = Field(None, alias='backfill')

    company: typing.Optional[ConnectionsCreateCustomConnectionRequestCompany] = Field(None, alias='company')

    credentials: typing.Optional[ConnectionsCreateCustomConnectionRequestCredentials] = Field(None, alias='credentials')

    external_id: typing.Optional[str] = Field(None, alias='externalId')

    provider: typing.Optional[str] = Field(None, alias='provider')

    sync_mode: typing.Optional[str] = Field(None, alias='syncMode')
    class Config:
        arbitrary_types_allowed = True
