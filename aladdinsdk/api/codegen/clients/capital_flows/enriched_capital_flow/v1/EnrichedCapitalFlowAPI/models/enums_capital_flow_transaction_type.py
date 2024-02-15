# coding: utf-8

"""
    Capital Flows 1.0.0

    Capital flows are the cash and asset subscriptions coming into a fund and the cash and asset redemptions going out of a fund (e.g., client contributions, withdrawals, and initial funding for a portfolio). This API permits users to validate, create, update, and receive capital flows transactions and their details. User needs standard API permissison ALADDIN_API_USER to use the Capital Flows API and standard newcash permissions to perform different actions. Please refer to the Capital Flows User Guide on the client landing page for more information on newcash permission structure.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class EnumsCapitalFlowTransactionType(str, Enum):
    """
    Describes capital flow transaction type. (*Required).   - CAPITAL_FLOW_TRANSACTION_TYPE_UNSPECIFIED: Represents unspecified transaction type.  - CAPITAL_FLOW_TRANSACTION_TYPE_CASHIN: Represents CASHIN transaction type.  - CAPITAL_FLOW_TRANSACTION_TYPE_CASHOUT: Represents CASHOUT transaction type.  - CAPITAL_FLOW_TRANSACTION_TYPE_ASSETIN: Represents ASSETIN transaction type.  - CAPITAL_FLOW_TRANSACTION_TYPE_ASSETOUT: Represents ASSETOUT transaction type.  - CAPITAL_FLOW_TRANSACTION_TYPE_TRANSFERIN: Represents TRANSFERIN transaction type.  - CAPITAL_FLOW_TRANSACTION_TYPE_TRANSFEROUT: Represents TRANSFEROUT transaction type.  - CAPITAL_FLOW_TRANSACTION_TYPE_ASSETTRNFRIN: Represents ASSETTRNFRIN transaction type.  - CAPITAL_FLOW_TRANSACTION_TYPE_ASSETTRNFROUT: Represents ASSETTRNFROUT transaction type.
    """

    """
    allowed enum values
    """
    CAPITAL_FLOW_TRANSACTION_TYPE_UNSPECIFIED = 'CAPITAL_FLOW_TRANSACTION_TYPE_UNSPECIFIED'
    CAPITAL_FLOW_TRANSACTION_TYPE_CASHIN = 'CAPITAL_FLOW_TRANSACTION_TYPE_CASHIN'
    CAPITAL_FLOW_TRANSACTION_TYPE_CASHOUT = 'CAPITAL_FLOW_TRANSACTION_TYPE_CASHOUT'
    CAPITAL_FLOW_TRANSACTION_TYPE_ASSETIN = 'CAPITAL_FLOW_TRANSACTION_TYPE_ASSETIN'
    CAPITAL_FLOW_TRANSACTION_TYPE_ASSETOUT = 'CAPITAL_FLOW_TRANSACTION_TYPE_ASSETOUT'
    CAPITAL_FLOW_TRANSACTION_TYPE_TRANSFERIN = 'CAPITAL_FLOW_TRANSACTION_TYPE_TRANSFERIN'
    CAPITAL_FLOW_TRANSACTION_TYPE_TRANSFEROUT = 'CAPITAL_FLOW_TRANSACTION_TYPE_TRANSFEROUT'
    CAPITAL_FLOW_TRANSACTION_TYPE_ASSETTRNFRIN = 'CAPITAL_FLOW_TRANSACTION_TYPE_ASSETTRNFRIN'
    CAPITAL_FLOW_TRANSACTION_TYPE_ASSETTRNFROUT = 'CAPITAL_FLOW_TRANSACTION_TYPE_ASSETTRNFROUT'

    @classmethod
    def from_json(cls, json_str: str) -> EnumsCapitalFlowTransactionType:
        """Create an instance of EnumsCapitalFlowTransactionType from a JSON string"""
        return EnumsCapitalFlowTransactionType(json.loads(json_str))

