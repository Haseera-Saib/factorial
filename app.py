import streamlit as st

st.header('Factorial Of Number')

num=st.number_input('Enter a number',value=0)
btn=st.button("Factorial")

if btn:    
    result=1 
    for i in range(1,num+1): 
         result=result*i   
    st.subheader(result)
  
         

