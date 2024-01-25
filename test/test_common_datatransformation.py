from unittest import TestCase, mock
import os
from test.resources.testutils import utils
import pandas as pd
import pandas.testing as pandastesting


class TestCommonDataTransformation(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_all_values_set.yaml",
            })
        self.env_patcher.start()
        utils.reload_modules()
        from aladdinsdk.common.datatransformation import json_to_pandas
        self.test_subject = json_to_pandas
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def setUp(self) -> None:
        return super().setUp()

    def test_conversion_valid(self):
        expected_df_1 = pd.DataFrame([])
        actual_df_1 = self.test_subject.convert("{}", "*")
        pandastesting.assert_frame_equal(actual_df_1, expected_df_1)

        expected_df_2 = pd.DataFrame(expected_df_data_2)
        actual_df_2 = self.test_subject.convert(json_string_valid_normal, "batters.batter.[*]")
        pandastesting.assert_frame_equal(actual_df_2, expected_df_2)

        expected_df_3 = pd.DataFrame(expected_df_data_3)
        actual_df_3 = self.test_subject.convert(json_string_valid_missing_key, "batters.batter.[*]")
        pandastesting.assert_frame_equal(actual_df_3, expected_df_3)

        expected_df_4 = pd.DataFrame(expected_df_data_4)
        actual_df_4 = self.test_subject.convert(json_string_bigger, "[*].batters.batter.[*].testleafarr.[*]")
        pandastesting.assert_frame_equal(actual_df_4, expected_df_4)

        expected_df_5 = pd.DataFrame(expected_df_data_5)
        actual_df_5 = self.test_subject.convert(json_string_bigger, "[*].batters.batter.[*].testleafarr")
        pandastesting.assert_frame_equal(actual_df_5, expected_df_5)

        expected_df_6 = pd.DataFrame(expected_df_data_6)
        actual_df_6 = self.test_subject.convert(json_string_bigger, "[*].batters.batter.[*]")
        pandastesting.assert_frame_equal(actual_df_6, expected_df_6)

    def test_conversion_malformed(self):
        self.assertRaises(Exception, self.test_subject.convert, "{invalidjson}", "*")
        self.assertRaises(Exception, self.test_subject.convert, "", "*")


expected_df_data_2 = [
    {'batters.batter.id': '1001', 'batters.batter.type': 'Regular', 'id': '0001', 'type': 'donut', 'name': 'Cake', 'ppu': 0.55},
    {'batters.batter.id': '1002', 'batters.batter.type': 'Chocolate', 'id': '0001', 'type': 'donut', 'name': 'Cake', 'ppu': 0.55},
    {'batters.batter.id': '1003', 'batters.batter.type': 'Blueberry', 'id': '0001', 'type': 'donut', 'name': 'Cake', 'ppu': 0.55},
    {'batters.batter.id': '1004', 'batters.batter.type': "Devil's Food", 'id': '0001', 'type': 'donut', 'name': 'Cake', 'ppu': 0.55}
    ]
expected_df_data_3 = [
    {'batters.batter.id': '1001', 'id': '0001', 'type': 'donut', 'name': 'Cake', 'ppu': 0.55, 'batters.batter.type': None},
    {'batters.batter.id': '1002', 'id': '0001', 'type': 'donut', 'name': 'Cake', 'ppu': 0.55, 'batters.batter.type': 'Chocolate'},
    {'batters.batter.id': None, 'id': '0001', 'type': 'donut', 'name': 'Cake', 'ppu': 0.55, 'batters.batter.type': 'Blueberry'},
    {'batters.batter.id': '1004', 'id': '0001', 'type': 'donut', 'name': 'Cake', 'ppu': 0.55, 'batters.batter.type': "Devil's Food"}
    ]
