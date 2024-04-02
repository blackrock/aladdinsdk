# coding: utf-8

"""
    Abor Lot

    This service can be used to get AborLot data.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Dict, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr
from aladdinsdk.api.codegen.accounting.transactions.abor_lot.v1.AborLotAPI.models.v1_abor_lot_setting import V1AborLotSetting

class V1AborLot(BaseModel):
    """
    AborLot describes the data of ABOR lots retrieved from the ledger_a_summary table.
    """
    id: Optional[StrictStr] = Field(None, description="describes the abor lot identifier.")
    portfolio_id: Optional[StrictStr] = Field(None, alias="portfolioId", description="describes the portfolio_id associated with the lots.")
    abor_lot_id: Optional[StrictStr] = Field(None, alias="aborLotId")
    obor_lot_id: Optional[StrictInt] = Field(None, alias="oborLotId")
    basis: Optional[StrictStr] = Field(None, description="describes the lot basis reflected from request.")
    asset_id: Optional[StrictStr] = Field(None, alias="assetId")
    lot_open_date_time: Optional[datetime] = Field(None, alias="lotOpenDateTime")
    lot_close_date_time: Optional[datetime] = Field(None, alias="lotCloseDateTime")
    entry_time: Optional[datetime] = Field(None, alias="entryTime")
    cancel_time: Optional[datetime] = Field(None, alias="cancelTime")
    open_time: Optional[datetime] = Field(None, alias="openTime")
    close_time: Optional[datetime] = Field(None, alias="closeTime")
    open_transaction_id: Optional[StrictStr] = Field(None, alias="openTransactionId")
    close_transaction_id: Optional[StrictStr] = Field(None, alias="closeTransactionId")
    parent_cusip: Optional[StrictStr] = Field(None, alias="parentCusip")
    lim_id: Optional[StrictInt] = Field(None, alias="limId")
    primary_basis: Optional[StrictStr] = Field(None, alias="primaryBasis")
    lot_settings_attributes_record_maps: Optional[Dict[str, V1AborLotSetting]] = Field(None, alias="lotSettingsAttributesRecordMaps")
    __properties = ["id", "portfolioId", "aborLotId", "oborLotId", "basis", "assetId", "lotOpenDateTime", "lotCloseDateTime", "entryTime", "cancelTime", "openTime", "closeTime", "openTransactionId", "closeTransactionId", "parentCusip", "limId", "primaryBasis", "lotSettingsAttributesRecordMaps"]

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
    def from_json(cls, json_str: str) -> V1AborLot:
        """Create an instance of V1AborLot from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in lot_settings_attributes_record_maps (dict)
        _field_dict = {}
        if self.lot_settings_attributes_record_maps:
            for _key in self.lot_settings_attributes_record_maps:
                if self.lot_settings_attributes_record_maps[_key]:
                    _field_dict[_key] = self.lot_settings_attributes_record_maps[_key].to_dict()
            _dict['lotSettingsAttributesRecordMaps'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1AborLot:
        """Create an instance of V1AborLot from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1AborLot.parse_obj(obj)

        _obj = V1AborLot.parse_obj({
            "id": obj.get("id"),
            "portfolio_id": obj.get("portfolioId"),
            "abor_lot_id": obj.get("aborLotId"),
            "obor_lot_id": obj.get("oborLotId"),
            "basis": obj.get("basis"),
            "asset_id": obj.get("assetId"),
            "lot_open_date_time": obj.get("lotOpenDateTime"),
            "lot_close_date_time": obj.get("lotCloseDateTime"),
            "entry_time": obj.get("entryTime"),
            "cancel_time": obj.get("cancelTime"),
            "open_time": obj.get("openTime"),
            "close_time": obj.get("closeTime"),
            "open_transaction_id": obj.get("openTransactionId"),
            "close_transaction_id": obj.get("closeTransactionId"),
            "parent_cusip": obj.get("parentCusip"),
            "lim_id": obj.get("limId"),
            "primary_basis": obj.get("primaryBasis"),
            "lot_settings_attributes_record_maps": dict(
                (_k, V1AborLotSetting.from_dict(_v))
                for _k, _v in obj.get("lotSettingsAttributesRecordMaps").items()
            )
            if obj.get("lotSettingsAttributesRecordMaps") is not None
            else None
        })
        return _obj
