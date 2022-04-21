import streamlit as st
from App_Pages import Home,Instruction,AppDescription,CornDiseases,Predict
from model import predict
from streamlit_option_menu import option_menu


st.set_page_config(
    
   page_title="Corn Disease Identification App",
   page_icon="App Images/corn.ico",
   layout="wide",
   initial_sidebar_state="expanded",
)
st.markdown('<style>body{text-align: center;}</style>', unsafe_allow_html=True)


hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: visible;}
    
    footer:before{
        content: 'Programmer @ Markrjmarte9@gmail.com';
        color: #FF4B4B;
        display: block;
        position: relative;
        padding 2px;
        top: 3px;
    }
    </style>
   """
st.markdown(hide_menu_style,unsafe_allow_html=True)


st.image('App Images/Header.jpg',use_column_width=True)

choose = option_menu("", ["Home", "Instruction","Predict Image", "App Description", "Corn Diseases"],
                    icons=['house', 'person lines fill','camera fill', 'app-indicator', 'book'],
                    menu_icon="menu-button-fill", default_index=0, orientation= 'horizontal',
                    styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "center", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"}
    }
    )        



if choose == "Home":
    Home.app()
elif choose == "Predict Image":
    Predict.app()
elif choose == "App Description":
    AppDescription.app()
elif choose == "Corn Diseases":
    CornDiseases.app()
elif choose == "Instruction":
    Instruction.app()