expected_df_data_4 = [{'batters.batter.testleafarr.[*]': 1, 'batters.batter.id': '1001', 'batters.batter.type': 'Regular',
                       'id': '0001', 'type': 'donut', 'name': 'Cake', 'ppu': 0.55},
                      {'batters.batter.testleafarr.[*]': 2, 'batters.batter.id': '1001', 'batters.batter.type': 'Regular',
                       'id': '0001', 'type': 'donut', 'name': 'Cake', 'ppu': 0.55},
                      {'batters.batter.testleafarr.[*]': 3, 'batters.batter.id': '1001', 'batters.batter.type': 'Regular',
                       'id': '0001', 'type': 'donut', 'name': 'Cake', 'ppu': 0.55},
                      {'batters.batter.testleafarr.[*]': 1, 'batters.batter.id': '1002', 'batters.batter.type': 'Chocolate',
                       'id': '0001', 'type': 'donut', 'name': 'Cake', 'ppu': 0.55},
                      {'batters.batter.testleafarr.[*]': 2, 'batters.batter.id': '1002', 'batters.batter.type': 'Chocolate',
                       'id': '0001', 'type': 'donut', 'name': 'Cake', 'ppu': 0.55},
                      {'batters.batter.testleafarr.[*]': 3, 'batters.batter.id': '1002', 'batters.batter.type': 'Chocolate',
                       'id': '0001', 'type': 'donut', 'name': 'Cake', 'ppu': 0.55},
                      {'batters.batter.testleafarr.[*]': 1, 'batters.batter.id': '1003', 'batters.batter.type': 'Blueberry',
                       'id': '0001', 'type': 'donut', 'name': 'Cake', 'ppu': 0.55},
                      {'batters.batter.testleafarr.[*]': 2, 'batters.batter.id': '1003', 'batters.batter.type': 'Blueberry',
                       'id': '0001', 'type': 'donut', 'name': 'Cake', 'ppu': 0.55},
                      {'batters.batter.testleafarr.[*]': 3, 'batters.batter.id': '1003', 'batters.batter.type': 'Blueberry',
                       'id': '0001', 'type': 'donut', 'name': 'Cake', 'ppu': 0.55},
                      {'batters.batter.testleafarr.[*]': 1, 'batters.batter.id': '1004', 'batters.batter.type': "Devil's Food",
                       'id': '0001', 'type': 'donut', 'name': 'Cake', 'ppu': 0.55},
                      {'batters.batter.testleafarr.[*]': 2, 'batters.batter.id': '1004', 'batters.batter.type': "Devil's Food",
                       'id': '0001', 'type': 'donut', 'name': 'Cake', 'ppu': 0.55},
                      {'batters.batter.testleafarr.[*]': 3, 'batters.batter.id': '1004', 'batters.batter.type': "Devil's Food",
                       'id': '0001', 'type': 'donut', 'name': 'Cake', 'ppu': 0.55},
                      {'batters.batter.testleafarr.[*]': 1, 'batters.batter.id': '1005', 'batters.batter.type': 'Vanilla',
                       'id': '0001', 'type': 'donut', 'name': 'Cake', 'ppu': 0.55},
                      {'batters.batter.testleafarr.[*]': 2, 'batters.batter.id': '1005', 'batters.batter.type': 'Vanilla',
                       'id': '0001', 'type': 'donut', 'name': 'Cake', 'ppu': 0.55},
                      {'batters.batter.testleafarr.[*]': 3, 'batters.batter.id': '1005', 'batters.batter.type': 'Vanilla',
                       'id': '0001', 'type': 'donut', 'name': 'Cake', 'ppu': 0.55},
                      {'batters.batter.testleafarr.[*]': 1, 'batters.batter.id': '2001', 'batters.batter.type': '2Regular',
                       'id': '0002', 'type': 'donut2', 'name': 'Cake2', 'ppu': 0.55},
                      {'batters.batter.testleafarr.[*]': 2, 'batters.batter.id': '2001', 'batters.batter.type': '2Regular',
                       'id': '0002', 'type': 'donut2', 'name': 'Cake2', 'ppu': 0.55},
                      {'batters.batter.testleafarr.[*]': 3, 'batters.batter.id': '2001', 'batters.batter.type': '2Regular',
                       'id': '0002', 'type': 'donut2', 'name': 'Cake2', 'ppu': 0.55},
                      {'batters.batter.testleafarr.[*]': 1, 'batters.batter.id': '2002', 'batters.batter.type': '2Chocolate',
                       'id': '0002', 'type': 'donut2', 'name': 'Cake2', 'ppu': 0.55},
                      {'batters.batter.testleafarr.[*]': 2, 'batters.batter.id': '2002', 'batters.batter.type': '2Chocolate',
                       'id': '0002', 'type': 'donut2', 'name': 'Cake2', 'ppu': 0.55},
                      {'batters.batter.testleafarr.[*]': 3, 'batters.batter.id': '2002', 'batters.batter.type': '2Chocolate',
                       'id': '0002', 'type': 'donut2', 'name': 'Cake2', 'ppu': 0.55},
                      {'batters.batter.testleafarr.[*]': 1, 'batters.batter.id': '2003', 'batters.batter.type': '2Blueberry',
                       'id': '0002', 'type': 'donut2', 'name': 'Cake2', 'ppu': 0.55},
                      {'batters.batter.testleafarr.[*]': 2, 'batters.batter.id': '2003', 'batters.batter.type': '2Blueberry',
                       'id': '0002', 'type': 'donut2', 'name': 'Cake2', 'ppu': 0.55},
                      {'batters.batter.testleafarr.[*]': 3, 'batters.batter.id': '2003', 'batters.batter.type': '2Blueberry',
                       'id': '0002', 'type': 'donut2', 'name': 'Cake2', 'ppu': 0.55},
                      {'batters.batter.testleafarr.[*]': 1, 'batters.batter.id': '2004', 'batters.batter.type': "2Devil's Food",
                       'id': '0002', 'type': 'donut2', 'name': 'Cake2', 'ppu': 0.55},
                      {'batters.batter.testleafarr.[*]': 2, 'batters.batter.id': '2004', 'batters.batter.type': "2Devil's Food",
                       'id': '0002', 'type': 'donut2', 'name': 'Cake2', 'ppu': 0.55},
                      {'batters.batter.testleafarr.[*]': 3, 'batters.batter.id': '2004', 'batters.batter.type': "2Devil's Food",
                       'id': '0002', 'type': 'donut2', 'name': 'Cake2', 'ppu': 0.55}]
