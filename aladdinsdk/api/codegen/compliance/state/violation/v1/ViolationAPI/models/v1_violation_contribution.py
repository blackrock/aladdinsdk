# coding: utf-8

"""
    Violation

    Retrieve and Create Compliance Violations  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from aladdinsdk.api.codegen.compliance.state.violation.v1.ViolationAPI.models.enums_compliance_position_source import EnumsCompliancePositionSource

class V1ViolationContribution(BaseModel):
    """
    Violation Contribution describes one or more allocations which contributed to the violation. Each violation is caused by one or more underlying positions.
    """
    asset_id: Optional[StrictStr] = Field(None, alias="assetId", description="Aladdin Security Identifier.")
    transaction_date: Optional[date] = Field(None, alias="transactionDate", description="The date on which the transaction took place.")
    allocation_quantity: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="allocationQuantity", description="Size of the allocation, dependent on the asset class of the security. e.g. in the case of equities, this will be the number of shares. Sign indicates the direction of the transaction.")
    portfolio_id: Optional[StrictStr] = Field(None, alias="portfolioId", description="Aladdin unique numeric portfolio id, e.g. -1123.")
    compliance_position_source: Optional[EnumsCompliancePositionSource] = Field(None, alias="compliancePositionSource")
    allocation_id: Optional[StrictInt] = Field(None, alias="allocationId", description="The id of the allocation.")
    __properties = ["assetId", "transactionDate", "allocationQuantity", "portfolioId", "compliancePositionSource", "allocationId"]

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
    def from_json(cls, json_str: str) -> V1ViolationContribution:
        """Create an instance of V1ViolationContribution from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1ViolationContribution:
        """Create an instance of V1ViolationContribution from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1ViolationContribution.parse_obj(obj)

        _obj = V1ViolationContribution.parse_obj({
            "asset_id": obj.get("assetId"),
            "transaction_date": obj.get("transactionDate"),
            "allocation_quantity": obj.get("allocationQuantity"),
            "portfolio_id": obj.get("portfolioId"),
            "compliance_position_source": obj.get("compliancePositionSource"),
            "allocation_id": obj.get("allocationId")
        })
        return _obj
