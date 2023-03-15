#Import required Libraries
import streamlit as st
import pickle
import pandas as pd
import webbrowser  

hide_menu_style = """
<style>
#MainMenu  {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_menu_style, unsafe_allow_html=True)

Stock = pd.read_csv('msft.csv')

st.sidebar.subheader(" ")

st.sidebar.subheader("Charts From:")
st.sidebar.text("National Stock Exchange")

st.sidebar.subheader("Developed By")
st.sidebar.text("Ashwin Raj, ASE at TCS")

st.title('NSE Charts')

selected_chart = st.selectbox('Select Stock', Stock['Name'].values)

url=Stock.loc[Stock['Name'] == selected_chart, 'Link'].item()
st.write(url)

if st.button('Show Chart'):
	webbrowser.open_new_tab(url)
