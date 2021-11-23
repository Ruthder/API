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
    dept = dept.lower()
    fixdept = dept
    if("bogotá" in dept):
        fixdept = "cundinamarca"
    elif("barranquilla" in dept):
        fixdept = "atlántico"
    elif("cartagena" in dept):
        fixdept = "bolívar"
    elif("santa marta" in dept):
        fixdept = "magdalena"
    elif("buenaventura" in dept):
        fixdept = "Valle del Cauca"
    response = {"original": dept.capitalize() , "fixedDepartment":fixdept.capitalize()}
    response = jsonify(response)
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response