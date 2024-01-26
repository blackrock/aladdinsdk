# coding: utf-8

# flake8: noqa

"""
    Token

    Handling and retrieval of tokens from Okta.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


__version__ = "1.0.0"

# import apis into sdk package
from aladdinsdk.api.codegen.platform.infrastructure.token.v1.TokenAPI.api.default_token_api import DefaultTokenAPI

# import ApiClient
from aladdinsdk.api.codegen.platform.infrastructure.token.v1.TokenAPI.api_response import ApiResponse
from aladdinsdk.api.codegen.platform.infrastructure.token.v1.TokenAPI.api_client import ApiClient
from aladdinsdk.api.codegen.platform.infrastructure.token.v1.TokenAPI.configuration import Configuration
from aladdinsdk.api.codegen.platform.infrastructure.token.v1.TokenAPI.exceptions import OpenApiException
from aladdinsdk.api.codegen.platform.infrastructure.token.v1.TokenAPI.exceptions import ApiTypeError
from aladdinsdk.api.codegen.platform.infrastructure.token.v1.TokenAPI.exceptions import ApiValueError
from aladdinsdk.api.codegen.platform.infrastructure.token.v1.TokenAPI.exceptions import ApiKeyError
from aladdinsdk.api.codegen.platform.infrastructure.token.v1.TokenAPI.exceptions import ApiAttributeError
from aladdinsdk.api.codegen.platform.infrastructure.token.v1.TokenAPI.exceptions import ApiException

# import models into sdk package
from aladdinsdk.api.codegen.platform.infrastructure.token.v1.TokenAPI.models.any import Any
from aladdinsdk.api.codegen.platform.infrastructure.token.v1.TokenAPI.models.rpc_status import RpcStatus
from aladdinsdk.api.codegen.platform.infrastructure.token.v1.TokenAPI.models.token_api_generate_authorization_url400_response import TokenAPIGenerateAuthorizationUrl400Response
from aladdinsdk.api.codegen.platform.infrastructure.token.v1.TokenAPI.models.v1_authorization_url import V1AuthorizationUrl
from aladdinsdk.api.codegen.platform.infrastructure.token.v1.TokenAPI.models.v1_check_token_exists_response import V1CheckTokenExistsResponse
from aladdinsdk.api.codegen.platform.infrastructure.token.v1.TokenAPI.models.v1_token import V1Token