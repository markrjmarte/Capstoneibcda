import streamlit as st
import streamlit.components.v1 as components
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
    MainMenu {visibility: hidden;}
    footer {visibility: visible;}
    
    footer:before{
        content: 'Team Padayon @ 2021-2022: IBCDI';
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
    st.empty()
    with st.container():
         st.markdown("""
            <style>
                .topnav {
                    background-color: #0ed145;
                    overflow: hidden;
                    text-color: white;
                    
                }
                .topnav a {
                    display: block;
                    color: white;
                    text-align: center;
                    padding: 14px 16px;
                    font-size: 22px;
                }
            </style>
            <body>
                <div class="topnav">
                    <a>We are here to provide solution in identifiying Corn diseases</a>
                </div>
            </body>
        """,unsafe_allow_html=True)
    st.markdown("""
            <style>
                #site_content{
                    width: 100%;
                    overflow: hidden;
                    background-color: #e1ffca;
                } 
                .sidebar{ 
                    float: right;
                    width: 50%;
                    padding: 0 20px 20px 15px;
                }
                .sidebar p { 
                    display: block;
                    color: black;
                    text-align: Left;
                    padding: 5px 16px;
                    font-size: 17px;
                }
                #content{ 
                    text-align: left;
                    width: 100%;
                    padding: 5px 16px;
                }
                .Paragraph {
                    overflow: hidden;
                }
                .Paragraph a {
                    display: block;
                    color: Black;
                    text-align: Left;
                    padding: 5px 40px;
                    font-size: 17px;
                }
            </style>
            <body>
                <div id="site_content">
                    <div class="sidebar">
                        <h1 style= "color: #1293EE; font: normal 120% arial, sans-serif; padding: 30px 0 5px 0;">Who we are.</h1>
                        <p>We are Team Padayon, a student of Southern Leyte State Uviversity. We've been making this app to provide helful
                        tools fo the farmers havibg a hard time dealing with corn plant diseases. We're proud and pride ourselves on
                        using this app to help our farmers on what they are expecting. Our team is compose of talented people that are
                        passionate about creating such an app</p>
                        <h1 style= "color: #1293EE; font: normal 120% arial, sans-serif; padding: 20px 0 5px 0;">Our Vission</h1>
                        <p>To generate possible solution and provide a better way to distinguish corn plant diseases.</p>
                        <h1 style= "color: #1293EE; font: normal 120% arial, sans-serif; padding: 20px 0 5px 0;">Our Mission</h1>
                        <p>Aiming for giving a usefull web app that will help the farmer to detect corn diseases more accurately.
                        The team, hopes to create a comfortable and user friendly web app for the user that will be using it.</p>
                        <h1 style= "color: #1293EE; font: normal 120% arial, sans-serif; padding: 20px 0 5px 0;">Prediction Range</h1>
                        <p>As of now the app can only predict the following diseases: Common Rust, Tar Spot, Eyespot, Southern Rust,Northern Corn Leaf Blight, Gray Leaf Spot</p>
                    </div>
                    <div id="content">
                        <div class="Paragraph">
                            <h1 style= "color: #1293EE; font: normal 120% arial, sans-serif; text-align: center; padding: 30px 0 5px 0;">Information</h1>
                            <a><p>The Department of Agriculture (DA) is crafting a strategic and robust corn industry development roadmap 
                            to address the sector’s challenges. The existing techniques that the farmer does is identifying a gray leaf spot, 
                            northern corn leaf blight, tar spot, common and southern rust. The usual process done by a farmer is to submit a 
                            hoto of the possible disease of corn and wait for the Bureau of Plant Industry to confirm and explain what kind of 
                            disease the corn has. This usually takes time and possible disease may worsen before their feedback would be done. 
                            Without using technology, manual disease control can be a waste of time and money, and can lead to further corn losses. 
                            Moreover, knowing and detecting corn diseases as early as possible is essential for keeping your corn crop healthy and 
                            protect your yields as well. Detecting what these diseases looks like is the first step to prevent, protect and avoid 
                            losses in the quantity of corn (Bayer, 2020). 
                            <p>With the development of technology, the use of deep learning and image recognition technology for plant disease 
                            detection has become an important research direction. With this application, implementing a suitable and fast identification 
                            system with machine learning can solve the gap in identifying and classifying the wide variety of corn diseases from 
                            images of plant leaves. The identification model focused on using class labels for training images, and built a fine-grained 
                            image classification system- a recognition method for corn disease images. Hence, this application is using a novel method
                            for identifying the diseases of corn plants using their leaf images. </p></a>
                        </div>
                    </div>
                </div>
            </body>
    """,unsafe_allow_html=True)

    
elif choose == "Predict Image":
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
                
elif choose == "App Description":
    st.empty()
    with st.container():
         st.markdown("""
            <style>
                .topnav {
                    background-color: #0ed145;
                    overflow: hidden;
                    text-color: white;
                    
                }
                .topnav a {
                    display: block;
                    color: white;
                    text-align: center;
                    padding: 14px 16px;
                    font-size: 22px;
                }
            </style>
            <body>
                <div class="topnav">
                    <a>We are here to provide solution in identifiying Corn diseases</a>
                </div>
            </body>
        """,unsafe_allow_html=True)
    st.markdown("""
            <style>
                #site_content{
                    width: 100%;
                    overflow: hidden;
                    background-color: #e1ffca;
                } 
                .sidebar{ 
                    float: right;
                    width: 50%;
                    padding: 0 20px 20px 15px;
                }
                .sidebar p { 
                    display: block;
                    color: black;
                    text-align: Left;
                    padding: 5px 16px;
                    font-size: 17px;
                }
                #content{ 
                    text-align: left;
                    width: 100%;
                    padding: 5px 16px;
                }
                .Paragraph {
                    overflow: hidden;
                }
                .Paragraph a {
                    display: block;
                    color: Black;
                    text-align: Left;
                    padding: 5px 40px;
                    font-size: 17px;
                }
            </style>
            <body>
                <div id="site_content">
                    <div class="sidebar">
                        <h1 style= "color: #1293EE; font: normal 120% arial, sans-serif; padding: 30px 0 5px 0;">Who we are.</h1>
                        <p>We are Team Padayon, a student of Southern Leyte State Uviversity. We've been making this app to provide helful
                        tools fo the farmers havibg a hard time dealing with corn plant diseases. We're proud and pride ourselves on
                        using this app to help our farmers on what they are expecting. Our team is compose of talented people that are
                        passionate about creating such an app</p>
                        <h1 style= "color: #1293EE; font: normal 120% arial, sans-serif; padding: 20px 0 5px 0;">Our Vission</h1>
                        <p>To generate possible solution and provide a better way to distinguish corn plant diseases.</p>
                        <h1 style= "color: #1293EE; font: normal 120% arial, sans-serif; padding: 20px 0 5px 0;">Our Mission</h1>
                        <p>Aiming for giving a usefull web app that will help the farmer to detect corn diseases more accurately.
                        The team, hopes to create a comfortable and user friendly web app for the user that will be using it.</p>
                        <h1 style= "color: #1293EE; font: normal 120% arial, sans-serif; padding: 20px 0 5px 0;">Prediction Range</h1>
                        <p>As of now the app can only predict the following diseases: Common Rust, Tar Spot, Eyespot, Southern Rust,Northern Corn Leaf Blight, Gray Leaf Spot</p>
                    </div>
                    <div id="content">
                        <div class="Paragraph">
                            <h1 style= "color: #1293EE; font: normal 120% arial, sans-serif; text-align: center; padding: 30px 0 5px 0;">Information</h1>
                            <a><p>The Department of Agriculture (DA) is crafting a strategic and robust corn industry development roadmap 
                            to address the sector’s challenges. The existing techniques that the farmer does is identifying a gray leaf spot, 
                            northern corn leaf blight, tar spot, common and southern rust. The usual process done by a farmer is to submit a 
                            hoto of the possible disease of corn and wait for the Bureau of Plant Industry to confirm and explain what kind of 
                            disease the corn has. This usually takes time and possible disease may worsen before their feedback would be done. 
                            Without using technology, manual disease control can be a waste of time and money, and can lead to further corn losses. 
                            Moreover, knowing and detecting corn diseases as early as possible is essential for keeping your corn crop healthy and 
                            protect your yields as well. Detecting what these diseases looks like is the first step to prevent, protect and avoid 
                            losses in the quantity of corn (Bayer, 2020). 
                            <p>With the development of technology, the use of deep learning and image recognition technology for plant disease 
                            detection has become an important research direction. With this application, implementing a suitable and fast identification 
                            system with machine learning can solve the gap in identifying and classifying the wide variety of corn diseases from 
                            images of plant leaves. The identification model focused on using class labels for training images, and built a fine-grained 
                            image classification system- a recognition method for corn disease images. Hence, this application is using a novel method
                            for identifying the diseases of corn plants using their leaf images. </p></a>
                        </div>
                    </div>
                </div>
            </body>
    """,unsafe_allow_html=True)

elif choose == "Corn Diseases":
    st.empty
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
                text-align: Left;
                padding: 14px 16px;
                text-decoration: none;
                font-size: 22px;
            }
            .Paragraph {
                background-color: #e1ffca;
                overflow: hidden;
            }
            .Paragraph a {
                display: block;
                color: black;
                text-align: Left;
                padding: 14px 16px;
                font-size: 17px;
            }
        </style>
        <body>
            <div class="topnav">
                    <a>What is Corn/Maize crops?</a>
                </div>
                <div class="Paragraph">
                    <a><p>Maize, Zea mays, is an annual grass in the family Poaceae and is a staple food crop grown all over the world. 
                    he maize plant possesses a simple stem of nodes and internodes. A pair of large leaves extend off of each internode 
                    and the leaves total 8–21 per plant. The leaves are linear or lanceolate (lance-like) with an obvious midrib (primary vein) 
                    and can grow from 30 to 100 cm (11.8–39.4 in) in length. The male and female inflorescences (flower bearing region of the plant) a
                    re positioned separately on the plant. The male inflorescence is known as the ‘tassel’ while the female inflorescence is the ‘ear’. 
                    The ear of the maize is a modified spike and there may be 1–3 per plant. The maize grains, or ‘kernels’, are encased in husks and total 30–1000 per ear. 
                    The kernels can be white, yellow, red, purple or black. Maize is an annual plant, surviving for only one growing season and can 
                    reach 2–3 m (7–10 ft) in height.</p></a>
                    <a style= "background-color: #aae27f" >Foliar Fungal Diseases</a>
                </div>
                <div class="Paragraph">
                    <a><p>Several diseases are economically important for corn production. Most of the major corn diseases 
                    are foliar – meaning they affect the leaves – which vary from year to year because they are strongly influenced by 
                    weather conditions. Thus, accurate identification and an awareness of potential disease losses are essential for continued 
                    successful corn production. </p></a>
                </div>
        </body>
        """,unsafe_allow_html=True)
    
    
        
        
        
    st.text('')
    #Southern Rust
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
                text-align: Left;
                padding: 14px 16px;
                text-decoration: none;
                font-size: 22px;
            }
            .Paragraph {
                background-color: #e1ffca;
                overflow: hidden;
            }
            .Paragraph a {
                display: block;
                color: black;
                text-align: Left;
                padding: 14px 16px;
                font-size: 17px;
            }
        </style>
        <body>
            <div class="topnav">
                    <a>1. Southern Rust</a>
                </div>
                <div class="Paragraph">
                    <a><p>Southern rust is caused by the fungus Puccinia polysora. Although generally considered a tropical disease, 
                    southern rust can occur in important corn production areas of the United States and Canada. Symptoms are similar 
                    to common rust, but pustules are smaller and occur almost exclusively on the upper leaf surface. Pustules are usually 
                    circular or oval, very numerous, and densely scattered over the leaf surface. Spores are orange 
                    when they erupt from the pustule. As pustules age, they become chocolate brown to black, often forming dark 
                    circles around the original pustule.</p></a>
                    <a style= "background-color: #aae27f" >Sounthern Rust Cycle</a>
                </div>
                <div class="Paragraph">
                    <a><p>Southern rust is caused by the fungus Puccinia polysora, which only infects corn. 
                    Pustules of southern rust are small (0.2 to 2 mm in diameter), circular to oval and light cinnamon 
                    brown to orange, they frequently form on the upper leaf surface and very rarely on the lower leaf surface 
                    (Figure 2). Southern rust pustules may occur on leaves, stalks, sheaths, and Husks. 
                    <p>Southern rust is easily overlooked by the casual observer early in the season because initial infections are typically only one to two pustules per plant
                    (Figure 1: Cycle). The absence of sporulation on the lower leaf surface early in the season is an indication of southern rust. 
                    As indicated earlier, rust sporulation on the lower leaf surface is associated with common rust, a minor disease. Early-season 
                    southern rust pustule development is most frequently observed in the field at mid-canopy (4 to 5 feet from the ground) along the edge 
                    of the field. Free moisture as dew or light rain is necessary for rust spores to germinate and infect. Symptoms appear about 3 to 6 days 
                    after infection, and by 7 to 10 days the pustules may rupture to expose more rust spores. Thus, new infections can occur very rapidly after 
                    the initial infection when conditions favor disease. Conditions that favor disease develop-ment consist of high temperatures (80° to 90°F), 
                    high relative humidity and frequent rainfall/ heavy dew. Even in hot summer conditions with temperatures above 100°F, pustules continue to 
                    sporulate, hence the name southern rust.</p></a>
                </div>
        </body>
        """,unsafe_allow_html=True)
    with st.expander("View Image"):
        st.image('App Images\Sr_cycle.png',use_column_width=True)
        st.image('App Images\Sr.png',use_column_width=True)
    st.text('')
  
    #Eyespot
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
                text-align: Left;
                padding: 14px 16px;
                text-decoration: none;
                font-size: 22px;
            }
            .Paragraph {
                background-color: #e1ffca;
                overflow: hidden;
            }
            .Paragraph a {
                display: block;
                color: black;
                text-align: Left;
                padding: 14px 16px;
                font-size: 17px;
            }
        </style>
        <body>
            <div class="topnav">
                <a>2. Eyespot</a>
            </div>
            <div class="Paragraph">
                <a><p>Eyespot is caused by the fungus Aureobasidium zeae. The initial 
                symptoms of eyespot are small, water-soaked or chlorotic circular spots (Figure 3). The tissue at the center of the spot later dies 
                and turns tan-colored with a brown ring at the margin. The spot is surrounded by a yellow “halo" that can be seen clearly 
                when the leaf is lighted from behind. Spots may join together into large necrotic areas and the entire leaf may die. The spots 
                remain visible even after the leaf dies. The disease is more common when corn follows corn. Cool temperatures (60s°F to low 70s°F) 
                favor disease development; thus, eyespot may appear early in the season on lower leaves and again near the end of the season on 
                upper leaves.</p></a>
            </div>
        </body>
        """,unsafe_allow_html=True)
    with st.expander("View Image"):
        st.image('App Images\F_ES.png',use_column_width=True)
    st.text('')
    
    #Gray Leaf Spot
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
                text-align: Left;
                padding: 14px 16px;
                text-decoration: none;
                font-size: 22px;
            }
            .Paragraph {
                background-color: #e1ffca;
                overflow: hidden;
            }
            .Paragraph a {
                display: block;
                color: black;
                text-align: Left;
                padding: 14px 16px;
                font-size: 17px;
            }
        </style>
        <body>
            <div class="topnav">
                <a>3. Gray Leaf Spot</a>
            </div>
            <div class="Paragraph">
                <a><p>Gray leaf spot, caused by the fungus Cercospora zeae-maydis, occurs virtually every growing season. 
                If conditions favor disease development, economic losses can occur. Symptoms first appear on lower leaves about two to three weeks before tasseling. 
                The leaf lesions are long (up to 2 inches), narrow, rectangular, and light tan colored. Later, the lesions can turn gray (Figure 5). They are usually 
                delimited by leaf veins but can join together and kill entire leaves.Rectangular gray leaf spot lesions delimited by leaf veins. </p></a>
                <a style= "background-color: #aae27f"> Gray leaf spot disease cycle.</a>
            </div>
            <div class="Paragraph">
                <a><p>The fungus survives in corn residue, and, consequently, the disease is often more severe in corn following corn (Figure 4: Cycle). 
                Spores are dispersed by wind and splashing water. Infection of corn leaves and disease development are favored by warm 
                (80s°F), humid (>90% for 12+ hours) weather. Disease severity depends on hybrid susceptibility and environmental conditions.</p></a>
            </div>
        </body>
        """,unsafe_allow_html=True)
    with st.expander("View Image"):
        st.image('App Images\GL_cycle.png',use_column_width=True)
        st.image('App Images\F_GS.png',use_column_width=True)
    st.text('')
      
        
    #Tar Spot
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
                text-align: Left;
                padding: 14px 16px;
                text-decoration: none;
                font-size: 22px;
            }
            .Paragraph {
                background-color: #e1ffca;
                overflow: hidden;
            }
            .Paragraph a {
                display: block;
                color: black;
                text-align: Left;
                padding: 14px 16px;
                font-size: 17px;
            }
        </style>
        <body>
            <div class="topnav">
                <a>4. Tar Spot</a>
            </div>
            <div class="Paragraph">
                <a><p>Tar spot is caused by the fungus Phyllachora maydis, and can cause severe yield loss on susceptible hybrids when 
                conditions are favorable for disease. Tar spot appears as small, raised, black spots scattered across the upper and lower leaf surfaces. 
                These spots are ascomatum (fungal fruiting structures). If viewed under the microscope, hundreds of sausage-shaped asci (spore cases) 
                filled with spores are visible. When severe, ascomatum can even appear on husks and leaf sheaths.Tan to brown lesions with dark borders 
                surrounding ascomatum can also develop. These are known as “fisheye” lesions. In Latin America, where tar spot is more common, fisheye 
                lesions are associated with another fungus, Monographella maydis, that forms a disease complex with P. maydis known as the tar spot complex.
                <p>At the end of the growing season, common and southern rust pustules can be mistaken for tar spot ascomatum as these rusts switch 
                from producing orange-red spores (urediniospores) to black spores (teliospores). However, rust spores burst through the epidermis and the 
                spores can be scraped away from the pustules with a fingernail while tar spots cannot be scraped off the leaf tissue.Characteristic tar spot 
                symptoms and signs on corn leaf. The pathogen that causes tar spot overwinters on infested corn residue on the soil surface, and it is 
                thought that high relative humidity and prolonged leaf wetness favor disease development. Residue management, rotation, and avoiding 
                susceptible hybrids may reduce tar spot development and severity. Some fungicides may also reduce tar spot, although little data exists 
                regarding application timing for efficacy and economic response (Figure 6). </p></a>
            </div>
        </body>
        """,unsafe_allow_html=True)
    with st.expander("View Image"):
        st.image('App Images\F_TS.png',use_column_width=True)
        st.image('App Images\F_TS1.png',use_column_width=True)
    st.text('')
    
    #Nothern Leaf Blight
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
                text-align: Left;
                padding: 14px 16px;
                text-decoration: none;
                font-size: 22px;
            }
            .Paragraph {
                background-color: #e1ffca;
                overflow: hidden;
            }
            .Paragraph a {
                display: block;
                color: black;
                text-align: Left;
                padding: 14px 16px;
                font-size: 17px;
            }
        </style>
        <body>
            <div class="topnav">
                <a>5. Northern Corn Leaf Blight</a>
            </div>
            <div class="Paragraph">
                <a><p>Northern corn leaf blight (NCLB) is caused by the fungus Setosphaeria turcica. Symptoms usually appear first 
                on the lower leaves. Leaf lesions are long (1 to 6 inches) and elliptical, gray-green at first but then turn pale gray or tan. 
                Under moist conditions, dark gray spores are produced, usually on the lower leaf surface, which give lesions a “dirty” gray appearance. 
                Entire leaves on severely blighted plants can die, so individual lesions are not visible(Figure 8). Lesions may occur on the outer husk of ears, 
                but the kernels are not infected. On hybrids that contain an Ht gene for resistance to the fungus, lesions are smaller, chlorotic, 
                and may develop into linear streaks. These lesions rarely produce spores.</p></a>
                <a style= "background-color: #aae27f">Northern Corn Leaf Blight Cycle.</a>
            </div>
            <div class="Paragraph">
                <a><p>The fungus overwinters in corn residue. Spores are dispersed by wind and splashing water. Disease development 
                is favored by extended periods (>6 hours) of leaf wetness (rain or dew) and moderate temperatures (64-81°F). There are at
                least four races of the fungus, with race 1 being the most predominant. Resistant hybrids are available and should be grown when disease 
                is a potential problem. There are two types of resistance to NCLB, monogenic (Ht genes – resistance that is controlled by one gene) 
                and polygenic (resistance that is controlled by many genes). Hybrids with an Ht gene are susceptible to some races of the pathogen. 
                Polygenic resistance provides resistance to all races, but the resistance is not as absolute as Ht resistance. Crop rotation and surface 
                residue reduction through tillage can decrease inoculum. There are several foliar fungicides that are labeled for NCLB. (Figure 7 : Cycle) </p></a>
            </div>
        </body>
        """,unsafe_allow_html=True)
    with st.expander("View Image"):
        st.image('App Images\nn_cycle.jpg',use_column_width=True)
        st.image('App Images\northern.jpg',use_column_width=True)
    st.text('')  
    
    #Common Rust
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
                text-align: Left;
                padding: 14px 16px;
                text-decoration: none;
                font-size: 22px;
            }
            .Paragraph {
                background-color: #e1ffca;
                overflow: hidden;
            }
            .Paragraph a {
                display: block;
                color: black;
                text-align: Left;
                padding: 14px 16px;
                font-size: 17px;
            }
        </style>
        <body>
            <div class="topnav">
                <a>6. Common Rust</a>
            </div>
            <div class="Paragraph">
                <a><p>Common rust is caused by the fungus Puccinia sorghi and occurs every growing season. 
                It is seldom a concern in hybrid corn. Rust pustules usually first appear in late June. Early symptoms of common rust 
                are chlorotic flecks on the leaf surface. These soon develop into powdery, brick-red pustules as the spores break through 
                the leaf surface. Pustules are oval or elongated, about 1/8 inch long, and scattered sparsely or clustered together. 
                The leaf tissue around the pustules may become yellow or die, leaving lesions of dead tissue. The lesions sometimes form a 
                band across the leaf and entire leaves will die if severely infected. As the pustules age, the red spores turn black, so the 
                pustules appear black, and continue to erupt through the leaf surface (Figure 9). Husks, leaf sheaths, and stalks also may be infected.
                The fungus survives the winter as spores in subtropical and tropical regions; spores are carried long distances by wind and 
                eventually reach the Midwest. Rust development is favored by high humidity with night temperatures of 65-70°F and moderate daytime 
                tem
        </body>
        """,unsafe_allow_html=True)
    with st.expander("View Image"):
        st.image('App Images\F_CR.png',use_column_width=True)
        st.image('App Images\F_CR1.png',use_column_width=True)
    st.text('')  
elif choose == "Instruction":
    st.empty()
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
                text-align: Left;
                padding: 14px 16px;
                text-decoration: none;
                font-size: 22px;
            }
            .Paragraph {
                background-color: #e1ffca;
                overflow: hidden;
            }
            .Paragraph a {
                display: block;
                color: black;
                text-align: Left;
                padding: 14px 16px;
                font-size: 17px;
            }
        </style>
        <body>
            <div class="topnav">
                <a>How to open streamlit file?</a>
            </div>
            <div class="Paragraph">
                <a>1.First locate the file location.</a>
            </div>
        </body>
        """,unsafe_allow_html=True)
        st.image('App Images\I1.png',use_column_width=True)
        st.markdown("""
        <style>
            .Paragraph {
                background-color: #e1ffca;
                overflow: hidden;
            }
            .Paragraph a {
                display: block;
                color: black;
                text-align: Left;
                padding: 14px 16px;
                font-size: 17px;
            }
        </style>
        <body>
            <div class="Paragraph">
                <a>2.Open the App folder or Any folder where you've saved the File “Corn_App.py” or the Main app(.py).</a>
            </div>
        </body>
        """,unsafe_allow_html=True)
        st.image('App Images\I2.png',use_column_width=True)
        st.markdown("""
        <style>
            .Paragraph {
                background-color: #e1ffca;
                overflow: hidden;
            }
            .Paragraph a {
                display: block;
                color: black;
                text-align: Left;
                padding: 14px 16px;
                font-size: 17px;
            }
        </style>
        <body>
            <div class="Paragraph">
                <a>3.Open Command Prompt or CMD.</a>
            </div>
        </body>
        """,unsafe_allow_html=True)
        st.image('App Images\I3.png',use_column_width=True)
        st.markdown("""
        <style>
            .Paragraph {
                background-color: #e1ffca;
                overflow: hidden;
            }
            .Paragraph a {
                display: block;
                color: black;
                text-align: Left;
                padding: 14px 16px;
                font-size: 17px;
            }
        </style>
        <body>
            <div class="Paragraph">
                <a>4.In CMD, encode “streamlit run Corn_App.py” or streamlit run (then the Main App (.py)) then Enter.</a>
            </div>
        </body>
        """,unsafe_allow_html=True)
        st.image('App Images\I4.png',use_column_width=True)
        st.markdown("""
        <style>
            .Paragraph {
                background-color: #e1ffca;
                overflow: hidden;
            }
            .Paragraph a {
                display: block;
                color: black;
                text-align: Left;
                padding: 14px 16px;
                font-size: 17px;
            }
        </style>
        <body>
            <div class="Paragraph">
                <a>5.After that, the Streamlit App can be view in your browser.</a>
            </div>
        </body>
        """,unsafe_allow_html=True)
        st.image('App Images\I5.png',use_column_width=True)
        st.text('')
        st.text('')
        st.text('')
        st.text('')
        st.markdown("""
        <style>
            .topnav {
                background-color: #0ed145;
                overflow: hidden;
            }
            .topnav a {
                display: block;
                color: #f2f2f2;
                text-align: Left;
                padding: 14px 16px;
                text-decoration: none;
                font-size: 22px;
            }
            .Paragraph {
                background-color: #e1ffca;
                overflow: hidden;
            }
            .Paragraph a {
                display: block;
                color: black;
                text-align: Left;
                padding: 14px 16px;
                font-size: 17px;
            }
        </style>
        <body>
            <div class="topnav">
                <a>How to use Corn Disease Idenintification App?</a>
            </div>
            <div class="Paragraph">
                <a>1.In Uploading an image. Just click the BROWSE FILE BUTTON.</a>
            </div>
        </body>
        """,unsafe_allow_html=True)

        st.image('App Images\I6.png',use_column_width=True)
        st.markdown("""
            <style>
            .Paragraph {
                background-color: #e1ffca;
                overflow: hidden;
            }
            .Paragraph a {
                display: block;
                color: black;
                text-align: Left;
                padding: 14px 16px;
                font-size: 17px;
            }
            </style>
            <body>
            <div class="Paragraph">
                <a>2.Select an image that you want to use.</a>
            </div>
            </body>
            """,unsafe_allow_html=True)
        st.image('App Images\I7.png',use_column_width=True)
        st.markdown("""
        <style>
            .Paragraph {
                background-color: #e1ffca;
                overflow: hidden;
            }
            .Paragraph a {
                display: block;
                color: black;
                text-align: Left;
                padding: 14px 16px;
                font-size: 17px;
            }   
        </style>
        <body>
            <div class="Paragraph">
                <a>3.After the image uploaded. Click PREDICT BUTTON and wait for the result.</a>
            </div>
        </body>
        """,unsafe_allow_html=True)
        st.image('App Images\I8.png',use_column_width=True)
        st.markdown("""
        <style>
            .Paragraph {
                background-color: #e1ffca;
                overflow: hidden;
            }
            .Paragraph a {
                display: block;
                color: black;
                text-align: Left;
                padding: 14px 16px;
                font-size: 17px;
            }
        </style>
        <body>
            <div class="Paragraph">
                <a>4.The application will predict the image and state the identification with the probability percentage.</a>
            </div>
        </body>
        """,unsafe_allow_html=True)
        st.image('App Images\9.png',use_column_width=True)


