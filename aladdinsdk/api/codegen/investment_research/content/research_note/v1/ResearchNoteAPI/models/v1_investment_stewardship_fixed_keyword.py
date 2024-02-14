# coding: utf-8

"""
    Research Note

    Create, modify, delete and retrieve research notes.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class V1InvestmentStewardshipFixedKeyword(str, Enum):
    """
    - INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_UNSPECIFIED: Unspecified  - INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_ACTIVIST: Activist  - INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_BOARD_MEMBER: Board Member  - INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_BOARD_SECRETARY: Board Secretary  - INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_BOARD_DIVERSITY: Board Diversity  - INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_CEO: CEO  - INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_CHAIRMAN: Chairman  - INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_CYBER_SECURITY: Cybersecurity  - INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_INVESTOR_RELATIONS: Investor Relations  - INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_M_AND_A: M&A  - INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_OPIOIDS: Opioids  - INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_POLITICAL_ACTIVITIES: Political Activities  - INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_PROXY_ACCESS: Proxy Access  - INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_PROXY_CONTEST: Proxy Contest  - INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_PURPOSE: Purpose  - INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_SPLIT_VOTE: Split Vote  - INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_SUCCESSION_PLANNING: Succession Planning  - INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_TCFD: TCFD  - INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_UNGC: UNGC
    """

    """
    allowed enum values
    """
    INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_UNSPECIFIED = 'INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_UNSPECIFIED'
    INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_ACTIVIST = 'INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_ACTIVIST'
    INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_BOARD_MEMBER = 'INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_BOARD_MEMBER'
    INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_BOARD_SECRETARY = 'INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_BOARD_SECRETARY'
    INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_BOARD_DIVERSITY = 'INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_BOARD_DIVERSITY'
    INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_CEO = 'INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_CEO'
    INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_CHAIRMAN = 'INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_CHAIRMAN'
    INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_CYBER_SECURITY = 'INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_CYBER_SECURITY'
    INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_INVESTOR_RELATIONS = 'INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_INVESTOR_RELATIONS'
    INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_M_AND_A = 'INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_M_AND_A'
    INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_OPIOIDS = 'INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_OPIOIDS'
    INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_POLITICAL_ACTIVITIES = 'INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_POLITICAL_ACTIVITIES'
    INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_PROXY_ACCESS = 'INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_PROXY_ACCESS'
    INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_PROXY_CONTEST = 'INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_PROXY_CONTEST'
    INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_PURPOSE = 'INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_PURPOSE'
    INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_SPLIT_VOTE = 'INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_SPLIT_VOTE'
    INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_SUCCESSION_PLANNING = 'INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_SUCCESSION_PLANNING'
    INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_TCFD = 'INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_TCFD'
    INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_UNGC = 'INVESTMENT_STEWARDSHIP_FIXED_KEYWORD_UNGC'

    @classmethod
    def from_json(cls, json_str: str) -> V1InvestmentStewardshipFixedKeyword:
        """Create an instance of V1InvestmentStewardshipFixedKeyword from a JSON string"""
        return V1InvestmentStewardshipFixedKeyword(json.loads(json_str))


