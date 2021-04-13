import json
import os
import unittest
from _pytest.monkeypatch import MonkeyPatch
from mock import patch
from utils.flex import stream_hello, stream_world

# MonkeyPatch().setattr('utils.flex.NAME', "Moon")

# def test_stream_hello_func():
#     result = stream_hello()
#     expected = 'Hi Moon'
#     assert result == expected
#     assert str == type(expected)

# @patch('utils.flex.Stream')
# def test_stream_world(mock_stream):
#     mock_stream.world.return_value = 'Hello LINE'
#     result = stream_world()
#     expected = 'Hello LINE'
#     mock_stream.world.assert_called_once()
#     assert result == expected
#     assert str == type(expected)

class TestClient(unittest.TestCase):
    def setUp(self):
        # mock global variable
        MonkeyPatch().setattr('utils.flex.NAME', "Moon")

    def test_stream_hello(self):
        result = stream_hello()
        expected = 'Hi Moon'
        self.assertEqual(result, expected)
        self.assertEqual(str, type(expected))

    @patch('utils.flex.Stream')
    def test_stream_world(self, mock_stream):
        mock_stream.world.return_value = 'Hello LINE'
        result = stream_world()
        expected = 'Hello LINE'
        mock_stream.world.assert_called_once()
        self.assertEqual(result, expected)
        self.assertEqual(str, type(expected))
    