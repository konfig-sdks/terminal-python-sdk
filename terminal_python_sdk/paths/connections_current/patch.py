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

from terminal_python_sdk.model.connections_update_current_connection_details_request_company import ConnectionsUpdateCurrentConnectionDetailsRequestCompany as ConnectionsUpdateCurrentConnectionDetailsRequestCompanySchema
from terminal_python_sdk.model.connections_update_current_connection_details_request_tags import ConnectionsUpdateCurrentConnectionDetailsRequestTags as ConnectionsUpdateCurrentConnectionDetailsRequestTagsSchema
from terminal_python_sdk.model.connections_update_current_connection_details_request import ConnectionsUpdateCurrentConnectionDetailsRequest as ConnectionsUpdateCurrentConnectionDetailsRequestSchema

from terminal_python_sdk.type.connections_update_current_connection_details_request_tags import ConnectionsUpdateCurrentConnectionDetailsRequestTags
from terminal_python_sdk.type.connections_update_current_connection_details_request import ConnectionsUpdateCurrentConnectionDetailsRequest
from terminal_python_sdk.type.connections_update_current_connection_details_request_company import ConnectionsUpdateCurrentConnectionDetailsRequestCompany

from ...api_client import Dictionary
from terminal_python_sdk.pydantic.connections_update_current_connection_details_request_tags import ConnectionsUpdateCurrentConnectionDetailsRequestTags as ConnectionsUpdateCurrentConnectionDetailsRequestTagsPydantic
from terminal_python_sdk.pydantic.connections_update_current_connection_details_request_company import ConnectionsUpdateCurrentConnectionDetailsRequestCompany as ConnectionsUpdateCurrentConnectionDetailsRequestCompanyPydantic
from terminal_python_sdk.pydantic.connections_update_current_connection_details_request import ConnectionsUpdateCurrentConnectionDetailsRequest as ConnectionsUpdateCurrentConnectionDetailsRequestPydantic

from . import path

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
# body param
SchemaForRequestBodyApplicationJson = ConnectionsUpdateCurrentConnectionDetailsRequestSchema


request_body_connections_update_current_connection_details_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'bearerAuth',
]


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
_status_code_to_response = {
    '200': _response_for_200,
}


class BaseApi(api_client.Api):

    def _update_current_connection_details_mapped_args(
        self,
        tags: typing.Optional[ConnectionsUpdateCurrentConnectionDetailsRequestTags] = None,
        company: typing.Optional[ConnectionsUpdateCurrentConnectionDetailsRequestCompany] = None,
        external_id: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        sync_mode: typing.Optional[str] = None,
        connection_token: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _body = {}
        if tags is not None:
            _body["tags"] = tags
        if company is not None:
            _body["company"] = company
        if external_id is not None:
            _body["externalId"] = external_id
        if status is not None:
            _body["status"] = status
        if sync_mode is not None:
            _body["syncMode"] = sync_mode
        args.body = _body
        if connection_token is not None:
            _header_params["connection-token"] = connection_token
        args.header = _header_params
        return args

    async def _aupdate_current_connection_details_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Update Current Connection
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
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
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/connections/current',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_connections_update_current_connection_details_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
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


    def _update_current_connection_details_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Update Current Connection
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
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
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/connections/current',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_connections_update_current_connection_details_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
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


class UpdateCurrentConnectionDetailsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_current_connection_details(
        self,
        tags: typing.Optional[ConnectionsUpdateCurrentConnectionDetailsRequestTags] = None,
        company: typing.Optional[ConnectionsUpdateCurrentConnectionDetailsRequestCompany] = None,
        external_id: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        sync_mode: typing.Optional[str] = None,
        connection_token: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_current_connection_details_mapped_args(
            tags=tags,
            company=company,
            external_id=external_id,
            status=status,
            sync_mode=sync_mode,
            connection_token=connection_token,
        )
        return await self._aupdate_current_connection_details_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def update_current_connection_details(
        self,
        tags: typing.Optional[ConnectionsUpdateCurrentConnectionDetailsRequestTags] = None,
        company: typing.Optional[ConnectionsUpdateCurrentConnectionDetailsRequestCompany] = None,
        external_id: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        sync_mode: typing.Optional[str] = None,
        connection_token: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_current_connection_details_mapped_args(
            tags=tags,
            company=company,
            external_id=external_id,
            status=status,
            sync_mode=sync_mode,
            connection_token=connection_token,
        )
        return self._update_current_connection_details_oapg(
            body=args.body,
            header_params=args.header,
        )

class UpdateCurrentConnectionDetails(BaseApi):

    async def aupdate_current_connection_details(
        self,
        tags: typing.Optional[ConnectionsUpdateCurrentConnectionDetailsRequestTags] = None,
        company: typing.Optional[ConnectionsUpdateCurrentConnectionDetailsRequestCompany] = None,
        external_id: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        sync_mode: typing.Optional[str] = None,
        connection_token: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aupdate_current_connection_details(
            tags=tags,
            company=company,
            external_id=external_id,
            status=status,
            sync_mode=sync_mode,
            connection_token=connection_token,
            **kwargs,
        )
    
    
    def update_current_connection_details(
        self,
        tags: typing.Optional[ConnectionsUpdateCurrentConnectionDetailsRequestTags] = None,
        company: typing.Optional[ConnectionsUpdateCurrentConnectionDetailsRequestCompany] = None,
        external_id: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        sync_mode: typing.Optional[str] = None,
        connection_token: typing.Optional[str] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.update_current_connection_details(
            tags=tags,
            company=company,
            external_id=external_id,
            status=status,
            sync_mode=sync_mode,
            connection_token=connection_token,
        )


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        tags: typing.Optional[ConnectionsUpdateCurrentConnectionDetailsRequestTags] = None,
        company: typing.Optional[ConnectionsUpdateCurrentConnectionDetailsRequestCompany] = None,
        external_id: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        sync_mode: typing.Optional[str] = None,
        connection_token: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_current_connection_details_mapped_args(
            tags=tags,
            company=company,
            external_id=external_id,
            status=status,
            sync_mode=sync_mode,
            connection_token=connection_token,
        )
        return await self._aupdate_current_connection_details_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def patch(
        self,
        tags: typing.Optional[ConnectionsUpdateCurrentConnectionDetailsRequestTags] = None,
        company: typing.Optional[ConnectionsUpdateCurrentConnectionDetailsRequestCompany] = None,
        external_id: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        sync_mode: typing.Optional[str] = None,
        connection_token: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_current_connection_details_mapped_args(
            tags=tags,
            company=company,
            external_id=external_id,
            status=status,
            sync_mode=sync_mode,
            connection_token=connection_token,
        )
        return self._update_current_connection_details_oapg(
            body=args.body,
            header_params=args.header,
        )

