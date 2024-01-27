from unittest import TestCase, mock
import os
from test.resources.testutils import utils
from aladdinsdk.common.error.asdkerrors import AsdkTransformationException


class TestCommonDataTransformationOptions(TestCase):
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

    def test_conversion_option_valid(self):
        arr = self.test_subject.conversion_options(json_string_valid_normal)
        for p in arr:
            self.test_subject.convert(json_string_valid_normal, p)
        assert "batters.batter.[*]" in arr

        arr = self.test_subject.conversion_options(json_string_bigger)
        for p in arr:
            self.test_subject.convert(json_string_bigger, p)
        assert "[0].batters.batter.[*]" in arr

    def test_conversion_option_extreme(self):
        arr = self.test_subject.conversion_options("{}")
        for p in arr:
            self.test_subject.convert("{}", p)
        assert "[*]" in arr
        self.assertEqual(len(arr), 1, "The only available path for empty json object is [*]")

        arr = self.test_subject.conversion_options(json_string_depth_one)
        for p in arr:
            self.test_subject.convert(json_string_depth_one, p)
        assert "[*]" in arr
        self.assertEqual(len(arr), 1, "The only available path for plain json object is [*]")

        arr = self.test_subject.conversion_options("[]")
        for p in arr:
            self.test_subject.convert("[]", p)
        assert "[*]" in arr
        self.assertEqual(len(arr), 1, "The only available path for empty array is [*]")

        with self.assertRaises(AsdkTransformationException):
            arr = self.test_subject.conversion_options(None)
            for p in arr:
                self.test_subject.convert(None, p)


json_string_depth_one = """
{
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "ppu": 0.55
}"""

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
