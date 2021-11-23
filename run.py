from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/")
def hello_world():
    return "API - Corregir departamentos"

@app.route("/department/<dept>", methods=["GET"])
def fixDepartment(dept):
    original = dept
    fixdept = dept
    if("bogotá" in dept.lower()):
        fixdept = "Cundinamarca"
    elif("barranquilla" in dept.lower()):
        fixdept = "Atlántico"
    elif("cartagena" in dept).lower():
        fixdept = "Bolívar"
    elif("santa marta" in dept.lower()):
        fixdept = "Magdalena"
    elif("buenaventura" in dept.lower()):
        fixdept = "Valle del Cauca"
    response = {"original": original , "fixedDepartment":fixdept.capit}
    response = jsonify(response)
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response