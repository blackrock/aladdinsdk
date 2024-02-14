# coding: utf-8

# flake8: noqa

"""
    Capital Flows 1.0.0

    Capital flows are the cash and asset subscriptions coming into a fund and the cash and asset redemptions going out of a fund (e.g., client contributions, withdrawals, and initial funding for a portfolio). This API permits users to validate, create, update, and receive capital flows transactions and their details. User needs standard API permissison ALADDIN_API_USER to use the Capital Flows API and standard newcash permissions to perform different actions. Please refer to the Capital Flows User Guide on the client landing page for more information on newcash permission structure.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


__version__ = "1.0.0"

# import apis into sdk package
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.api.default_enriched_capital_flow_api import DefaultEnrichedCapitalFlowAPI

# import ApiClient
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.api_response import ApiResponse
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.api_client import ApiClient
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.configuration import Configuration
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.exceptions import OpenApiException
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.exceptions import ApiTypeError
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.exceptions import ApiValueError
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.exceptions import ApiKeyError
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.exceptions import ApiAttributeError
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.exceptions import ApiException

# import models into sdk package
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.models.any import Any
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.models.enriched_capital_flow_api_transition_enriched_capital_flow400_response import EnrichedCapitalFlowAPITransitionEnrichedCapitalFlow400Response
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.models.enums_action import EnumsAction
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.models.enums_capital_flow_basis import EnumsCapitalFlowBasis
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.models.enums_capital_flow_transaction_type import EnumsCapitalFlowTransactionType
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.models.enums_estimate_state import EnumsEstimateState
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.models.enums_pricing_methodology import EnumsPricingMethodology
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.models.enums_severity import EnumsSeverity
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.models.enums_state import EnumsState
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.models.enums_true_up import EnumsTrueUp
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.models.rpc_status import RpcStatus
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.models.v1_batch_validate_enriched_capital_flows_request import V1BatchValidateEnrichedCapitalFlowsRequest
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.models.v1_batch_validate_enriched_capital_flows_response import V1BatchValidateEnrichedCapitalFlowsResponse
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.models.v1_enriched_capital_flow import V1EnrichedCapitalFlow
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.models.v1_enriched_capital_flow_query import V1EnrichedCapitalFlowQuery
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.models.v1_enriched_capital_flow_transfer_detail import V1EnrichedCapitalFlowTransferDetail
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.models.v1_enriched_capital_flow_transition import V1EnrichedCapitalFlowTransition
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.models.v1_enriched_capital_flow_validation import V1EnrichedCapitalFlowValidation
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.models.v1_enriched_capital_flows_by_historical_transactions_query import V1EnrichedCapitalFlowsByHistoricalTransactionsQuery
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.models.v1_enriched_capital_flows_response import V1EnrichedCapitalFlowsResponse
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.models.v1_external_enriched_capital_flow_identifier import V1ExternalEnrichedCapitalFlowIdentifier
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.models.v1_filter_enriched_capital_flows_by_historical_transactions_request import V1FilterEnrichedCapitalFlowsByHistoricalTransactionsRequest
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.models.v1_filter_enriched_capital_flows_by_historical_transactions_response import V1FilterEnrichedCapitalFlowsByHistoricalTransactionsResponse
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.models.v1_filter_enriched_capital_flows_request import V1FilterEnrichedCapitalFlowsRequest
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.models.v1_filter_enriched_capital_flows_response import V1FilterEnrichedCapitalFlowsResponse
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.models.v1_import_enriched_capital_flows_request import V1ImportEnrichedCapitalFlowsRequest
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.models.v1_import_enriched_capital_flows_response import V1ImportEnrichedCapitalFlowsResponse
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.models.v1_transition_enriched_capital_flow_request import V1TransitionEnrichedCapitalFlowRequest
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.models.v1_validate_enriched_capital_flow_response import V1ValidateEnrichedCapitalFlowResponse
