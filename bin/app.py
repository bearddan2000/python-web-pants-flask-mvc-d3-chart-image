from flask import Flask, render_template, jsonify
import pandas as pd
import data

# Create Flask's `app` object
app = Flask(
    __name__,
    instance_relative_config=False,
    template_folder="templates"
)

def data_creation(data, value):
    for index, item in value.items():
        data_instance = {}
        data_instance['category'] = index
        data_instance['value'] = item
        data_instance['group'] = None
        data.append(data_instance)

@app.route('/', methods=['GET'])
def getIndex():
    return render_template("index.html")

@app.route('/getData')
def getData():
    p = data.main()
    piechart_data= []
    data_creation(piechart_data, p)
    response = jsonify(piechart_data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)
