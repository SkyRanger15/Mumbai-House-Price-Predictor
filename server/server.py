from flask import Flask, request, jsonify
import util 

app = Flask(__name__)


@app.route('/get_region_names', methods=['GET'])
def get_region_names():
    response = jsonify({
        'region': util.get_region_names() 
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_type_names', methods=['GET'])
def get_type_names():
    response = jsonify({
        'type': util.get_type_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_house_price',methods =['GET','POST'])
def predict_house_price():
    bhk = int(request.form['bhk'])
    type_ = request.form['type']
    area = float(request.form['area'])
    region = request.form['region']
    status = request.form['status']
    age = request.form['age']

    response = jsonify({
        'estimated_price' : util.predict_price(bhk, type_, area, region, status, age)
    })

    return response



if __name__ == '__main__':
    print("Starting Flask Server...")
    util.load_saved_artifacts()
    app.run()