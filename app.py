from flask import request, jsonify, Flask
from routes.reminders import reminders_bp

app = Flask(__name__)


app.register_blueprint(reminders_bp, url_prefix='/reminders')


@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found"}), 404


if __name__ == "__main__":
    app.run(port=3000)