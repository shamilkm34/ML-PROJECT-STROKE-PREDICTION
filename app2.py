import streamlit as st
import pickle
from PIL import Image

def main():
    st.title(":rainbow[STROKE PREDICTION]")
    image = Image.open('22.jpg')
    st.image(image,width=800)



    id = st.text_input(":red[id]")

    gender = st.text_input(":green[gender]")
    
    age = st.text_input(":orange[age]")
    
    hypertension = st.text_input(":blue[hypertension]")

    heart_disease  = st.text_input(":green[heart_disease]")
    
    ever_married = st.text_input(":violet[ever_married]")
    
    work_type  = st.text_input(":red[work_type ]")
    
    Residence_type = st.text_input(":blue[Residence_type]")

    avg_glucose_level = st.text_input(":blue[avg_glucose_level]")

    bmi = st.text_input(":blue[bmi]")

    smoking_status = st.text_input(":blue[smoking_status]")

    stroke = st.text_input(":blue[lmb]")







    features = [id,gender,age,hypertension,work_type,ever_married,heart_disease,Residence_type,avg_glucose_level,bmi,smoking_status,stroke]

    model = pickle.load(open('model11.sav','rb'))
    sc = pickle.load(open('sc11.sav','rb'))

    pred = st.button('PREDICT')

    if pred:
        prediction = model.predict(sc.transform([features]))


        if prediction == 1:
            st.write("THE PATIENT EFFECTED A SEVER STROKE")

        else:
            st.write("THE PATIENT IS FINE , NO WAY FOR AA STROKE ")
main()