expected_df_data_5 = [{'batters.batter.testleafarr.testleafarr_0': 1, 'batters.batter.testleafarr.testleafarr_1': 2,
                      'batters.batter.testleafarr.testleafarr_2': 3, 'batters.batter.id': '1001', 'batters.batter.type': 'Regular',
                       'id': '0001', 'type': 'donut', 'name': 'Cake', 'ppu': 0.55},
                      {'batters.batter.testleafarr.testleafarr_0': 1, 'batters.batter.testleafarr.testleafarr_1': 2,
                      'batters.batter.testleafarr.testleafarr_2': 3, 'batters.batter.id': '1002', 'batters.batter.type': 'Chocolate',
                       'id': '0001', 'type': 'donut', 'name': 'Cake', 'ppu': 0.55},
                      {'batters.batter.testleafarr.testleafarr_0': 1, 'batters.batter.testleafarr.testleafarr_1': 2,
                      'batters.batter.testleafarr.testleafarr_2': 3, 'batters.batter.id': '1003', 'batters.batter.type': 'Blueberry',
                       'id': '0001', 'type': 'donut', 'name': 'Cake', 'ppu': 0.55},
                      {'batters.batter.testleafarr.testleafarr_0': 1, 'batters.batter.testleafarr.testleafarr_1': 2,
                      'batters.batter.testleafarr.testleafarr_2': 3, 'batters.batter.id': '1004', 'batters.batter.type': "Devil's Food",
                       'id': '0001', 'type': 'donut', 'name': 'Cake', 'ppu': 0.55},
                      {'batters.batter.testleafarr.testleafarr_0': 1, 'batters.batter.testleafarr.testleafarr_1': 2,
                      'batters.batter.testleafarr.testleafarr_2': 3, 'batters.batter.id': '1005', 'batters.batter.type': 'Vanilla',
                       'id': '0001', 'type': 'donut', 'name': 'Cake', 'ppu': 0.55},
                      {'batters.batter.testleafarr.testleafarr_0': 1, 'batters.batter.testleafarr.testleafarr_1': 2,
                      'batters.batter.testleafarr.testleafarr_2': 3, 'batters.batter.id': '2001', 'batters.batter.type': '2Regular',
                       'id': '0002', 'type': 'donut2', 'name': 'Cake2', 'ppu': 0.55},
                      {'batters.batter.testleafarr.testleafarr_0': 1, 'batters.batter.testleafarr.testleafarr_1': 2,
                      'batters.batter.testleafarr.testleafarr_2': 3, 'batters.batter.id': '2002', 'batters.batter.type': '2Chocolate',
                       'id': '0002', 'type': 'donut2', 'name': 'Cake2', 'ppu': 0.55},
                      {'batters.batter.testleafarr.testleafarr_0': 1, 'batters.batter.testleafarr.testleafarr_1': 2,
                      'batters.batter.testleafarr.testleafarr_2': 3, 'batters.batter.id': '2003', 'batters.batter.type': '2Blueberry',
                       'id': '0002', 'type': 'donut2', 'name': 'Cake2', 'ppu': 0.55},
                      {'batters.batter.testleafarr.testleafarr_0': 1, 'batters.batter.testleafarr.testleafarr_1': 2,
                      'batters.batter.testleafarr.testleafarr_2': 3, 'batters.batter.id': '2004', 'batters.batter.type': "2Devil's Food",
                       'id': '0002', 'type': 'donut2', 'name': 'Cake2', 'ppu': 0.55}]
