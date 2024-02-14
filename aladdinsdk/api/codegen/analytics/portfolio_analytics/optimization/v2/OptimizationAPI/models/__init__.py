# coding: utf-8

# flake8: noqa
"""
    Portfolio Optimization 2.0

    Optimize portfolio positions to maximize expected returns and minimize risk and transaction costs.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


# import models into model package
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.additional_factor_source_attribute_factor_source import AdditionalFactorSourceAttributeFactorSource
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.additional_factor_source_breakdown_factor_source import AdditionalFactorSourceBreakdownFactorSource
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.additional_factor_source_stress_scenario_source import AdditionalFactorSourceStressScenarioSource
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.any import Any
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.asset_universe_holdings_unit import AssetUniverseHoldingsUnit
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.bound_bound_style import BoundBoundStyle
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.bound_bound_type import BoundBoundType
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.group_bound_bound import GroupBoundBound
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.optimization_api_create_long_running_optimization_case_group400_response import OptimizationAPICreateLongRunningOptimizationCaseGroup400Response
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.protobuf_null_value import ProtobufNullValue
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.risk_model_additional_factor_source import RiskModelAdditionalFactorSource
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.rpc_status import RpcStatus
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.soft_bound_objective_soft_bound_type import SoftBoundObjectiveSoftBoundType
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.tablev1_sparse_data_table import Tablev1SparseDataTable
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.tablev1_sparse_data_table_sparse_table_number_element import Tablev1SparseDataTableSparseTableNumberElement
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.tablev2_sparse_data_table import Tablev2SparseDataTable
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.tablev2_sparse_data_table_sparse_table_number_element import Tablev2SparseDataTableSparseTableNumberElement
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.tax_model_asset_wash_sale import TaxModelAssetWashSale
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.tax_model_tax_lot import TaxModelTaxLot
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.tax_model_tax_rate import TaxModelTaxRate
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.tax_model_taxable_optimization_type import TaxModelTaxableOptimizationType
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.tax_rate_tax_rate_type import TaxRateTaxRateType
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.transaction_cost_model_asset_transaction_cost_parameter import TransactionCostModelAssetTransactionCostParameter
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.tree_table_data_tree_table_column import TreeTableDataTreeTableColumn
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.tree_table_data_tree_table_data_node import TreeTableDataTreeTableDataNode
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.tree_table_data_tree_table_generic_data import TreeTableDataTreeTableGenericData
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.types_analytics_portfolio_holding import TypesAnalyticsPortfolioHolding
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.types_analytics_position_type import TypesAnalyticsPositionType
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.types_exposure_parameter import TypesExposureParameter
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.types_risk_model_parameter import TypesRiskModelParameter
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.types_risk_model_parameter_reference import TypesRiskModelParameterReference
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.types_tree_table_data import TypesTreeTableData
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.types_var_fi_eq import TypesVarFiEq
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.types_var_matrix_parameter import TypesVarMatrixParameter
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.types_var_matrix_type import TypesVarMatrixType
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v1_longrunning_operation import V1LongrunningOperation
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_allow_purchase_outside_universe import V2AllowPurchaseOutsideUniverse
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_allow_short_position import V2AllowShortPosition
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_alpha_model import V2AlphaModel
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_asset_universe import V2AssetUniverse
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_blk_ops_entry import V2BlkOpsEntry
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_bound_relaxation import V2BoundRelaxation
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_bound_unit import V2BoundUnit
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_composite import V2Composite
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_composite_universe import V2CompositeUniverse
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_create_long_running_optimization_case_group_request import V2CreateLongRunningOptimizationCaseGroupRequest
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_diversification_rule import V2DiversificationRule
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_group_bound import V2GroupBound
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_heuristic_model import V2HeuristicModel
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_optimization_case import V2OptimizationCase
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_optimization_case_adjustment import V2OptimizationCaseAdjustment
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_optimization_case_group import V2OptimizationCaseGroup
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_optimization_case_type import V2OptimizationCaseType
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_optimization_constraint import V2OptimizationConstraint
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_optimization_data_model import V2OptimizationDataModel
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_optimization_objective import V2OptimizationObjective
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_optimization_setting import V2OptimizationSetting
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_optimization_solution import V2OptimizationSolution
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_optimization_solution_type import V2OptimizationSolutionType
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_optimization_solutions import V2OptimizationSolutions
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_optimizer_control_parameter import V2OptimizerControlParameter
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_report_request_entry import V2ReportRequestEntry
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_risk_budgeting import V2RiskBudgeting
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_risk_model import V2RiskModel
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_single_bound import V2SingleBound
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_single_bound_hard import V2SingleBoundHard
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_single_bound_soft import V2SingleBoundSoft
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_single_per_asset_bound import V2SinglePerAssetBound
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_soft_bound_objective import V2SoftBoundObjective
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_tax_model import V2TaxModel
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_transaction_cost_model import V2TransactionCostModel
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_transaction_type import V2TransactionType
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_treat_assets_without_risk import V2TreatAssetsWithoutRisk
