# Confit
import streamlit as st
import os
import sklearn
st.set_page_config(page_title='Hotel Reservations Prediction Tool', page_icon=':bar_chart:', layout='wide')

#Core Pkgs
import streamlit.components.v1 as stc


from PIL import Image

#import our mini apps
from eda_app import run_eda_app
from ml_app import run_ml_app




# Title
st.title('Hotel Reservations Prediction Tool')

# Content
path1 = os.path.dirname('data/hotel_logos.png')
c1 = path1+'/hotel_logos.png'
desc_temp = """
            ### Hotel Reservations Cancellations
            This dataset contains some factors that influence the rate of hotel booking cancellations.
            ### Datasource
            -https://www.kaggle.com/datasets/ahsan81/hotel-reservations-classification-dataset
            ### App Content
            -EDA Section : Exploratory Data Analysis <br>
            -ML Section : ML Predictor App
            """

def main():
        #st.title("Main App")
        
        menu = ["Home","EDA","ML","About"]
        choice = st.sidebar.selectbox("Menu",menu)

        if choice =="Home":
           #st.subheader("Home")
           st.image(c1,use_column_width=True)
           st.markdown(desc_temp,unsafe_allow_html=True)
        elif choice =="EDA":
              run_eda_app()
        elif choice == "ML":
              run_ml_app()
        else:
              st.subheader("About")
       



if __name__=='__main__':
        main()

