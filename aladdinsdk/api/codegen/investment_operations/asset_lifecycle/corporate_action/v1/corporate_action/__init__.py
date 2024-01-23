# coding: utf-8

# flake8: noqa

"""
    Aladdin Corporate Action

    A corporate action is an event triggered by a public company that changes an equity or fixed income security issued by the company. There are two main categories - Mandatory and Voluntary.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


__version__ = "1.0.0"

# import apis into sdk package
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.corporate_action.api.default_corporate_action_api import DefaultCorporateActionAPI

# import ApiClient
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.corporate_action.api_response import ApiResponse
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.corporate_action.api_client import ApiClient
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.corporate_action.configuration import Configuration
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.corporate_action.exceptions import OpenApiException
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.corporate_action.exceptions import ApiTypeError
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.corporate_action.exceptions import ApiValueError
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.corporate_action.exceptions import ApiKeyError
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.corporate_action.exceptions import ApiAttributeError
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.corporate_action.exceptions import ApiException

# import models into sdk package
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.corporate_action.models.any import Any
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.corporate_action.models.corporate_action_api_get_corporate_action400_response import CorporateActionAPIGetCorporateAction400Response
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.corporate_action.models.rpc_status import RpcStatus
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.corporate_action.models.type_date_time import TypeDateTime
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.corporate_action.models.type_time_zone import TypeTimeZone
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.corporate_action.models.v1_corporate_action import V1CorporateAction
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.corporate_action.models.v1_corporate_action_link_state import V1CorporateActionLinkState
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.corporate_action.models.v1_corporate_action_option import V1CorporateActionOption
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.corporate_action.models.v1_corporate_action_query import V1CorporateActionQuery
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.corporate_action.models.v1_corporate_action_view import V1CorporateActionView
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.corporate_action.models.v1_corporate_action_workflow_state import V1CorporateActionWorkflowState
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.corporate_action.models.v1_filter_corporate_actions_request import V1FilterCorporateActionsRequest
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.corporate_action.models.v1_filter_corporate_actions_response import V1FilterCorporateActionsResponse
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.corporate_action.models.v1_option_alignment_state import V1OptionAlignmentState
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.corporate_action.models.v1_payout import V1Payout
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.corporate_action.models.v1_payout_type import V1PayoutType
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.corporate_action.models.v1_tax_code import V1TaxCode
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.corporate_action.models.v1_voluntary_mandatory_code import V1VoluntaryMandatoryCode
