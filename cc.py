import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image
  
# loading in the model to predict on the data
pickle_in = open('cc.pkl', 'rb')
c= pickle.load(pickle_in)
  
def welcome():
    return 'welcome all'
  
# defining the function which will make the prediction using 
# the data which the user inputs
def prediction(age,mi,g,ms,years,d_amt,cr_amt,cus_tar,tar_desc):  
    prediction = c.predict(np.array([age,mi,g,ms,years,d_amt,cr_amt,cus_tar,tar_desc]).reshape(1,9))
    print(prediction)
    return prediction
      

 #this is the main function in which we define our webpage 
def main():
      # giving the webpage a title
    st.title("Customer Churn")
      
    # here we define some of the front end elements of the web page like 
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Customer Churn </h1>
    </div>
    """
      
    # this line allows us to display the front end aspects we have 
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
      
    # the following lines create text boxes in which the user can enter 
    # the data required to make the prediction
    age= st.text_input("Age","")
    mi= st.text_input("Monthly Income", "")
    g = st.selectbox("Gender", ("FEMALE","MALE"))
    ms=st.selectbox("Marital Staus",('DIVORCE', 'MARRIED', 'OTHER', 'PARTNER', 'SINGLE', 'WIDOWED'))
    years=st.text_input("Years With Us","")
    d_amt=st.text_input("Debit Amount","")
    cr_amt=st.text_input("Credit Amount","")
    cus_tar=st.selectbox("Customer Target",(2211,2212,2222,2223,2224,2230,2231,2232,2233,2234,2235,2236))   
    tar_desc=st.selectbox("Target Description",('EXECUTIVE', 'LOW', 'MIDDLE', 'PLATINUM'))
    
    g_d={'FEMALE':0,'MALE':1}
    ms_d={'DIVORCE':0, 'MARRIED':1, 'OTHER':2, 'PARTNER':3, 'SINGLE':4, 'WIDOWED':5}
    tar_d={'EXECUTIVE':0, 'LOW':1, 'MIDDLE':2, 'PLATINUM':3}
    result =""
    r=""
     
    # the below line ensures that when the button called 'Predict' is clicked, 
    # the prediction function defined above is called to make the prediction 
    # and store it in the variable result
    if st.button("Predict"):
        print(g_d[g],ms_d[ms],tar_d[tar_desc],cus_tar)
        result = prediction(age,mi,g_d[g],ms_d[ms],years,d_amt,cr_amt,cus_tar,tar_d[tar_desc])
        if(result[0]==0):
            r="ACTIVE"
        elif(result[0]==1):
            r="CHURNED"
    st.success('THE CUSTOMER IS {}'.format(r))

if __name__=='__main__':
    main() 