expected_df_data_6 = [
    {'batters.batter.id': '1001', 'batters.batter.type': 'Regular', 'batters.batter.testleafarr': [1, 2, 3],
     'id': '0001', 'type': 'donut', 'name': 'Cake', 'ppu': 0.55},
    {'batters.batter.id': '1002', 'batters.batter.type': 'Chocolate', 'batters.batter.testleafarr': [1, 2, 3],
     'id': '0001', 'type': 'donut', 'name': 'Cake', 'ppu': 0.55},
    {'batters.batter.id': '1003', 'batters.batter.type': 'Blueberry', 'batters.batter.testleafarr': [1, 2, 3],
     'id': '0001', 'type': 'donut', 'name': 'Cake', 'ppu': 0.55},
    {'batters.batter.id': '1004', 'batters.batter.type': "Devil's Food", 'batters.batter.testleafarr': [1, 2, 3],
     'id': '0001', 'type': 'donut', 'name': 'Cake', 'ppu': 0.55},
    {'batters.batter.id': '1005', 'batters.batter.type': 'Vanilla', 'batters.batter.testleafarr': [1, 2, 3],
     'id': '0001', 'type': 'donut', 'name': 'Cake', 'ppu': 0.55},
    {'batters.batter.id': '2001', 'batters.batter.type': '2Regular', 'batters.batter.testleafarr': [1, 2, 3],
     'id': '0002', 'type': 'donut2', 'name': 'Cake2', 'ppu': 0.55},
    {'batters.batter.id': '2002', 'batters.batter.type': '2Chocolate', 'batters.batter.testleafarr': [1, 2, 3],
     'id': '0002', 'type': 'donut2', 'name': 'Cake2', 'ppu': 0.55},
    {'batters.batter.id': '2003', 'batters.batter.type': '2Blueberry', 'batters.batter.testleafarr': [1, 2, 3],
     'id': '0002', 'type': 'donut2', 'name': 'Cake2', 'ppu': 0.55},
    {'batters.batter.id': '2004', 'batters.batter.type': "2Devil's Food", 'batters.batter.testleafarr': [1, 2, 3],
     'id': '0002', 'type': 'donut2', 'name': 'Cake2', 'ppu': 0.55}]


