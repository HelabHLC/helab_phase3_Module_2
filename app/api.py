from flask import Blueprint, jsonify, request

api_bp = Blueprint('api', __name__)

@api_bp.route("/match", methods=["POST"])
def match_color():
    # Dummy response
    return jsonify({"match": "Dummy color match result"})

@api_bp.route("/colors", methods=["GET"])
def get_colors():
    return jsonify(["Color1", "Color2"])

@api_bp.route("/lab-to-rgb", methods=["POST"])
def lab_to_rgb():
    return jsonify({"rgb": [255, 255, 255]})
