from flask import Blueprint, request, jsonify
from middleware.auth import authenticate_token 

reminders_bp = Blueprint("reminders", __name__)

reminders = []

@reminders_bp.before_request 
def before_request():
    authenticate_token()

@reminders_bp.route("/", methods=["GET"])
def get_rems():
    return jsonify(reminders)

@reminders_bp.route("/", methods=["POST"])
def create_rem():
    rem = {
        "id": len(reminders) + 1,
        "title": request.json.get ("title"),
        "completed": request.json.get ("completed", False)
    }
    reminders.append(rem)
    return jsonify(rem), 201

@reminders_bp.route("/<int:id>", methods=["PUT"])
def update_rem(id):
    rem = next((r for r in reminders if r["id"] == id), None)
    if rem is None:
        return jsonify({"error": "Reminder not found"}), 404
    rem["title"] = request.json.get("title", rem["title"])
    rem["completed"] = request.json.get ("completed", rem["completed"])
    return jsonify(rem)

@reminders_bp.route("/<int:id>", methods=[ "DELETE"])
def delete_rem(id):
    global reminders
    reminders = [r for r in reminders if r["id"] != id]
    return ' ', 204

