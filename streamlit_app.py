import streamlit as st

st.header('st.button')

if st.button('Please Click Here'):
     st.write('Why did you click')
else:
     st.write('Goodbye Boy')