# coding: utf-8

"""
    Terminal API

    Terminal is a unified API that makes it easy to integrate with the leading telematics service providers.  Contact Support:  Name: Terminal  Email: connect@withterminal.com

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from terminal_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from terminal_python_sdk.api_response import AsyncGeneratorResponse
from terminal_python_sdk import api_client, exceptions
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



from ...api_client import Dictionary

# Query params
CursorSchema = schemas.StrSchema
LimitSchema = schemas.StrSchema
StartAtSchema = schemas.StrSchema
EndAtSchema = schemas.StrSchema
RawSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'cursor': typing.Union[CursorSchema, str, ],
        'limit': typing.Union[LimitSchema, str, ],
        'startAt': typing.Union[StartAtSchema, str, ],
        'endAt': typing.Union[EndAtSchema, str, ],
        'raw': typing.Union[RawSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_cursor = api_client.QueryParameter(
    name="cursor",
    style=api_client.ParameterStyle.FORM,
    schema=CursorSchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
request_query_start_at = api_client.QueryParameter(
    name="startAt",
    style=api_client.ParameterStyle.FORM,
    schema=StartAtSchema,
    explode=True,
)
request_query_end_at = api_client.QueryParameter(
    name="endAt",
    style=api_client.ParameterStyle.FORM,
    schema=EndAtSchema,
    explode=True,
)
request_query_raw = api_client.QueryParameter(
    name="raw",
    style=api_client.ParameterStyle.FORM,
    schema=RawSchema,
    explode=True,
)
# Header params
ConnectionTokenSchema = schemas.StrSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'connection-token': typing.Union[ConnectionTokenSchema, str, ],
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_connection_token = api_client.HeaderParameter(
    name="connection-token",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ConnectionTokenSchema,
)
# Path params
VehicleIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'vehicleId': typing.Union[VehicleIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_vehicle_id = api_client.PathParameter(
    name="vehicleId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=VehicleIdSchema,
    required=True,
)


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
)


class BaseApi(api_client.Api):

    def _list_historical_locations_mapped_args(
        self,
        vehicle_id: str,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[str] = None,
        start_at: typing.Optional[str] = None,
        end_at: typing.Optional[str] = None,
        raw: typing.Optional[str] = None,
        connection_token: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _header_params = {}
        _path_params = {}
        if cursor is not None:
            _query_params["cursor"] = cursor
        if limit is not None:
            _query_params["limit"] = limit
        if start_at is not None:
            _query_params["startAt"] = start_at
        if end_at is not None:
            _query_params["endAt"] = end_at
        if raw is not None:
            _query_params["raw"] = raw
        if connection_token is not None:
            _header_params["connection-token"] = connection_token
        if vehicle_id is not None:
            _path_params["vehicleId"] = vehicle_id
        args.query = _query_params
        args.header = _header_params
        args.path = _path_params
        return args

    async def _alist_historical_locations_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Historical Vehicle Locations
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_vehicle_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_cursor,
            request_query_limit,
            request_query_start_at,
            request_query_end_at,
            request_query_raw,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_connection_token,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/vehicles/{vehicleId}/locations',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _list_historical_locations_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Historical Vehicle Locations
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_vehicle_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_cursor,
            request_query_limit,
            request_query_start_at,
            request_query_end_at,
            request_query_raw,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_connection_token,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/vehicles/{vehicleId}/locations',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class ListHistoricalLocationsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_historical_locations(
        self,
        vehicle_id: str,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[str] = None,
        start_at: typing.Optional[str] = None,
        end_at: typing.Optional[str] = None,
        raw: typing.Optional[str] = None,
        connection_token: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_historical_locations_mapped_args(
            vehicle_id=vehicle_id,
            cursor=cursor,
            limit=limit,
            start_at=start_at,
            end_at=end_at,
            raw=raw,
            connection_token=connection_token,
        )
        return await self._alist_historical_locations_oapg(
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def list_historical_locations(
        self,
        vehicle_id: str,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[str] = None,
        start_at: typing.Optional[str] = None,
        end_at: typing.Optional[str] = None,
        raw: typing.Optional[str] = None,
        connection_token: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_historical_locations_mapped_args(
            vehicle_id=vehicle_id,
            cursor=cursor,
            limit=limit,
            start_at=start_at,
            end_at=end_at,
            raw=raw,
            connection_token=connection_token,
        )
        return self._list_historical_locations_oapg(
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
        )

class ListHistoricalLocations(BaseApi):

    async def alist_historical_locations(
        self,
        vehicle_id: str,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[str] = None,
        start_at: typing.Optional[str] = None,
        end_at: typing.Optional[str] = None,
        raw: typing.Optional[str] = None,
        connection_token: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.alist_historical_locations(
            vehicle_id=vehicle_id,
            cursor=cursor,
            limit=limit,
            start_at=start_at,
            end_at=end_at,
            raw=raw,
            connection_token=connection_token,
            **kwargs,
        )
    
    
    def list_historical_locations(
        self,
        vehicle_id: str,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[str] = None,
        start_at: typing.Optional[str] = None,
        end_at: typing.Optional[str] = None,
        raw: typing.Optional[str] = None,
        connection_token: typing.Optional[str] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.list_historical_locations(
            vehicle_id=vehicle_id,
            cursor=cursor,
            limit=limit,
            start_at=start_at,
            end_at=end_at,
            raw=raw,
            connection_token=connection_token,
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        vehicle_id: str,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[str] = None,
        start_at: typing.Optional[str] = None,
        end_at: typing.Optional[str] = None,
        raw: typing.Optional[str] = None,
        connection_token: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_historical_locations_mapped_args(
            vehicle_id=vehicle_id,
            cursor=cursor,
            limit=limit,
            start_at=start_at,
            end_at=end_at,
            raw=raw,
            connection_token=connection_token,
        )
        return await self._alist_historical_locations_oapg(
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        vehicle_id: str,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[str] = None,
        start_at: typing.Optional[str] = None,
        end_at: typing.Optional[str] = None,
        raw: typing.Optional[str] = None,
        connection_token: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_historical_locations_mapped_args(
            vehicle_id=vehicle_id,
            cursor=cursor,
            limit=limit,
            start_at=start_at,
            end_at=end_at,
            raw=raw,
            connection_token=connection_token,
        )
        return self._list_historical_locations_oapg(
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
        )
