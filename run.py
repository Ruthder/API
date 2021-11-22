from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/department/<dept>", methods=["GET"])
def fixDepartment(dept):
    dept = dept.lower()
    fixdept = dept
    if("bogotá" in dept):
        fixdept = "Cundinamarca"
    elif("barranquilla" in dept):
        fixdept = "Atlántico"
    elif("cartagena" in dept):
        fixdept = "Bolívar"
    elif("santa marta" in dept):
        fixdept = "Magdalena"
    elif("buenaventura" in dept):
        fixdept = "Valle del Cauca"
    response = {"original": dept, "fixedDepartment":fixdept}
    response = jsonify(response)
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response