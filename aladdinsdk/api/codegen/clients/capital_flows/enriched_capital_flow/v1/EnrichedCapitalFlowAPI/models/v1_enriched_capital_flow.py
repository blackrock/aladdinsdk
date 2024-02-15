# coding: utf-8

"""
    Capital Flows 1.0.0

    Capital flows are the cash and asset subscriptions coming into a fund and the cash and asset redemptions going out of a fund (e.g., client contributions, withdrawals, and initial funding for a portfolio). This API permits users to validate, create, update, and receive capital flows transactions and their details. User needs standard API permissison ALADDIN_API_USER to use the Capital Flows API and standard newcash permissions to perform different actions. Please refer to the Capital Flows User Guide on the client landing page for more information on newcash permission structure.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date, datetime
from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, conlist
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.models.enums_capital_flow_basis import EnumsCapitalFlowBasis
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.models.enums_capital_flow_transaction_type import EnumsCapitalFlowTransactionType
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.models.enums_estimate_state import EnumsEstimateState
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.models.enums_pricing_methodology import EnumsPricingMethodology
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.models.enums_state import EnumsState
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.models.enums_true_up import EnumsTrueUp
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.models.v1_enriched_capital_flow_transfer_detail import V1EnrichedCapitalFlowTransferDetail
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.models.v1_external_enriched_capital_flow_identifier import V1ExternalEnrichedCapitalFlowIdentifier

class V1EnrichedCapitalFlow(BaseModel):
    """
    V1EnrichedCapitalFlow
    """
    id: Optional[StrictStr] = None
    cash_amount: Union[StrictFloat, StrictInt] = Field(..., alias="cashAmount", description="Cash amount in the specified currency. Incoming cash is positive, outgoing cash is negative (*Required).")
    enriched_capital_flow_transaction_type: EnumsCapitalFlowTransactionType = Field(..., alias="enrichedCapitalFlowTransactionType")
    cash_originator: StrictStr = Field(..., alias="cashOriginator")
    currency_code: StrictStr = Field(..., alias="currencyCode")
    create_time: Optional[datetime] = Field(None, alias="createTime")
    modifier: Optional[StrictStr] = None
    modify_time: Optional[datetime] = Field(None, alias="modifyTime")
    settlement_date: date = Field(..., alias="settlementDate")
    state: Optional[EnumsState] = None
    trade_date: date = Field(..., alias="tradeDate")
    authorizer_user_id: Optional[StrictStr] = Field(None, alias="authorizerUserId")
    authorizing_system: Optional[StrictStr] = Field(None, alias="authorizingSystem")
    authorize_time: Optional[datetime] = Field(None, alias="authorizeTime")
    creator: Optional[StrictStr] = None
    approver_user_id: Optional[StrictStr] = Field(None, alias="approverUserId")
    approving_system: Optional[StrictStr] = Field(None, alias="approvingSystem")
    confirm_time: Optional[datetime] = Field(None, alias="confirmTime")
    estimate_state: EnumsEstimateState = Field(..., alias="estimateState")
    fx_rate: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="fxRate")
    external_enriched_capital_flow_ids: Optional[conlist(V1ExternalEnrichedCapitalFlowIdentifier)] = Field(None, alias="externalEnrichedCapitalFlowIds")
    enriched_capital_flow_comment: Optional[StrictStr] = Field(None, alias="enrichedCapitalFlowComment")
    order_id: Optional[StrictStr] = Field(None, alias="orderId")
    order_type: Optional[StrictStr] = Field(None, alias="orderType")
    reason: Optional[StrictStr] = None
    system_owner: Optional[StrictStr] = Field(None, alias="systemOwner")
    touch_count: Optional[StrictInt] = Field(None, alias="touchCount")
    true_up: Optional[EnumsTrueUp] = Field(None, alias="trueUp")
    unit_owner_id: Optional[StrictStr] = Field(None, alias="unitOwnerId")
    unit_price: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="unitPrice")
    units_issue: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="unitsIssue")
    enriched_capital_flow_basis: Optional[EnumsCapitalFlowBasis] = Field(None, alias="enrichedCapitalFlowBasis")
    asset_id: Optional[StrictStr] = Field(None, alias="assetId")
    priced_entity: Optional[StrictStr] = Field(None, alias="pricedEntity")
    priced_time: Optional[datetime] = Field(None, alias="pricedTime")
    settlement_code: Optional[StrictInt] = Field(None, alias="settlementCode")
    pricing_methodology: Optional[EnumsPricingMethodology] = Field(None, alias="pricingMethodology")
    enriched_capital_flow_source: Optional[StrictStr] = Field(None, alias="enrichedCapitalFlowSource")
    settlement_info: Optional[StrictStr] = Field(None, alias="settlementInfo")
    client_payment_reference: Optional[StrictStr] = Field(None, alias="clientPaymentReference")
    cancel_requestor: Optional[StrictStr] = Field(None, alias="cancelRequestor")
    cancel_approver: Optional[StrictStr] = Field(None, alias="cancelApprover")
    send_eligible: Optional[StrictBool] = Field(None, alias="sendEligible")
    enriched_capital_flow_transfer_detail: Optional[V1EnrichedCapitalFlowTransferDetail] = Field(None, alias="enrichedCapitalFlowTransferDetail")
    portfolio_ticker: StrictStr = Field(..., alias="portfolioTicker")
    broker_ticker: Optional[StrictStr] = Field(None, alias="brokerTicker")
    portfolio_id: Optional[StrictStr] = Field(None, alias="portfolioId", description="Portfolio code.")
    broker_id: Optional[StrictStr] = Field(None, alias="brokerId", description="Counterparty code.")
    __properties = ["id", "cashAmount", "enrichedCapitalFlowTransactionType", "cashOriginator", "currencyCode", "createTime", "modifier", "modifyTime", "settlementDate", "state", "tradeDate", "authorizerUserId", "authorizingSystem", "authorizeTime", "creator", "approverUserId", "approvingSystem", "confirmTime", "estimateState", "fxRate", "externalEnrichedCapitalFlowIds", "enrichedCapitalFlowComment", "orderId", "orderType", "reason", "systemOwner", "touchCount", "trueUp", "unitOwnerId", "unitPrice", "unitsIssue", "enrichedCapitalFlowBasis", "assetId", "pricedEntity", "pricedTime", "settlementCode", "pricingMethodology", "enrichedCapitalFlowSource", "settlementInfo", "clientPaymentReference", "cancelRequestor", "cancelApprover", "sendEligible", "enrichedCapitalFlowTransferDetail", "portfolioTicker", "brokerTicker", "portfolioId", "brokerId"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> V1EnrichedCapitalFlow:
        """Create an instance of V1EnrichedCapitalFlow from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in external_enriched_capital_flow_ids (list)
        _items = []
        if self.external_enriched_capital_flow_ids:
            for _item in self.external_enriched_capital_flow_ids:
                if _item:
                    _items.append(_item.to_dict())
            _dict['externalEnrichedCapitalFlowIds'] = _items
        # override the default output from pydantic by calling `to_dict()` of enriched_capital_flow_transfer_detail
        if self.enriched_capital_flow_transfer_detail:
            _dict['enrichedCapitalFlowTransferDetail'] = self.enriched_capital_flow_transfer_detail.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1EnrichedCapitalFlow:
        """Create an instance of V1EnrichedCapitalFlow from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1EnrichedCapitalFlow.parse_obj(obj)

        _obj = V1EnrichedCapitalFlow.parse_obj({
            "id": obj.get("id"),
            "cash_amount": obj.get("cashAmount"),
            "enriched_capital_flow_transaction_type": obj.get("enrichedCapitalFlowTransactionType"),
            "cash_originator": obj.get("cashOriginator"),
            "currency_code": obj.get("currencyCode"),
            "create_time": obj.get("createTime"),
            "modifier": obj.get("modifier"),
            "modify_time": obj.get("modifyTime"),
            "settlement_date": obj.get("settlementDate"),
            "state": obj.get("state"),
            "trade_date": obj.get("tradeDate"),
            "authorizer_user_id": obj.get("authorizerUserId"),
            "authorizing_system": obj.get("authorizingSystem"),
            "authorize_time": obj.get("authorizeTime"),
            "creator": obj.get("creator"),
            "approver_user_id": obj.get("approverUserId"),
            "approving_system": obj.get("approvingSystem"),
            "confirm_time": obj.get("confirmTime"),
            "estimate_state": obj.get("estimateState"),
            "fx_rate": obj.get("fxRate"),
            "external_enriched_capital_flow_ids": [V1ExternalEnrichedCapitalFlowIdentifier.from_dict(_item) for _item in obj.get("externalEnrichedCapitalFlowIds")] if obj.get("externalEnrichedCapitalFlowIds") is not None else None,
            "enriched_capital_flow_comment": obj.get("enrichedCapitalFlowComment"),
            "order_id": obj.get("orderId"),
            "order_type": obj.get("orderType"),
            "reason": obj.get("reason"),
            "system_owner": obj.get("systemOwner"),
            "touch_count": obj.get("touchCount"),
            "true_up": obj.get("trueUp"),
            "unit_owner_id": obj.get("unitOwnerId"),
            "unit_price": obj.get("unitPrice"),
            "units_issue": obj.get("unitsIssue"),
            "enriched_capital_flow_basis": obj.get("enrichedCapitalFlowBasis"),
            "asset_id": obj.get("assetId"),
            "priced_entity": obj.get("pricedEntity"),
            "priced_time": obj.get("pricedTime"),
            "settlement_code": obj.get("settlementCode"),
            "pricing_methodology": obj.get("pricingMethodology"),
            "enriched_capital_flow_source": obj.get("enrichedCapitalFlowSource"),
            "settlement_info": obj.get("settlementInfo"),
            "client_payment_reference": obj.get("clientPaymentReference"),
            "cancel_requestor": obj.get("cancelRequestor"),
            "cancel_approver": obj.get("cancelApprover"),
            "send_eligible": obj.get("sendEligible"),
            "enriched_capital_flow_transfer_detail": V1EnrichedCapitalFlowTransferDetail.from_dict(obj.get("enrichedCapitalFlowTransferDetail")) if obj.get("enrichedCapitalFlowTransferDetail") is not None else None,
            "portfolio_ticker": obj.get("portfolioTicker"),
            "broker_ticker": obj.get("brokerTicker"),
            "portfolio_id": obj.get("portfolioId"),
            "broker_id": obj.get("brokerId")
        })
        return _obj
