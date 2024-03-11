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


class ConnectionsCreateCustomConnectionRequestCredentials(BaseModel):
    database: typing.Optional[str] = Field(None, alias='database')

    password: typing.Optional[str] = Field(None, alias='password')

    username: typing.Optional[str] = Field(None, alias='username')
    class Config:
        arbitrary_types_allowed = True
