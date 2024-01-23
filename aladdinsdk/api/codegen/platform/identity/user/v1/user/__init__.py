# coding: utf-8

# flake8: noqa

"""
    Aladdin User

     API contains operations on Aladdin User resource.  # Description  An Aladdin User is a person or a system account that can login into  Aladdin client's website and may be granted access to Aladdin applications.  ## Example Use Cases   This API may be used to:   - create records of Aladdin Client's employees   - retrieve information about     = Aladdin Client's employees granted access to Aladdin     = BlackRock employees granted access to client's Aladdin products     = bot accounts granted access to Aladdin   - modify Aladdin Client's employees records in Aladdin system   - search User records by email or client's internal user id (if populated)  ## Implementation Status  This API is production ready. In the future it will be enhanced with additional search capabilities    [Developer Guide]: apps/aladdin-developer-portal/#/guides/developer-guide   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


__version__ = "1.0.0"

# import apis into sdk package
from aladdinsdk.api.codegen.platform.identity.user.v1.user.api.default_user_api import DefaultUserAPI

# import ApiClient
from aladdinsdk.api.codegen.platform.identity.user.v1.user.api_response import ApiResponse
from aladdinsdk.api.codegen.platform.identity.user.v1.user.api_client import ApiClient
from aladdinsdk.api.codegen.platform.identity.user.v1.user.configuration import Configuration
from aladdinsdk.api.codegen.platform.identity.user.v1.user.exceptions import OpenApiException
from aladdinsdk.api.codegen.platform.identity.user.v1.user.exceptions import ApiTypeError
from aladdinsdk.api.codegen.platform.identity.user.v1.user.exceptions import ApiValueError
from aladdinsdk.api.codegen.platform.identity.user.v1.user.exceptions import ApiKeyError
from aladdinsdk.api.codegen.platform.identity.user.v1.user.exceptions import ApiAttributeError
from aladdinsdk.api.codegen.platform.identity.user.v1.user.exceptions import ApiException

# import models into sdk package
from aladdinsdk.api.codegen.platform.identity.user.v1.user.models.any import Any
from aladdinsdk.api.codegen.platform.identity.user.v1.user.models.enums_user_type import EnumsUserType
from aladdinsdk.api.codegen.platform.identity.user.v1.user.models.rpc_status import RpcStatus
from aladdinsdk.api.codegen.platform.identity.user.v1.user.models.user_api_list_users400_response import UserAPIListUsers400Response
from aladdinsdk.api.codegen.platform.identity.user.v1.user.models.user_user_profile import UserUserProfile
from aladdinsdk.api.codegen.platform.identity.user.v1.user.models.user_user_record_status import UserUserRecordStatus
from aladdinsdk.api.codegen.platform.identity.user.v1.user.models.v1_alternate_id import V1AlternateId
from aladdinsdk.api.codegen.platform.identity.user.v1.user.models.v1_list_users_response import V1ListUsersResponse
from aladdinsdk.api.codegen.platform.identity.user.v1.user.models.v1_user import V1User
