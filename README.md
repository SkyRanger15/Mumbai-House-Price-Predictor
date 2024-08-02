# House Prices in Mumbai: End-to-End Machine Learning Project

## AIM
The aim of this mini project was to create an end-to-end machine learning pipeline to apply and test the concepts I have learned so far. The project includes data collection, preprocessing, model training, backend and frontend development, and deployment to an online platform.

<img width="1265" alt="image" src="https://github.com/user-attachments/assets/1af19f32-ebcc-41c3-b5b0-6f38ecc53d75">

You can test it yourself by clicking on this link : https://huggingface.co/spaces/Sky-Ranger/Mumbai-House-Price-Predictor

## Concepts and Workflow

### Days 1-2: Data Collection and Preprocessing

**Data Collection:**
- Collected a large dataset of current house prices in Mumbai. The dataset included various features such as the number of bedrooms (BHK), type of property, area, region, status, age of the property, and the price in INR. This also required my understanding of how property prices work in real life

**Data Cleaning:**
- Handled missing values by either imputing them with appropriate statistics or removing the rows/columns if necessary.
- Removed any duplicate records to ensure data integrity.

**Feature Engineering:**
- Created new features from existing ones to capture more information, such as the price per square foot.
- Normalized and scaled numerical features to standardize the range of data.

**Encoding:**
- Applied ordinal encoding to the `status` and `age` columns to convert categorical data into numerical format.
- Used one-hot encoding for the `region` and `type` column to handle categorical data with multiple levels.

**Model Training:**
- Split the dataset into training and testing sets to evaluate model performance.
- Trained several machine learning models including linear regression, decision trees,lasso,randomforest and gradient boosting.(Some were removed from the jupyter notebook, because the time to compute those took too long)
- Performed hyperparameter tuning using cross-validation to optimize model performance.

**Best Model Selection:**
- Selected the Random Forest Regressor as the best-performing model based on evaluation metrics like Mean Squared Error (MSE) and R-squared score.
- Created a pickle file of the trained Random Forest Regressor for deployment.

  *For detailed implementation, refer to `MLmodel.ipynb` in the `model` directory.*

### Day 3: Backend Development with Flask

**Setting Up Flask:**
- Created a Flask application to serve the machine learning model.
- Defined routes and endpoints for GET and POST methods to interact with the model.

**JSON Handling:**
- Ensured that all columns required for model prediction are included in the JSON input file.
- Created utility functions to parse the JSON input and convert it into a format suitable for the model.

**Model Integration:**
- Loaded the pickle file of the Random Forest Regressor in the Flask app.
- Implemented prediction logic to process incoming data and return predictions in JSON format.

  *For detailed implementation, refer to `server.py` in the `server` directory.*

### Day 4: Frontend Development with Streamlit

**Setting Up Streamlit:**
- Developed a Streamlit application for the frontend to create an interactive user interface.
- Designed the layout to include input fields for all necessary features such as BHK, property type, area, region, status, and age.

**Connecting Frontend to Backend:**
- Integrated the Streamlit frontend with the Flask backend using API calls.
- Set up mechanisms to send user input from Streamlit to Flask, and display predictions received from Flask in the Streamlit app.

**User Interface:**
- Made the interface user-friendly and intuitive to ensure a seamless experience for users.
- Added error handling and validation checks to manage incorrect or incomplete inputs.

*For detailed implementation, refer to `app.py` in the `client` directory.*

### Day 5: Deployment on Hugging Face

**Deploying on Hugging Face:**
- Chose Hugging Face Spaces as the deployment platform for its ease of use and integration capabilities.
- Packaged the Flask application and Streamlit frontend for deployment on Hugging Face.

**Deployment Steps:**
- Created a repository on Hugging Face and pushed the codebase, including the model pickle file, Flask backend, and Streamlit frontend.
- Configured the deployment settings to ensure proper execution of both the backend and frontend components.

**Testing and Optimization:**
- Tested the deployed application to ensure it works as expected and handles real-time data inputs efficiently.
- Made necessary optimizations to improve the application's performance and response time.

## Conclusion

This mini project involved a comprehensive process of collecting, preprocessing, and modeling data, followed by the development and deployment of an interactive application. The end result is an online tool that predicts house prices in Mumbai based on various input features, showcasing the practical application of machine learning concepts and end-to-end project deployment.

