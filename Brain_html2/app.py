# coding: utf-8

from src.GenerateHTML import projectsWriter
from flask import Flask, render_template
import os
import webbrowser

html = projectsWriter('templates/template.html', 'config.json')
html.create('templates/index.html')


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/phone', methods = ['POST'])
def run_phone():
    os.system("bash scripts/cellphone.sh") 
    return ('', 204)
    
@app.route('/helmet_area', methods = ['POST'])
def run_helmet():
    os.system("bash scripts/helmet_area.sh")
    return ('', 204)

    
@app.route('/emotion', methods=['POST'])
def run_emotion():
    os.system("bash scripts/emotion.sh")
    return('', 204)

@app.route('/car', methods = ['POST'])
def run_car():
    os.system("bash scripts/car.sh")
    return ('', 204)

@app.route('/objectMeasure', methods = ['POST'])
def run_objectMeasure():
    os.system("bash scripts/objectMeasure.sh")
    return ('', 204)

@app.route('/maskDetector', methods = ['POST'])
def run_maskDetector():
    os.system("bash scripts/maskDetection.sh")
    return ('', 204)
    
@app.route('/faceRecognition', methods = ['POST'])
def run_faceRecognition():
    os.system("bash scripts/faceRecognition.sh")
    return ('', 204)

@app.route('/brainTumorDetection', methods = ['POST'])
def run_brainTumorDetection():
    os.system("bash scripts/brainTumorDetection.sh")
    return ('', 204)

@app.route('/CustomerSegmentation', methods = ['POST'])
def run_CustomerSegmentation():
    webbrowser.open_new_tab("https://app.powerbi.com/view?r=eyJrIjoiOWNhZjNlOTAtNzA5Yi00Njg5LWExMWMtMjMzNGUzNzFlYzgwIiwidCI6IjU5ZDRmMjQ5LTA1MjAtNDZjZi1iNmIyLTg3M2Q1ZGE1NDNmZSJ9&pageName=ReportSection")
    return ('', 204)



if __name__=='__main__':
    app.run(debug=True)
