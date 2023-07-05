import streamlit as st
import db

st.title('Daily retention')

k_val = st.number_input('Insert a number',min_value=1,max_value=7,step=1)
st.write("Retention for day ",f"{k_val}"," is ","%.2f"%db.daykretention(k_val))
