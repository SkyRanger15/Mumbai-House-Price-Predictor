import streamlit as st
import requests
import base64


def load_options():
    type_url = "http://127.0.0.1:5000/get_type_names"
    region_url = "http://127.0.0.1:5000/get_region_names"
    
    type_response = requests.get(type_url)
    region_response = requests.get(region_url)
    
    if type_response.status_code == 200 and region_response.status_code == 200:
        types = type_response.json()['type']
        regions = region_response.json()['region']
        return types, regions
    else:
        return [], []

types, regions = load_options()


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

image_base64 = encode_image("Mumbai.jpg")

st.markdown(f"""
<style>
.stApp {{
    background-image: url('data:image/jpeg;base64,{image_base64}');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}}


div[data-testid="stMarkdownContainer"] {{
    color: white;
    font-size: 2em;

}}

div.stButton > button:first-child {{
    background-color: #4CAF50; 
    color: white;
    font-size: 1.2em;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}}

div.stButton > button:first-child:hover {{
    background-color: #45a049; 
}}

</style>
""", unsafe_allow_html=True)


st.title("Mumbai House Price Predictor")

bhk = st.number_input("BHK", min_value=1, step=1)
type_ = st.selectbox("Type", options=types, format_func=lambda x: x.capitalize())
area = st.number_input("Area (in sqft)", min_value=400, step=50)
region = st.selectbox("Region", options=regions + ["Other"], format_func=lambda x: x.capitalize(), help="Input a region name. If not in the list, it will be considered as 'other'")
status = st.selectbox("Status", ["Under Construction", "Ready to move"])
age = st.selectbox("Age", ["Unknown", "Resale", "New"])

def get_prediction(bhk, type_, area, region, status, age):
    url = "http://127.0.0.1:5000/predict_house_price"
    data = {
        "bhk": bhk,
        "type": type_,
        "area": area,
        "region": region,
        "status": status,
        "age": age
    }
    response = requests.post(url, data=data)
    return response.json()

if st.button("Predict Price"):
    result = get_prediction(bhk, type_, area, region, status, age)
    st.markdown(f"<div style='color: white; font-size: 1.2em;'>Estimated Price: {result['estimated_price']} INR</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    st.write("Streamlit app is running...")
