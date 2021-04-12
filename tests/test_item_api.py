from unittest.mock import patch
from api import app
import unittest
import json


class TestItemController(unittest.TestCase):
    @patch('controller.item_controller.something')
    def test_item_api(self, mock_something):
        mock_something.return_value = 'Sally'
        client = app.test_client()
        response = client.post(
            '/items',
            data=json.dumps({
                'value': 100,
                'tax': 1.5
            }),
            content_type='application/json'
        )
        mock_something.assert_called_once()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'value': 150, 'name': 'Sally'})
