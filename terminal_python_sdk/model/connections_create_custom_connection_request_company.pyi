# coding: utf-8

"""
    Terminal API

    Terminal is a unified API that makes it easy to integrate with the leading telematics service providers.  Contact Support:  Name: Terminal  Email: connect@withterminal.com

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from terminal_python_sdk import schemas  # noqa: F401


class ConnectionsCreateCustomConnectionRequestCompany(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def dotNumbers() -> typing.Type['ConnectionsCreateCustomConnectionRequestCompanyDotNumbers']:
                return ConnectionsCreateCustomConnectionRequestCompanyDotNumbers
            name = schemas.StrSchema
            __annotations__ = {
                "dotNumbers": dotNumbers,
                "name": name,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dotNumbers"]) -> 'ConnectionsCreateCustomConnectionRequestCompanyDotNumbers': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["dotNumbers", "name", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dotNumbers"]) -> typing.Union['ConnectionsCreateCustomConnectionRequestCompanyDotNumbers', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["dotNumbers", "name", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        dotNumbers: typing.Union['ConnectionsCreateCustomConnectionRequestCompanyDotNumbers', schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ConnectionsCreateCustomConnectionRequestCompany':
        return super().__new__(
            cls,
            *args,
            dotNumbers=dotNumbers,
            name=name,
            _configuration=_configuration,
            **kwargs,
        )

from terminal_python_sdk.model.connections_create_custom_connection_request_company_dot_numbers import ConnectionsCreateCustomConnectionRequestCompanyDotNumbers