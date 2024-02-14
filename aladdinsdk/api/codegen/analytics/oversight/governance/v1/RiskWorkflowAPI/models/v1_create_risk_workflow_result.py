# coding: utf-8

"""
    Risk Governance - Workflows

    Retrieve, update, and transition Workflow items as surfaced in Risk Radar.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel
from aladdinsdk.api.codegen.analytics.oversight.governance.v1.RiskWorkflowAPI.models.rpc_status import RpcStatus
from aladdinsdk.api.codegen.analytics.oversight.governance.v1.RiskWorkflowAPI.models.v1_risk_workflow import V1RiskWorkflow

class V1CreateRiskWorkflowResult(BaseModel):
    """
    V1CreateRiskWorkflowResult
    """
    error: Optional[RpcStatus] = None
    output: Optional[V1RiskWorkflow] = None
    __properties = ["error", "output"]

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
    def from_json(cls, json_str: str) -> V1CreateRiskWorkflowResult:
        """Create an instance of V1CreateRiskWorkflowResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict['error'] = self.error.to_dict()
        # override the default output from pydantic by calling `to_dict()` of output
        if self.output:
            _dict['output'] = self.output.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1CreateRiskWorkflowResult:
        """Create an instance of V1CreateRiskWorkflowResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1CreateRiskWorkflowResult.parse_obj(obj)

        _obj = V1CreateRiskWorkflowResult.parse_obj({
            "error": RpcStatus.from_dict(obj.get("error")) if obj.get("error") is not None else None,
            "output": V1RiskWorkflow.from_dict(obj.get("output")) if obj.get("output") is not None else None
        })
        return _obj

