from flask import Flask
from flask_cors import CORS, cross_origin


# To initialize the app
app = Flask(__name__)
# To enable CORS support
CORS(app)

# To enable debugging
app.config["DEBUG"] = True

# app.run(host='0.0.0.0', port=5000, debug=True)