import streamlit as st

#Load EDA pkgs
import pandas as pd

#import ML Pkgs
import joblib
import os

#Load EDA Pkgs
import numpy as np

attrib_info = """
#### Attribute Information:
- lead time 0-443
- avg_price_per_room 0-375.5
- no_of_special_requests 0-5
- arrival_date 1-31
- arrival_month 1-12
- market segment_type ?
- no_of_week_nights 0-17
- no_of_weekend_nights 0-6
- no_of_adults 0-4
- arrival_year 2017-2018
"""

label_dict = {"Canceled":0,"Not_Canceled":1}
market_segment = {"Online":1,"Offline":2,"Corporate":3,"Complementary":4,"Aviation":5}
#adults = {"0":0,"1":1,"2":2,"3":3,"4":4}

def get_fvalue(val):
    feature_dict = {"Canceled":0,"Not_Canceled":1}
    for key,value in feature_dict.items():
       if val == key:
          return value
       
def get_value(val,my_dict):
    for key,value in my_dict.items():
       if val == key:
          return value
       

#def get_gvalue(val):
 #   feature_dic = {"0":0,"1":1,"2":2,"3":3,"4":4}
  #  for key,value in feature_dic.items():
   #    if val == key:
    #      return value      

#Load ML Models
@st.cache_data
def load_model(model_file):
 loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
 return loaded_model


def run_ml_app():
    st.subheader("From ML Section")
    #st.write("It is working")
    #st.success("It is sooo cool")

    with st.expander("Attribute Info"):
        st.markdown(attrib_info)

    #Layout
    col1,col2 = st.columns(2)

    with col1:
      avg_price_per_room = st.slider("avg_price_per_room",0,540)
      no_of_adults = st.slider("no_of_adults",0,4)
      lead_time = st.slider(" lead_time",0,443)
      no_of_special_requests = st.number_input("no_of_special_requests",0,5)

    with col2:
      arrival_date = st.number_input("arrival_date",1,31)
      arrival_month = st.number_input("arrival_month",1,12)
      market_segment_type = st.radio("market_segment_type",["Online","Offline","Corporate","Aviation","Complementary"])
      no_of_week_nights = st.slider("no_of_week_nights",0,17)
      no_of_weekend_nights = st.slider("no_of_weekend_nights",0,6)
      arrival_year = st.slider("arrival_year",2017,2018)
      #is_canceled = st.radio("is_canceled",["Canceled","Not_Canceled"])



    with st.expander("Your Selected Options"):
        result = {'lead_time':lead_time,
        'avg_price_per_room':avg_price_per_room,
        'no_of_special_requests': no_of_special_requests,
        'arrival_date':arrival_date,
        'arrival_month':arrival_month,
        'market_segment_type':market_segment_type, 
        'no_of_week_nights':no_of_week_nights,
        'no_of_weekend_nights':no_of_weekend_nights,
        'no_of_adults': no_of_adults,
        'arrival_year':arrival_year}

        
    st.write(result)


    encoded_result = []
    for i in result.values():
        if type(i) == int:
         encoded_result.append(i)
        elif i in ["Canceled","Not_Canceled"]:
         res = get_value(i,label_dict)
         encoded_result.append(res)
        elif i in ["Online","Offline","Corporate","Complementary","Aviation"]:
         res = get_value(i,market_segment)
         encoded_result.append(res)
        else:
         encoded_result.append(get_fvalue(i))

    st.write(encoded_result)


    with st.expander("Prediction Result"):
     single_sample = np.array(encoded_result).reshape(1,-1)
     st.write(single_sample)

    model = load_model("models/Random_Forest_model_hotel_reservations_1_07_2023.pkl")
    prediction = model.predict(single_sample)
    pred_prob = model.predict_proba(single_sample)
    st.write(prediction)
    st.write(pred_prob)

    if prediction == 1:
      st.success("Booking risk : Positive{}".format(prediction[1]))
      pred_probability_score = {"Booking risk : Positive":pred_prob[0][0]*100,
      "Booking risk : Positive":pred_prob[0][1]*100}
      st.write(pred_probability_score)
    else:
       st.warning("Booking risk : Negative{}".format(prediction[0]))
       pred_probability_score = {"Booking risk : Negative":pred_prob[0][0]*100,
      "Booking risk : Negative":pred_prob[0][1]*100}
       st.write(pred_probability_score)


