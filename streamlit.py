# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 17:48:15 2021

@author: user
"""

import streamlit as st
import requests


def main():

    st.title("Stock Price Prediction")
    message = st.text_input('Enter News Headlines to Classify')

    if st.button('Predict'):
        url="http://127.0.0.1:8000/predict"
        myobj = {
            "text": message
        }
        res = requests.post(url,json=myobj )
        with st.spinner('Classifying, please wait....'):
            st.write(res.json())




if __name__ == '__main__':
    main()
