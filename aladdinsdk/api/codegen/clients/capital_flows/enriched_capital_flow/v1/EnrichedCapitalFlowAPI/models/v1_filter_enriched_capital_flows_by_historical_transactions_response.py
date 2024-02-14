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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.models.v1_enriched_capital_flow import V1EnrichedCapitalFlow

class V1FilterEnrichedCapitalFlowsByHistoricalTransactionsResponse(BaseModel):
    """
    V1FilterEnrichedCapitalFlowsByHistoricalTransactionsResponse
    """
    enriched_capital_flows: Optional[conlist(V1EnrichedCapitalFlow)] = Field(None, alias="enrichedCapitalFlows")
    next_page_token: Optional[StrictStr] = Field(None, alias="nextPageToken")
    __properties = ["enrichedCapitalFlows", "nextPageToken"]

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
    def from_json(cls, json_str: str) -> V1FilterEnrichedCapitalFlowsByHistoricalTransactionsResponse:
        """Create an instance of V1FilterEnrichedCapitalFlowsByHistoricalTransactionsResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in enriched_capital_flows (list)
        _items = []
        if self.enriched_capital_flows:
            for _item in self.enriched_capital_flows:
                if _item:
                    _items.append(_item.to_dict())
            _dict['enrichedCapitalFlows'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1FilterEnrichedCapitalFlowsByHistoricalTransactionsResponse:
        """Create an instance of V1FilterEnrichedCapitalFlowsByHistoricalTransactionsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1FilterEnrichedCapitalFlowsByHistoricalTransactionsResponse.parse_obj(obj)

        _obj = V1FilterEnrichedCapitalFlowsByHistoricalTransactionsResponse.parse_obj({
            "enriched_capital_flows": [V1EnrichedCapitalFlow.from_dict(_item) for _item in obj.get("enrichedCapitalFlows")] if obj.get("enrichedCapitalFlows") is not None else None,
            "next_page_token": obj.get("nextPageToken")
        })
        return _obj

