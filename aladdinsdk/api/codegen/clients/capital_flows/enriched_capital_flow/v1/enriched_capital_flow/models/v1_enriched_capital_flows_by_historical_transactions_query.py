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

class V1EnrichedCapitalFlowsByHistoricalTransactionsQuery(BaseModel):
    """
    Query search parameters. This method returns: the latest version of the capital flows transaction record when no version is provided; the specified version of the capital flows transaction record when the version is provided; or all versions of the capital flows transaction record when '*' is provided as the version.
    """
    enriched_capital_flow_id: StrictStr = Field(..., alias="enrichedCapitalFlowId")
    enriched_capital_flow_version: Optional[StrictInt] = Field(None, alias="enrichedCapitalFlowVersion")
    __properties = ["enrichedCapitalFlowId", "enrichedCapitalFlowVersion"]

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
    def from_json(cls, json_str: str) -> V1EnrichedCapitalFlowsByHistoricalTransactionsQuery:
        """Create an instance of V1EnrichedCapitalFlowsByHistoricalTransactionsQuery from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1EnrichedCapitalFlowsByHistoricalTransactionsQuery:
        """Create an instance of V1EnrichedCapitalFlowsByHistoricalTransactionsQuery from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1EnrichedCapitalFlowsByHistoricalTransactionsQuery.parse_obj(obj)

        _obj = V1EnrichedCapitalFlowsByHistoricalTransactionsQuery.parse_obj({
            "enriched_capital_flow_id": obj.get("enrichedCapitalFlowId"),
            "enriched_capital_flow_version": obj.get("enrichedCapitalFlowVersion")
        })
        return _obj

