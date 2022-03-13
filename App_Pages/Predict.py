import streamlit as st
from model import predict

import requests
from streamlit_lottie import st_lottie

def load_lottie(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
 
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
            try:
                prediction_class, prediction_probability = predict(img)
                c=st.container()
                with c :
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
                a = f'Classification: {prediction_class}, Probability: {prediction_probability}%'
                html_pre = f"""
                    <style>
                    p.a{{
                        padding: 14px 5px;
                        font: bold 20px Arial;
                        background-color: #e1ffca;
                    }}
                    </style>
                    <p class="a">{a}</p>
                    """
                st.markdown(html_pre,unsafe_allow_html=True)
            except ValueError:
                st.markdown("""
                        <style>
                            .topnav {
                                background-color: #ff4b4b;
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
                            .Paragraph {
                                overflow: hidden;
                                background-color: #e1ffca;
                            }
                            .Paragraph a {
                                display: block;
                                color: Black;
                                text-align: Center;
                                padding: 14px 16px;
                                font-size: 17px;
                            }
                        </style>
                        <body>
                            <div class="topnav">
                                <a>Invalid Input!</a>
                            </div>
                            <div class="Paragraph">
                                <a><p>Sorry, the image you have inputed is invalid for image reshaping and object detection. 
                                <p>Please select another image. Thank you!</p></a>
                             </div>
                        </body>
                        """,unsafe_allow_html=True)
        
