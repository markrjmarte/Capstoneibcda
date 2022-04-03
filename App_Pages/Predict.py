import streamlit as st
from model import predict

 
def app():
    st.empty
    st.text("")
    img = st.file_uploader(label='Upload corn leaf image (PNG, JPG or JPEG)', type=['png', 'jpg', 'jpeg'])
    if img is not None:
        col1, col2,col3 = st.columns(3)
        col1.text("")
        with col2:
            st.image(image=img.read(), caption='Uploaded image', use_column_width = True, channels = "RGB")
        col3.text("")
        predict_button = st.button(label='Predict')
        if predict_button :
            st.Write("Image")
             
