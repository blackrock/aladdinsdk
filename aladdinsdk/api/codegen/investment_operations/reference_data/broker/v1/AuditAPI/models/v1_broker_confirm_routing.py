# coding: utf-8

"""
    Broker Entities - Audit

    Operations to retrieve audit data for broker entities.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr

class V1BrokerConfirmRouting(BaseModel):
    """
    BrokerConfirmRouting describes instructions for delivering trade information to a broker desk. After a trade is booked in Aladdin, it needs to be confirmed with broker.  Confirm routings are setup at broker level in order for the confirmation deliveries to be created and sent out.
    """
    id: Optional[StrictStr] = Field(None, description="Resources must have a 'id' field. Name describes the computer or human assigned resource identifier. Routing id.")
    broker_id: Optional[StrictStr] = Field(None, alias="brokerId", description="Represents Aladdin Broker Identifier (Numeric), commonly referred to as broker code.")
    broker_desk_id: Optional[StrictStr] = Field(None, alias="brokerDeskId", description="Broker desk id.")
    delivery_purpose: Optional[StrictStr] = Field(None, alias="deliveryPurpose", description="Purpose of the confirmation delivery. Please see decode named DELIV_PURPOSE.")
    delivery_type: Optional[StrictStr] = Field(None, alias="deliveryType", description="The method of delivery. E.g. fax. Please see decode named BRKR_DELIV_T.")
    delivery_format: Optional[StrictStr] = Field(None, alias="deliveryFormat", description="Format of the delivery. Please see decode named BRKR_FORMATS.")
    recipient_contact_id: Optional[StrictStr] = Field(None, alias="recipientContactId", description="The contact id of the recipient.")
    auto_send: Optional[StrictBool] = Field(None, alias="autoSend", description="Send automatically true, do not send automatically false.")
    confirm_delivery_rule: Optional[StrictStr] = Field(None, alias="confirmDeliveryRule", description="JQL to evaluate whether to create delivery.")
    reviewer_sign_required: Optional[StrictBool] = Field(None, alias="reviewerSignRequired", description="Boolean flag that tells whether to add digital signature of reviewer to confirm sheet or not.")
    delivery_start_date: Optional[date] = Field(None, alias="deliveryStartDate", description="Date in which delivery becomes effective. NULL=no min effective date.")
    delivery_stop_date: Optional[date] = Field(None, alias="deliveryStopDate", description="Date in which delivery stops being effective. NULL=infinity date.")
    schedule_name: Optional[StrictStr] = Field(None, alias="scheduleName", description="Schedule to follow if auto send is true.")
    business_purpose: Optional[StrictStr] = Field(None, alias="businessPurpose", description="Purpose of delivery from business standpoint. This specifies the type of delivery like Confirm/Recon etc.")
    __properties = ["id", "brokerId", "brokerDeskId", "deliveryPurpose", "deliveryType", "deliveryFormat", "recipientContactId", "autoSend", "confirmDeliveryRule", "reviewerSignRequired", "deliveryStartDate", "deliveryStopDate", "scheduleName", "businessPurpose"]

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
    def from_json(cls, json_str: str) -> V1BrokerConfirmRouting:
        """Create an instance of V1BrokerConfirmRouting from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1BrokerConfirmRouting:
        """Create an instance of V1BrokerConfirmRouting from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1BrokerConfirmRouting.parse_obj(obj)

        _obj = V1BrokerConfirmRouting.parse_obj({
            "id": obj.get("id"),
            "broker_id": obj.get("brokerId"),
            "broker_desk_id": obj.get("brokerDeskId"),
            "delivery_purpose": obj.get("deliveryPurpose"),
            "delivery_type": obj.get("deliveryType"),
            "delivery_format": obj.get("deliveryFormat"),
            "recipient_contact_id": obj.get("recipientContactId"),
            "auto_send": obj.get("autoSend"),
            "confirm_delivery_rule": obj.get("confirmDeliveryRule"),
            "reviewer_sign_required": obj.get("reviewerSignRequired"),
            "delivery_start_date": obj.get("deliveryStartDate"),
            "delivery_stop_date": obj.get("deliveryStopDate"),
            "schedule_name": obj.get("scheduleName"),
            "business_purpose": obj.get("businessPurpose")
        })
        return _obj
