import streamlit as st

#Load EDA pkgs
import pandas as pd

#Data Viz pkg
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns 
import plotly.express as px  
from PIL import Image



#content
c2 = Image.open('data/radd.png')
c3 = Image.open('data/2017.png')
c4 = Image.open('data/2018.png')
c5 = Image.open('data/2017 segment.png')
c6 = Image.open('data/2018 segment.png')
c7 = Image.open('data/top market segments.png')
c8 = Image.open('data/how much guests pay.png')
c9 = Image.open('data/how price varies.png')
c10 = Image.open('data/busiest months.png')
c11= Image.open('data/how long people stay.png')
c12= Image.open('data/corr plot.png')


#Load Data
@st.cache_data
def load_data(data):
    df = pd.read_csv(data)
    return df 

def run_eda_app():
    st.subheader("From Exploratory Data Analysis")
    #df = pd.read_csv("data/Hotel_reservations.csv")
    df = load_data("metadata_app_final/Hotel_reservations.csv")
    df = df.rename(columns={'booking_status': 'is_canceled'})
    #df['is_canceled'].replace('Canceled', '1',inplace=True)
    #df['is_canceled'].replace('Not_Canceled', '0',inplace=True)
    #df['is_canceled'] = df['is_canceled'].astype(int)
    #df['is_canceled'] = df['is_canceled'].astype(int)



    submenu = st.sidebar.selectbox("Submenu",["Descriptive","Plots"])
    if submenu == "Descriptive":

     with st.expander("Data"):
          st.dataframe(df)
       
     with st.expander("Data Types"):
          st.dataframe(df.dtypes)

     with st.expander("Descriptive Summary"):
          st.dataframe(df.describe())
               
  
          st.markdown(desc_temp_eda,unsafe_allow_html=True)

          st.image(c2,use_column_width=True)
    
    elif submenu == "Plots":
     #layoutd
     col1,col2 = st.columns([2,2]) 
     with col1:
        #2017 distribution
      with st.expander("Correlation Plot"):
          st.image(c12,use_column_width=True)
      with st.expander("2017 Distribution of Bookings"):
           st.image(c3,use_column_width=True)
        #For Distribution by sectors
     with st.expander("2017 Dist Plot by Sectors"):
          st.image(c5,use_column_width=True)
     with st.expander("2018 Dist Plot by Sectors"):
          st.image(c6,use_column_width=True)
     with st.expander("Top Market Segments"):
          st.image(c7,use_column_width=True)
     with st.expander("How does price vary?"):
          st.image(c9,use_column_width=True)
     with st.expander("How long do people stay?"):
          st.image(c11,use_column_width=True)


     with col2:
         #2018 distribution
      with st.expander("2018 Distribution of Bookings"):
           st.image(c4,use_column_width=True)
     
     with st.expander("How much do guests pay?"):
          st.image(c8,use_column_width=True)
     with st.expander("Which months are busiest?"):
          st.image(c10,use_column_width=True)

        #with st.beta_expander("Data Types")
         #   st.dataframe(df.dtypes)
    pass

    # Content
   
desc_temp_eda = """  
    <br> <br>
### The rise of hotel Reservation Cancellations ###
The rise of reservation channels has revolutionized
the way customers book their stays,resulting in a shift 
in their behavior. Unfortunately, this has also led to a
surge in the number of cancellations 
no-shows, posing a significant challenge
for hotels like Radisson. Customers cancel for a variety of reasons, 
including changes in plans and scheduling conflicts, often taking
advantage of free or low-cost cancellation policies. While this benefits guests, 
it can be a revenue-diminishing factor for hotels. Therefore, 
it is crucial for hotels to be able to predict whether a customer 
will cancel their reservation or not, in order to optimize their revenue and minimize losses.
"""



