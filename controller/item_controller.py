from flask import request, jsonify
from flask_restful import Resource

from utils.flex import item_tax, something


class ItemController(Resource):

    def post(self):
        payload = request.get_json(force=True)
        # {'value': 100, 'tax': 1.5}
        total = item_tax(payload=payload)

        item_name = something()  # do something logic
        return jsonify({'value': total, 'name': item_name})
