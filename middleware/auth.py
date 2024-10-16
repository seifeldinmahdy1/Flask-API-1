from flask import request, jsonify, Flask, abort

TOKEN = "seifseifseif"

def authenticate_token():
    token = request.headers.get("Authorization")
    if not token or token != f"Bearer {TOKEN}":
        abort(401, description="Unauthorized")
    
