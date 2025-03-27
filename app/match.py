from colormath.color_objects import LabColor
from colormath.color_diff import delta_e_cie2000
import json

with open("pigment_data.json", "r") as f:
    pigment_data = json.load(f)

def delta_e2000_check(lab):
    ref = [50.0, 0.0, 0.0]
    color1 = LabColor(*lab)
    color2 = LabColor(*ref)
    return delta_e_cie2000(color1, color2), ref

def match_lab_to_pigments(input_lab):
    input_color = LabColor(*input_lab)
    best = None
    best_delta = float("inf")
    for code, data in pigment_data.items():
        pigment_lab = LabColor(*data["lab"])
        delta = delta_e_cie2000(input_color, pigment_lab)
        if delta < best_delta:
            best = {"code": code, "name": data["name"], "lab": data["lab"], "delta": round(delta, 2)}
            best_delta = delta
    return best

def gamut_warning(lab):
    return any(abs(x) > 100 for x in lab[1:])
