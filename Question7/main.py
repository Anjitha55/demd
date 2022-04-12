from flask import Flask, request
import streamlit as st
import pickle
from sklearn.linear_model import LogisticRegression

pickled_model_file = open("pickle_wine_model.pkl","rb")
classifier = pickle.load(pickled_model_file)


def hello():

    try :
        st.title("Streamlit")
        alcohol = st.text_input("alcohol")
        malicacid = st.text_input("malicacid")
        ash = st.text_input("ash")
        alcalinity_ash = st.text_input("alcalinity_ash")
        magnesium = st.text_input("magnesium")
        total_phenols = st.text_input("total_phenols")
        flavanoids = st.text_input("flavanoids")
        nonflavoured_phenols = st.text_input("nonflavoured_phenols")
        proanthocyanis = st.text_input("proanthocyanis")
        color_intensity = st.text_input("color_intensity")
        hue = st.text_input("hue")
        diluted_wine = st.text_input("diluted_wine")
        proline = st.text_input("proline")
        #return "Oops something went wrong", 400
        result = classifier.predict([[alcohol,malicacid,ash,alcalinity_ash,magnesium,total_phenols,flavanoids,nonflavoured_phenols,proanthocyanis,color_intensity,hue,diluted_wine,proline]])
        #result =  f"The values are {alcohol},{malicacid},{ash},{alcalinity_ash},{magnesium},{total_phenols},{flavanoids},{nonflavoured_phenols},{proanthocyanis},{color_intensity},{hue},{diluted_wine},{proline}"
        if st.button("Print output"):
            st.success(result)
    except Exception as e :
        return f" Error occuredd with message : {e}"

if __name__=="__main__":
    hello()
