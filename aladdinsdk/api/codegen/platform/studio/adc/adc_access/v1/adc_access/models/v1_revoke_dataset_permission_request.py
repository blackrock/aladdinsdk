# coding: utf-8

"""
    Adc Access

    Manages User Access via Functional Roles and Access Roles in Aladdin Data Cloud (ADC). Used by Studio's ADC Admin Center.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field
from aladdinsdk.api.codegen.platform.studio.adc.adc_access.v1.adc_access.models.v1_adc_dataset_qualified_name import V1AdcDatasetQualifiedName
from aladdinsdk.api.codegen.platform.studio.adc.adc_access.v1.adc_access.models.v1_functional_role import V1FunctionalRole

class V1RevokeDatasetPermissionRequest(BaseModel):
    """
    The request message for AdcAccessAPI.RevokeDatasetPermission.
    """
    adc_dataset_qualified_name: Optional[V1AdcDatasetQualifiedName] = Field(None, alias="adcDatasetQualifiedName")
    functional_role: Optional[V1FunctionalRole] = Field(None, alias="functionalRole")
    __properties = ["adcDatasetQualifiedName", "functionalRole"]

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
    def from_json(cls, json_str: str) -> V1RevokeDatasetPermissionRequest:
        """Create an instance of V1RevokeDatasetPermissionRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of adc_dataset_qualified_name
        if self.adc_dataset_qualified_name:
            _dict['adcDatasetQualifiedName'] = self.adc_dataset_qualified_name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of functional_role
        if self.functional_role:
            _dict['functionalRole'] = self.functional_role.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1RevokeDatasetPermissionRequest:
        """Create an instance of V1RevokeDatasetPermissionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1RevokeDatasetPermissionRequest.parse_obj(obj)

        _obj = V1RevokeDatasetPermissionRequest.parse_obj({
            "adc_dataset_qualified_name": V1AdcDatasetQualifiedName.from_dict(obj.get("adcDatasetQualifiedName")) if obj.get("adcDatasetQualifiedName") is not None else None,
            "functional_role": V1FunctionalRole.from_dict(obj.get("functionalRole")) if obj.get("functionalRole") is not None else None
        })
        return _obj

