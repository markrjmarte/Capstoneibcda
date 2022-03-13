import streamlit as st

 
def app():
    st.empty()
    c=st.container()
    with c :
        st.markdown("""
        <style>
            #site_content{
                    width: 100%;
                    overflow: hidden;
                    background-color: #e1ffca;
                } 
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
                <a>Technology Development</a>
            </div>
            <div class="Paragraph">
                <a>First, with the development of technology, the use of deep learning and image recognition
                    technology for plant disease detection has become an important research direction. This app,
                    is implementing a suitable and fast identification system with machine learning can solve the gap in
                    identifying and classifying the wide variety of corn diseases from images of plant leaves.
                    The identification model focused on using class labels for training images, and built a fine-grained
                    image classification system- a recognition method for corn disease images.</a>
            </div>
            <div class="topnav">
                    <a>App's Purpose</a>
                </div>
                <div class="Paragraph">
                    <a><p>In agriculture environment, image-based corn disease identifier is an advanced technology used to overcome
                    the problems related with all existing techniques of corn disease detection. Image-based corn decease identifier
                    provides very fast and more accurate result which help in disease management. Thus, this App serves as assistance
                    to farmers in preventing, manage and distinguish the variety of corn diseases in a short period of time.
                    We, the proponents of this App are in task of gathering available data sets of corn disease images in which this data
                    set will be used for training the system for it to be able to identify a variety of corn diseases. The system will accept
                    an image input from the user that will undergo object detection in which it will identify all corn diseases that is presented
                    in the image. This project is designed to identify a variety of corn disease. With the help of Image processing,we will implemented
                    an algorithm in which we can detect all of the corn disease in the provided image and identify it individually.
                    </p></a>
                </div>
                <div class="topnav">
                    <a>App's Technicality</a>
                </div>
                <div class="Paragraph">
                    <a><p>The Image-Based Corn Disease Identifier is a Computer-Based software application that identifies the disease of a corn plant.
                    The user can upload an image of a corn plant leaves so that the system can process it and the system can identify corn plant disease.
                    We, the proponents aimed for this software to be capable of running without the use of internet connection. This goal will be able to achieve
                    with the help of CNN model that will be created to train the datasets so that it can be able to classify and identify the corn plant diseases.</p></a>
                </div>
        </body>
        """,unsafe_allow_html=True)
    st.image('App Images\CNN.png',use_column_width=True)
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
                <a>Figure 1. Schematic diagram of Convolutional Neural Network (CNN).</a>
            </div>
            <div class="Paragraph">
                <a><p>Figure 1 shows that convolutional neural network (CNN) has one or more convolutional layers and are used mainly for image processing,
                segmentation, features extraction and classification and also for other auto correlated data. The CNN uses a system much like a multilayer
                perception that has been designed for reduced processing requirements. The layer of CNN consist of an input layer, an output layer and hidden
                layer that includes multiple convolutional layers and normalization layers. The effective way in removal of limitations and increase in
                efficiency for image processing results in a system.</p></a>
            </div>
            <div class="topnav">
                <a>How the App Work</a>
            </div>
            <div class="Paragraph">
                <a><p>The App will be a Computer-Based application in which the user will provide and upload an image in a jpeg. / Jpg. / png.
                format that has a clear image of corn plant leaves on it. The pictures from leaf samples of corn are subjected to undergo image processing
                in which it's enhancing image data so that undesired distortions are suppressed and image features that are relevant for the further processing
                are emphasized. Next, the corn leaf image will undergo image segmentation where the region of interest will be partitioning into different parts
                according to their features and properties. Once the image is segmented, it will proceed to features extraction. The features such as color and
                texture which have to be analyzed were extracted from the image. This may be done to extract the region of interest from the corn leaf image.
                Using the extracted features, it will be then loaded to that training system which is utilizing Convolutional Neutral Network (CNN) machine learning algorithm.
                With the trained system it is then the system will be able to identify the type of disease based on the corn leaf image that is uploaded to the system.</p></a>
            </div>
        </body>
        """,unsafe_allow_html=True)
    st.image('App Images\HTW.PNG',use_column_width=True)
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
                <a>Relevance of Technology</a>
            </div>
            <div class="Paragraph">
                <a><p>A computer is the most needed technology we can use in this system because this will be deployed in a computer-based application.
                Hence, all operations should be mainly done in the computer. Third party cameras or web cams can be used to capture high-definition images
                that we can use as our input data to the system so that we can generate a more accurate result.</p></a>
            </div>
        </body>
        """,unsafe_allow_html=True)
        
   