#Import required Libraries
import streamlit as st
import pickle
import pandas as pd

#Stock = pd.DataFrame({'Link' : ["https://in.investing.com/equities/axis-bank-chart", "https://in.investing.com/equities/hdfc-bank-chart"] }, index=['Axis', 'HDFC'])
Stock = pd.read_csv('msft.csv')

#Frontend Design for StreamLit WebApp Sidebar
st.sidebar.subheader(" ")

st.sidebar.subheader("Technology:")
st.sidebar.text("Natural Language Processing")

st.sidebar.subheader("Developed By")
st.sidebar.text("Ashwin Raj, Student at UCEK")

#movies_dict = pickle.load(open('pickle/movie_dict.pkl','rb'))
#movies = pd.DataFrame(movies_dict)

#similarity = pickle.load(open('pickle/similarity.pkl','rb'))

#Frontend Hero Section
st.title('NSE Charts')


selected_chart = st.selectbox('Select Stock', Stock['Link'].values)

#Output Recommendations with Posters
if st.button('Show Chart'):
	st.write(selected_chart.Link)
