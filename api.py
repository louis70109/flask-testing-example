import os

from flask import Flask
from flask_cors import CORS
from flask_restful import Api


if os.getenv('FLASK_ENV') != 'production':
    from dotenv import load_dotenv
    load_dotenv()

from controller.item_controller import ItemController

app = Flask(__name__)
CORS(app)

api = Api(app)

api.add_resource(ItemController, '/items')


@app.route("/health", methods=['GET'])
def health_check():
    return 'ok'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
