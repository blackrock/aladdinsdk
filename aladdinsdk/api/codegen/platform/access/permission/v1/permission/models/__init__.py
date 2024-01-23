# coding: utf-8

# flake8: noqa
"""
    Aladdin Permission

    API contains operations on Aladdin Permission resource. Permissions cannot be applied directly to a user, they must be applied to a User Group first, then the user is added to a User Group. Note: This is not intended to be used for Authorization.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


# import models into model package
from aladdinsdk.api.codegen.platform.access.permission.v1.permission.models.any import Any
from aladdinsdk.api.codegen.platform.access.permission.v1.permission.models.permission_api_get_permission400_response import PermissionAPIGetPermission400Response
from aladdinsdk.api.codegen.platform.access.permission.v1.permission.models.rpc_status import RpcStatus
from aladdinsdk.api.codegen.platform.access.permission.v1.permission.models.v1_filter_permissions_request import V1FilterPermissionsRequest
from aladdinsdk.api.codegen.platform.access.permission.v1.permission.models.v1_filter_permissions_response import V1FilterPermissionsResponse
from aladdinsdk.api.codegen.platform.access.permission.v1.permission.models.v1_permission import V1Permission
from aladdinsdk.api.codegen.platform.access.permission.v1.permission.models.v1_permission_query import V1PermissionQuery
from aladdinsdk.api.codegen.platform.access.permission.v1.permission.models.v1_permission_sensitivity_grade import V1PermissionSensitivityGrade
