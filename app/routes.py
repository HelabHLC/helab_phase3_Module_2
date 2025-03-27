from flask import render_template, request, send_file
import io, csv, json
from app.matching import match_lab_to_pigments

def register_routes(app):
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/tools/match", methods=["GET", "POST"])
    def match():
        result = None
        if request.method == "POST":
            L = float(request.form["L"])
            a = float(request.form["a"])
            b = float(request.form["b"])
            result = match_lab_to_pigments([L, a, b])
        return render_template("match.html", result=result)

    @app.route("/tools/match/export", methods=["POST"])
    def export():
        format = request.form["format"]
        result = {
            "input": [50, 0, 0],
            "delta": 2.4,
            "pigment": "Ultramarine Blue"
        }
        if format == "csv":
            output = io.StringIO()
            writer = csv.writer(output)
            writer.writerow(["L", "a", "b", "ΔE", "Pigment"])
            writer.writerow([50, 0, 0, result["delta"], result["pigment"]])
            output.seek(0)
            return send_file(io.BytesIO(output.read().encode()), mimetype="text/csv", as_attachment=True, download_name="match_result.csv")
        elif format == "json":
            return send_file(io.BytesIO(json.dumps(result).encode()), mimetype="application/json", as_attachment=True, download_name="match_result.json")
        return "Unsupported format", 400
