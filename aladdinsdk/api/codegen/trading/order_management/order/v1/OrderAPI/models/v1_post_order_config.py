# coding: utf-8

"""
    Order

    Filter, post or cancel orders. An order is a directive from a portfolio manager to the trading desk to execute a particular investment decision.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr

class V1PostOrderConfig(BaseModel):
    """
    V1PostOrderConfig
    """
    what_if: StrictBool = Field(..., alias="whatIf")
    run_compliance: Optional[StrictBool] = Field(None, alias="runCompliance", description="Default is true to run compliance on this post order request.")
    account_code: Optional[StrictStr] = Field(None, alias="accountCode", description="Aladdin's unique account code/ID for an organization or system (e.g. an external broker or counterparty). Also known as \"org_id\" to some legacy systems. Used for linking to the external portfolio details.")
    external_entity_type: Optional[StrictStr] = Field(None, alias="externalEntityType", description="External entity type like CUST - custodian, FUTR - futures agent. ADMN - administrator, etc., as per the EXTENT_TYPES decodes. Used for linking to the external portfolio details.")
    compliance_timeout: Optional[StrictStr] = Field(None, alias="complianceTimeout", description="Timeout for running compliance, specified in seconds (example format: \"10s\"). The timer is set on the compliance run during order posting. If the non-zero time is reached and the run is not complete, orders will be posted with the \"Compl Pending\" status set regardless of any violations that may have resulted if the run was successful. Default is infinite if not specified or if the value is 0s / negative.")
    __properties = ["whatIf", "runCompliance", "accountCode", "externalEntityType", "complianceTimeout"]

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
    def from_json(cls, json_str: str) -> V1PostOrderConfig:
        """Create an instance of V1PostOrderConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1PostOrderConfig:
        """Create an instance of V1PostOrderConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1PostOrderConfig.parse_obj(obj)

        _obj = V1PostOrderConfig.parse_obj({
            "what_if": obj.get("whatIf"),
            "run_compliance": obj.get("runCompliance"),
            "account_code": obj.get("accountCode"),
            "external_entity_type": obj.get("externalEntityType"),
            "compliance_timeout": obj.get("complianceTimeout")
        })
        return _obj
