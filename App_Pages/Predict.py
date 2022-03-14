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
        if predict_button:
            st.text('')
            st.text('')
            prediction_class, prediction_probability = predict(img)
            st.markdown("""
                        <style>
                            .topnav {
                                background-color: #0ed145;
                                overflow: hidden;
                            }
                            .topnav a {
                                display: block;
                                color: #f2f2f2;
                                text-align: center;
                                padding: 14px 16px;
                                text-decoration: none;
                                font-size: 22px;
                            }
                        </style>
                        <body>
                            <div class="topnav">
                                <a>Prediction</a>
                            </div>
                        </body>
                        """,unsafe_allow_html=True)
            st.info(f'Classification: {prediction_class}, Probability: {prediction_probability}%')
             