json_string_valid_normal = """
{
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "ppu": 0.55,
    "batters": {
        "batter": [
            { "id": "1001", "type": "Regular" },
            { "id": "1002", "type": "Chocolate" },
            { "id": "1003", "type": "Blueberry" },
            { "id": "1004", "type": "Devil's Food" }
        ]
    },
    "topping": [
        { "id": "5001", "type": "None" },
        { "id": "5002", "type": "Glazed" },
        { "id": "5005", "type": "Sugar" },
        { "id": "5007", "type": "Powdered Sugar" },
        { "id": "5006", "type": "Chocolate with Sprinkles" },
        { "id": "5003", "type": "Chocolate" },
        { "id": "5004", "type": "Maple" }
    ]
}
"""


json_string_valid_missing_key = """
{
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "ppu": 0.55,
    "batters": {
        "batter": [
            { "id": "1001"},
            { "id": "1002", "type": "Chocolate" },
            { "type": "Blueberry" },
            { "id": "1004", "type": "Devil's Food" }
        ]
    },
    "topping": [
        { "id": "5001", "type": "None" },
        { "id": "5002", "type": "Glazed" },
        { "id": "5005", "type": "Sugar" },
        { "id": "5007", "type": "Powdered Sugar" },
        { "id": "5006", "type": "Chocolate with Sprinkles" },
        { "id": "5003", "type": "Chocolate" },
        { "id": "5004", "type": "Maple" }
    ]
}
"""


json_string_bigger = """
[
  {
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "ppu": 0.55,
    "batters": {
      "batter": [
        {
          "id": "1001",
          "type": "Regular",
          "testleafarr": [
            1,
            2,
            3
          ]
        },
        {
          "id": "1002",
          "type": "Chocolate",
          "testleafarr": [
            1,
            2,
            3
          ]
        },
        {
          "id": "1003",
          "type": "Blueberry",
          "testleafarr": [
            1,
            2,
            3
          ]
        },
        {
          "id": "1004",
          "type": "Devil's Food",
          "testleafarr": [
            1,
            2,
            3
          ]
        },
        {
          "id": "1005",
          "type": "Vanilla",
          "testleafarr": [
            1,
            2,
            3
          ]
        }
      ]
    },
    "topping": [
      {
        "id": "5001",
        "type": "None"
      },
      {
        "id": "5002",
        "type": "Glazed"
      },
      {
        "id": "5005",
        "type": "Sugar"
      },
      {
        "id": "5007",
        "type": "Powdered Sugar"
      },
      {
        "id": "5006",
        "type": "Chocolate with Sprinkles"
      },
      {
        "id": "5003",
        "type": "Chocolate"
      },
      {
        "id": "5004",
        "type": "Maple"
      }
    ]
  },
  {
    "id": "0002",
    "type": "donut2",
    "name": "Cake2",
    "ppu": 0.55,
    "batters": {
      "batter": [
        {
          "id": "2001",
          "type": "2Regular",
          "testleafarr": [
            1,
            2,
            3
          ]
        },
        {
          "id": "2002",
          "type": "2Chocolate",
          "testleafarr": [
            1,
            2,
            3
          ]
        },
        {
          "id": "2003",
          "type": "2Blueberry",
          "testleafarr": [
            1,
            2,
            3
          ]
        },
        {
          "id": "2004",
          "type": "2Devil's Food",
          "testleafarr": [
            1,
            2,
            3
          ]
        }
      ]
    },
    "topping": [
      {
        "id": "5001",
        "type": "None"
      },
      {
        "id": "5002",
        "type": "Glazed"
      },
      {
        "id": "5005",
        "type": "Sugar"
      },
      {
        "id": "5007",
        "type": "Powdered Sugar"
      },
      {
        "id": "5006",
        "type": "Chocolate with Sprinkles"
      },
      {
        "id": "5003",
        "type": "Chocolate"
      },
      {
        "id": "5004",
        "type": "Maple"
      }
    ]
  }
]
"""
