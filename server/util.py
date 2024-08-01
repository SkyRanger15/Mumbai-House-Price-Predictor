import json
import pickle
import numpy as np

__type_ = None
__region = None
__data_columns = None
__model = None


def predict_price(bhk, type_, area, region, status, age):
    global __model
    global __data_columns

    status_map = {'Under Construction': 0, 'Ready to move': 1}
    status_encoded = status_map.get(status, -1)
    if status_encoded == -1:
        raise ValueError("Invalid status provided")
    
    age_map = {'Unknown': 0, 'Resale': 1, 'New': 2}
    age_encoded = age_map.get(age, -1)
    if age_encoded == -1:
        raise ValueError("Invalid age provided")
    

    type_ = type_.lower()
    region = region.lower()
    
    x = np.zeros(len(__data_columns))
    
    x[0] = bhk
    x[1] = area
    x[2] = status_encoded
    x[3] = age_encoded
    
    if type_ in __data_columns:
        type_index = __data_columns.index(type_)
        x[type_index] = 1
    else:
        raise ValueError(f"Invalid type provided: {type_}")
    
    try:
        region_index = __data_columns.index(region)
    except ValueError:
        region_index = -1
    
    if region_index >= 0:
        x[region_index] = 1
       
    return round(__model.predict([x])[0],2)


def load_saved_artifacts():
    print("loading saved artifacts....")
    global __data_columns
    global __region
    global __type_
    global __model

    with open("./artifacts/columns.json","r") as f:
        __data_columns = json.load(f)["data_columns"]
        __region = __data_columns[9:]
        __type_ = __data_columns[4:9]

    with open("./artifacts/Mumbai_Price_predictor.pickle","rb") as f:
        __model = pickle.load(f)
    print("Loading Artifacts Completed !!")


def get_region_names():
    return __region

def get_type_names():
    return __type_


if __name__ == "__main__":
    load_saved_artifacts()
    print(get_region_names())
    print(get_type_names())
    print(predict_price(2,'Apartment',650,'Agripada','Under Construction','Resale'))
    print(predict_price(2,'Apartment',1650,'Agripada','Ready to move','Resale'))
    print(predict_price(2,'Apartment',1650,'other','Ready to move','Resale'))