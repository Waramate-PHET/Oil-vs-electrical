import streamlit as st

st.write("ใส่ code Pythone ในนี้")
st.title("Button Example")
if st.button("Click Me!"):
    st.write("You clicked the button!")
else:
    st.write("Please click the button.")