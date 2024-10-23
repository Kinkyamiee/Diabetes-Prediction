import os
import pickle
import streamlit as st

# Print the current working directory
print("Current working directory:", os.getcwd())

# Loading the trained model
pickle_in = open(r"C:\Users\hp\Documents\Diabetes Project\classifier.pkl", 'rb')
classifier = pickle.load(pickle_in)

# Defining the function to make predictions using the user input
@st.cache_data
def prediction(Gender, Age, Hypertension, Heart_disease, Smoking_history,
               BMI, HbA1c_level, Blood_glucose_level):
    
    # Convert categorical data
    gender_encoded = 1 if Gender == "Male" else 0
    smoking_mapping = {"Never": 0, "Former": 1, "Current": 2}
    smoking_encoded = smoking_mapping[Smoking_history]

    # Making Predictions (ensure that the order of input features matches your model training)
    prediction = classifier.predict([[gender_encoded, Age, Hypertension, Heart_disease, smoking_encoded,
                                      BMI, HbA1c_level, Blood_glucose_level]])

    if prediction == 0:
        pred = "Not Diabetes"
    else:
        pred = "Diabetes"

    return pred

# Main function to define the Streamlit web app
def main():
    # Front end elements of the web page
    html_temp = '''
    <div style='background-color: red; padding:13px'>
    <h1 style='color: black; text-align: center;'>Diabetes Prediction ML App</h1>
    </div>
    '''

    # Display the front end aspect
    st.markdown(html_temp, unsafe_allow_html=True)

    # Input Parameters
    st.header("Input Parameters")
    Age = st.number_input("Age", min_value=0, max_value=90, value=30)
    Gender = st.selectbox("Gender", ["Male", "Female"])
    Hypertension = st.selectbox("Hypertension", [0, 1], help="0: No, 1: Yes")
    Heart_disease = st.selectbox("Heart Disease", [0, 1], help="0: No, 1: Yes")
    Smoking_history = st.selectbox("Smoking History", ["Never", "Former", "Current"])
    BMI = st.number_input("BMI (Body Mass Index)", min_value=15.0, max_value=40.0, value=24.0)
    HbA1c_level = st.number_input("HbA1c Level", min_value=3.0, max_value=7.0, value=5.5)
    Blood_glucose_level = st.number_input("Blood Glucose Level", min_value=50, max_value=300, value=100)

    result = ""

    # When 'Predict' is clicked, make prediction and display the result
    if st.button("Predict"):
        result = prediction(Gender, Age, Hypertension, Heart_disease, Smoking_history,
                            BMI, HbA1c_level, Blood_glucose_level)
        st.success("Prediction: {}".format(result))

if __name__ == '__main__':
    main()
