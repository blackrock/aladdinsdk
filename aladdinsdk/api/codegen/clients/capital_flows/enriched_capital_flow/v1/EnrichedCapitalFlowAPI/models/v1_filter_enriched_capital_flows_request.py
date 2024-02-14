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


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr
from aladdinsdk.api.codegen.clients.capital_flows.enriched_capital_flow.v1.EnrichedCapitalFlowAPI.models.v1_enriched_capital_flow_query import V1EnrichedCapitalFlowQuery

class V1FilterEnrichedCapitalFlowsRequest(BaseModel):
    """
    V1FilterEnrichedCapitalFlowsRequest
    """
    page_size: Optional[StrictInt] = Field(None, alias="pageSize", description="The maximum number of capital flows transaction records to return. The service may return fewer than this value.")
    page_token: Optional[StrictStr] = Field(None, alias="pageToken", description="When paginating, all other parameters provided to 'FilterEnrichedCapitalFlows' must match the call that provided the page token. This field is not being used presently")
    enriched_capital_flow_query: Optional[V1EnrichedCapitalFlowQuery] = Field(None, alias="enrichedCapitalFlowQuery")
    __properties = ["pageSize", "pageToken", "enrichedCapitalFlowQuery"]

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
    def from_json(cls, json_str: str) -> V1FilterEnrichedCapitalFlowsRequest:
        """Create an instance of V1FilterEnrichedCapitalFlowsRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of enriched_capital_flow_query
        if self.enriched_capital_flow_query:
            _dict['enrichedCapitalFlowQuery'] = self.enriched_capital_flow_query.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1FilterEnrichedCapitalFlowsRequest:
        """Create an instance of V1FilterEnrichedCapitalFlowsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1FilterEnrichedCapitalFlowsRequest.parse_obj(obj)

        _obj = V1FilterEnrichedCapitalFlowsRequest.parse_obj({
            "page_size": obj.get("pageSize"),
            "page_token": obj.get("pageToken"),
            "enriched_capital_flow_query": V1EnrichedCapitalFlowQuery.from_dict(obj.get("enrichedCapitalFlowQuery")) if obj.get("enrichedCapitalFlowQuery") is not None else None
        })
        return _obj

