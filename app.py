import streamlit as st
from streamlit_option_menu import option_menu
from streamlit.components.v1 import html
from st_on_hover_tabs import on_hover_tabs
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import streamlit_analytics
import base64
from streamlit_extras.mention import mention
from streamlit_extras.app_logo import add_logo
import sqlite3
from bs4 import BeautifulSoup
from streamlit_extras.echo_expander import echo_expander



# Set page title
st.set_page_config(page_title="Amen Allah Berrejeb", page_icon = "desktop_computer", layout = "wide", initial_sidebar_state = "auto")

# Use the following line to include your style.css file
#st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def render_lottie(url, width, height):
    lottie_html = f"""
    <html>
    <head>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/lottie-web/5.7.14/lottie.min.js"></script>
    </head>
    <body>
        <div id="lottie-container" style="width: {width}; height: {height};"></div>
        <script>
            var animation = lottie.loadAnimation({{
                container: document.getElementById('lottie-container'),
                renderer: 'svg',
                loop: true,
                autoplay: true,
                path: '{url}'
            }});
            animation.setRendererSettings({{
                preserveAspectRatio: 'xMidYMid slice',
                clearCanvas: true,
                progressiveLoad: false,
                hideOnTransparent: true
            }});
        </script>
    </body>
    </html>
    """
    return lottie_html

# Use local CSS
"""def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#local_css("style.css")"""

footer = """
footer{
    visibility:visible;
}
footer:after{
    content:'Copyright © 2023 Amenallah Berrejeb';
    position:relative;
    color:black;
}
"""
# PDF functions
def show_pdf(file_path):
        with open(file_path,"rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="400" height="600" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

def pdf_link(pdf_url, link_text="Click here to view PDF"):
    href = f'<a href="{pdf_url}" target="_blank">{link_text}</a>'
    return href

# Load assets
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
# Assets for about me
img_utown = Image.open("fb_new copy.jpg")
img_lh = Image.open("fb_new copy.jpg")
# Assets for education
img_nus = Image.open("enit.jpg")
img_poc = Image.open("ipein.png")
# Assets for experiences
img_saf = Image.open("tt.png")
img_groundup = Image.open("m&c.png")
# Assets for experiences
img_ieee = Image.open("IEEE.png")
img_gdsc = Image.open("GDSC.png")
# Assets for projects
img_qt=Image.open("qt.png")
img_neural=Image.open("neural.jpg")
img_geo=Image.open("geospatial.jpg")
img_breast=Image.open("breast_cancer.png")
img_racing=Image.open("racing.png")
img_jax=Image.open("jax.png")
# Assets for contact
lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_abqysclq.json")

img_linkedin = Image.open("linkedin.png")
img_github = Image.open("github.png")
img_email = Image.open("email.png")

def social_icons(width=24, height=24, **kwargs):
        icon_template = '''
        <a href="{url}" target="_blank" style="margin-right: 20px;">
            <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
        </a>
        '''

        icons_html = ""
        for name, url in kwargs.items():
            icon_src = {
                "youtube": "https://img.icons8.com/ios-filled/100/ff8c00/youtube-play.png",
                "linkedin": "https://img.icons8.com/ios-filled/100/ff8c00/linkedin.png",
                "github": "https://img.icons8.com/ios-filled/100/ff8c00/github--v2.png",
                "email": "https://img.icons8.com/ios-filled/100/ff8c00/filled-message.png"
            }.get(name.lower())

            if icon_src:
                icons_html += icon_template.format(url=url, icon_src=icon_src, alt_text=name.capitalize(), width=width, height=height)

        return icons_html
#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)


def txt3(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'<p style="font-size: 20px;">{a}</p>', unsafe_allow_html=True)
  with col2:
    b_no_commas = b.replace(',', '')
    st.markdown(b_no_commas)

def txt4(a, b):
  col1, col2 = st.columns([1.5,2])
  with col1:
    st.markdown(f'<p style="font-size: 25px; color: white;">{a}</p>', unsafe_allow_html=True)
  with col2: #can't seem to change color besides green
    st.markdown(f'<p style="font-size: 25px; color: red;"><code>{b}</code></p>', unsafe_allow_html=True)

#####################
"""def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('bg.png')  """ 


# Sidebar: If using streamlit_option_menu
with st.sidebar:
    with st.container():
        l, m, r = st.columns((1,3,1))
        with l:
            st.empty()
        with m:
            st.empty()
        with r:
            st.empty()
    
    choose = option_menu(
                        "Amen Allah  Berrejeb ", 
                        ["About Me", "Papers That Inspire Me","My Research Paper", "Experience", "Technical Skills", "Education", "Projects", "Extra Academic Activities", "Resume",  "Contact"],
                         icons=['person fill',  'lightbulb' , 'globe', 'clock history', 'tools', 'book half', 'clipboard', 'heart', 'paperclip',  'envelope'],
                         menu_icon="mortarboard", 
                         default_index=0,
                         styles={
        "container": {"padding": "0!important", "background-color": "#f5f5dc"},
        "icon": {"color": "darkorange", "font-size": "20px"}, 
        "nav-link": {"font-size": "17px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#cfcfb4"},
    }
    )
    linkedin_url = "https://www.linkedin.com/in/amen-berrjeb-639101256/"
    github_url = "https://github.com/berrejebamen"
    email_url = "mailto:amenallah.berrejb@etudiant-enit.utm."
    with st.container():
        l, m, r = st.columns((0.11,2,0.1))
        with l:
            st.empty()
        with m:
            st.markdown(
                social_icons(30, 30, LinkedIn=linkedin_url, GitHub=github_url,  Email=email_url),
                unsafe_allow_html=True)


st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)
st.title("Amen Allah Berrejeb")
# Create header
if choose == "About Me":
    #aboutme.createPage()
    with st.container():
        left_column, middle_column, right_column = st.columns((1,0.2,0.5))
        with left_column:
            st.header("About Me")
            st.subheader("Aspiring Data Scientist , Machine Learning Engineer , AI Research engineer")
            st.write("👋🏻 Amenallah Berrejeb a Final year ICT engineering student at national engineering school of tunis (ENIT) , motivated and dynamic student , curious and learns quickly . I aim to grow my knowledge in Data Science sector and its subfields . Currently , I spend a lot of time learning on Coursera and DeepLearning.AI , reading machine learning papers and exploring their codes from paperswithcode.com and doing some beginner kaggle competitions.")
            st.write("💼 I secured a commendable rank in the Tunisian National Competitions for Entry to Engineering Training Cycles, showcasing my academic aptitude. This was followed by my significant contribution to the AI domain, marked by the publication of my research paper in the IEEE AMCAI: 1st IEEE AfroMediterranean Conference on Artificial Intelligence, titled Towards A Machine Learning based Platform for Diseases Detection: Case of Breast Cancer under the supervision of my teacher . Additionally, I undertook an enriching NLP summer internship at M&C, focusing on comparative studies of transformerbased language models for ADAD project comprehension and delving into the state-of-the-art LLMs research.")
            st.write("👨🏼‍💻 Academic interests: Data Visualization, Machine Learning Algorithms, Data science, Natural Language Processing , Computer Vision")
            st.write("💭 Ideal Career Prospects: Data Analyst, Data Scientist, AI Research engineer, Machine Learning Engineer, AI Researcher")
            st.write("📄 [Resume (2 pages)](https://drive.google.com/file/d/1DPwtSv5JUY2IRflcZX9wCfgFZFa9SR3M/view?usp=drive_link")
        with middle_column:
            st.empty()
        with right_column:
            st.image(img_utown)
elif choose == "My Research Paper":   
    resume_url = "https://drive.google.com/file/d/1wR1000t-96d48qinqq9lP4OPS14cz2K7/view?usp=drive_link"
    st.header("My Research Paper")
    st.write("*In case your current browser cannot display the PDF documents, do refer to the hyperlink below!*")

    st.markdown(pdf_link(resume_url, "**Research paper (7 pages)**"), unsafe_allow_html=True)
    show_pdf("my_research_paper.pdf")
    with open("my_research_paper.pdf", "rb") as file:
        btn = st.download_button(
            label="Download paper (7 pages)",
            data=file,
            file_name="my_research_paper.pdf",
            mime="application/pdf"
        )
# Create section for Work Experience
elif choose == "Experience":
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_groundup)
        with text_column:
            st.subheader("NLP Intern, [M&C IT CONSULTING](https://mnc.aero/)")
            st.write("*July to August 2023 (Summer Internship)")
            st.markdown("""
            - Developing a comparative study of transformer-based language models on ADAD (M&C's project) specifications understanding
            - Browsing the state-of-the-art of LLMs Research papers
            - Training GPT on the company's  text data 
            `Python` `Pytorch` `NLTK` `Confluence` `T5` `GPT` `BERT` `ALBERT` `Langchain` `Streamlit`
            """)
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_saf)
        with text_column:
            st.subheader("Summer Intern, [Tunisie Telecom](https://www.tunisietelecom.tn/particulier/)")
            st.write("July 2022 to August 2022| [Observation Internship]")
            st.markdown("""
            - An introduction to the telecommunications field , study of transmissions supports and line building center
            """)
    st.markdown('''
    <style>
    [data-testid="stMarkdownContainer"] ul{
        padding-left:0px;
    }
    </style>
    ''', unsafe_allow_html=True)


# Create section for Technical Skills
elif choose == "Technical Skills":
    #st.write("---")
    st.header("Technical Skills")
    txt3("Programming Languages"," `Python`, `C++`, `Java`, `C`, `MATLAB`")
    txt3("Academic Interests","`Data Visualization`, `Machine learning Algorithms`, `Computer Vision`, `Natural Language Processing`")
    txt3("Data Visualization", "`missingno`, `matplotlib`, `seaborn`, `Plotly`")
    txt3("Cloud Platforms", " `Amazon Web Services`")
    txt3("Natural Language Processing", "`NLTK`, `Tranformers`, `Question Answering`")
    txt3("Model Deployement and Front-end Development", " `Streamlit`")
    txt3("Data Science Techniques", "`Regression`, `Clustering`, `XGBOOST`, `Random Forest`, `Decison Trees`, `Principal Components Analysis`")
    txt3("Machine Learning  and Deep Learning Frameworks", "`Numpy`, `Pandas`, `Scikit-Learn`, `TensorFlow`, `Pytorch`, `JAX`")

# Create section for Education

elif choose == "Education":
    st.header("Education")
    selected_options = ["Summary", "Modules"]
    selected = st.selectbox("Which section would you like to read?", options = selected_options)
    st.write("Current selection:", selected)
    if selected == "Summary":
        st.subheader("Summary")
        st.write("*Summary of education from primary school till university*")
        with st.container():
            image_column, text_column = st.columns((1,2.5))
            with image_column:
                st.image(img_nus)
            with text_column:
                st.subheader("Information and Communication Technologies Engineering Degree - [Telecommunications](http://www.enit.rnu.tn/fr/diverses/arrete.25.04.17.php), [National Engineering School Of Tunis](http://www.enit.rnu.tn/fr/diverses/news.php) (2021-2024)")
                st.write("Relevant Coursework: Signal Processing,  Electronics ,C, C++, JAVA, Databases, JEE, MATLAB, Statistics, Probability, Antenna, 4G, 5G,Entrepreneurship and Innovation ,PL/ SQL")
        with st.container():
            image_column, text_column = st.columns((1,2.5))
            with image_column:
                st.image(img_poc)
            with text_column:
                st.subheader("Two year Undergraduate Program Preparing For The National Engineeering School Entrance Competitions - Mathematics And Physics, [Preparatory Institute For Engineering Studies](https://ipein.rnu.tn/) (2019-2021)")
                st.write("Coursework:  Chemistry, Physics, Algebra, Integral Calculus, Python, Mecahnics")                
        with st.container():
            
            st.subheader("High School Diploma - [High School Road Tabarka Mateur] (2018 - 2019)")
            st.write("Coursework: English, Mathematics, Science, Physics, French, Philosophy, Arabic, Sports")

    elif selected == "Modules of this Year : 2023/2024":
        st.subheader("Modules of this Year")
        with st.container():
          left, mid, right = st.columns((0.1, 1, 0.1))
        
          with left:
            st.empty()
            
          with mid:
            # Display the image in the center
            st.image("plan.png", caption="Modules for Final Year")  
            st.write("If the photo is not clear enough and you need more information, you can visit [this link](http://www.enit.rnu.tn/fr/ressources/PE2122/FIL/TE.index.htm).")  
        
          with right:
            st.empty()
elif choose == "Projects":
    st.header("Projects")
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("FashionMNIST: A Deep Dive into JAX Modeling")
            st.write("*Ongoing Project : First time trying jax library with the famous fashion MNIST dataset. *")
        with image_column:
            st.image(img_jax)
     
    keywords = ["Jax ", "Deep Learning", "Image Dataset Analysis"]
    colors = ["#FF5733"]
    colored_keywords = ', '.join([f'<span style="color: {colors[idx % len(colors)]}">{keyword}</span>' for idx, keyword in enumerate(keywords)])
    st.markdown(f"**Keywords**: {colored_keywords}", unsafe_allow_html=True)
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader(" Simulation of Racing Cars Game using Reinforcement Learning")
            st.write("*Ongoing Project*")
        with image_column:
            st.image(img_racing)
     
    keywords = ["OpenAI Gym ", "Intellignet Agent", "State" ,"Reward"]
    colors = ["#FF5733"]
    colored_keywords = ', '.join([f'<span style="color: {colors[idx % len(colors)]}">{keyword}</span>' for idx, keyword in enumerate(keywords)])
    st.markdown(f"**Keywords**: {colored_keywords}", unsafe_allow_html=True)     
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader(" Internship Project: Building a Comparative Study  of Transformer-based language models on ADAD(M&C's Project) specifications understanding.")
            st.write("*This internship project presents a comparative study of Transformers-based language models, with a primary focus on their efficacy in understanding project specifications. The analysis delves into various models, highlighting their strengths and weaknesses in the context of extracting meaningful insights from project requirements. Additionally, the report provides an overview of key research papers in the realm of Large Language Models (LLMs). This comparative study aims to furnish readers with a clearer picture of the capabilities and limitations of current Transformer architectures in project specification comprehension.*")
            mention(label="Github Code", icon="github", url="https://github.com/berrejebamen/Building_comparative_study_of_large_language_models_on_a_project_specifcations_understanding",)
        with image_column:
            st.image(img_groundup)
     
    keywords = ["BERT", "T5", "ALBERT" , "Project Specifications" , "GPT" , "Pytorch" , "Transformers" ,"ROUGE Score", "Research", ""]
    colors = ["#FF5733"]
    colored_keywords = ', '.join([f'<span style="color: {colors[idx % len(colors)]}">{keyword}</span>' for idx, keyword in enumerate(keywords)])
    st.markdown(f"**Keywords**: {colored_keywords}", unsafe_allow_html=True)   
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("End of Year 2 Project: Developing a Streamlit Web Application for Breast Cancer Detection")
            st.write("*Starting from 2 datasets, I built a user-friendly web application that allows doctors to predict whether a breast tumor is malignant or benign and to predict the possibility of developing breast cancer.*")
            mention(label="Github Code", icon="github", url="https://github.com/berrejebamen/Breast_cancer_web_app",)
        with image_column:
            st.image(img_breast)
     
    keywords = ["Streamlit", "Machine Learning For Medical Diagnosis", "Data Analysis"]
    colors = ["#FF5733"]
    colored_keywords = ', '.join([f'<span style="color: {colors[idx % len(colors)]}">{keyword}</span>' for idx, keyword in enumerate(keywords)])
    st.markdown(f"**Keywords**: {colored_keywords}", unsafe_allow_html=True)                  
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("End of Year 1 Project: A Bibliographic Research about Geospatial Big Data")
            st.write("*Reviewing the methods used to gather, analyse geospatial big data, state-of-the-art review of machine learning methods and framework used in the geospatial domain.*")
            mention(label="Google Drive", icon="📁", url="https://drive.google.com/file/d/10ZC8aL0IBz-z2youe7EGlOGk31-TV79u/view?usp=drive_link",)
        with image_column:
            st.image(img_geo)
    keywords = ["Cloud Computing", "Machine Learning Applied to Geospatial Data", "GIS Framework"]
    colors = ["#FF5733"]
    colored_keywords = ', '.join([f'<span style="color: {colors[idx % len(colors)]}">{keyword}</span>' for idx, keyword in enumerate(keywords)])        
    st.markdown(f"**Keywords**: {colored_keywords}", unsafe_allow_html=True)    
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Building a Small Neural Network from Scratch")
            st.write("*Instead of using predefined frameworks , I built a small neural network using Numpy*")
            mention(label="Github Code", icon="github", url="",)
        with image_column:
            st.image(img_neural)
    keywords = ["Deep Learning", "Numpy", "Activation Functions"]
    colors = ["#FF5733"]
    colored_keywords = ', '.join([f'<span style="color: {colors[idx % len(colors)]}">{keyword}</span>' for idx, keyword in enumerate(keywords)])
    st.markdown(f"**Keywords**: {colored_keywords}", unsafe_allow_html=True)         
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
           st.subheader("Library Management Desktop Application")
           st.write("An object-oriented project dedicated to build a desktop application combining several technologies like QT framework and SQL databases.")   
           mention(label="Google Drive", icon="📁", url="https://www.loom.com/share/48c64c036f0545a8b903d415aa3ef605?sid=7e635573-20bd-45ef-9185-0e2e665fea56",)
        with image_column:
              st.image(img_qt)
    keywords = ["QT framework", "SQL ", "C++"]
    colors = ["#FF5733"]
    colored_keywords = ', '.join([f'<span style="color: {colors[idx % len(colors)]}">{keyword}</span>' for idx, keyword in enumerate(keywords)])
    st.markdown(f"**Keywords**: {colored_keywords}", unsafe_allow_html=True)      
              
              
              
              
    
elif choose == "Papers That Inspire Me":
    selected_topic = st.selectbox("Choose a Topic:", ["Computer Vision", "NLP", "Machine Learning"])

    if selected_topic == "Computer Vision":
        st.header("Computer Vision Papers")
        paper_name_10 = "Going Deeper with Convolutions"
        paper_link_10 = "https://arxiv.org/pdf/1409.4842v1.pdf"  
        st.markdown(f"[{paper_name_10}]({paper_link_10})")
        paper_name_11 = "U-Net: Convolutional Networks for Biomedical Image Segmentation"
        paper_link_11 = "https://arxiv.org/pdf/1505.04597v1.pdf"  
        st.markdown(f"[{paper_name_11}]({paper_link_11})")
        paper_name_12 = "MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications"
        paper_link_12 = "https://arxiv.org/pdf/1704.04861v1.pdf"  
        st.markdown(f"[{paper_name_12}]({paper_link_12})")
        paper_name_13 = "MobileNetV2: Inverted Residuals and Linear Bottlenecks"
        paper_link_13 = "https://arxiv.org/pdf/1801.04381v4.pdf"  
        st.markdown(f"[{paper_name_13}]({paper_link_13})")
        paper_name_14 = "GradientBased Learning Applied to Document Recognition"
        paper_link_14 = "http://vision.stanford.edu/cs598_spring07/papers/Lecun98.pdfs"  
        st.markdown(f"[{paper_name_14}]({paper_link_14})")
        paper_name_15 = "You Only Look Once: Unified, Real-Time Object Detection"
        paper_link_15 = "https://arxiv.org/pdf/1506.02640v5.pdf"  
        st.markdown(f"[{paper_name_15}]({paper_link_15})")
        paper_name_16 = "FaceNet: A Unified Embedding for Face Recognition and Clustering"
        paper_link_16 = "https://arxiv.org/pdf/1503.03832v3.pdf"  
        st.markdown(f"[{paper_name_16}]({paper_link_16})")
    # Continue adding more papers as needed

    elif selected_topic == "NLP":
       st.header("NLP Papers")
       paper_name_2 = "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"
       paper_link_2 = "https://arxiv.org/pdf/1810.04805v2.pdf" 
       st.markdown(f"[{paper_name_2}]({paper_link_2})")
       paper_name_4 = "ALBERT: A LITE BERT FOR SELF-SUPERVISED LEARNING OF LANGUAGE REPRESENTATIONS"
       paper_link_4 = "https://arxiv.org/pdf/1909.11942v6.pdf" 
       st.markdown(f"[{paper_name_4}]({paper_link_4})") 
       paper_name_5 = "Language Models are Few-Shot Learners"
       paper_link_5 = "https://arxiv.org/pdf/2005.14165v4.pdf" 
       st.markdown(f"[{paper_name_5}]({paper_link_5})") 
       paper_name_6 = "BLEU: a Method for Automatic Evaluation of Machine Translation"
       paper_link_6 = "https://aclanthology.org/P02-1040.pdf" 
       st.markdown(f"[{paper_name_6}]({paper_link_6})") 
       paper_name_8 = "Attention Is All You Need"
       paper_link_8 = "https://arxiv.org/pdf/1706.03762v7.pdf" 
       st.markdown(f"[{paper_name_8}]({paper_link_8})") 
       paper_name_9 = "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer"
       paper_link_9 = "https://arxiv.org/pdf/1910.10683v4.pdf" 
       st.markdown(f"[{paper_name_9}]({paper_link_9})") 

    elif selected_topic == "Machine Learning":
       st.header("Machine Learning Papers")
       # Add your research papers here
       paper_name_3 = "XGBoost: A Scalable Tree Boosting System"
       paper_link_3 = "https://arxiv.org/pdf/1603.02754v3.pdf"  
       st.markdown(f"[{paper_name_3}]({paper_link_3})")
       paper_name_17 = "RANDOM FORESTS"
       paper_link_17 = "https://www.stat.berkeley.edu/~breiman/randomforest2001.pdf"  
       st.markdown(f"[{paper_name_17}]({paper_link_17})")
       paper_name_18 = "Scikit-learn: Machine Learning in Python"
       paper_link_18 = "https://arxiv.org/pdf/1201.0490v4.pdf"  
       st.markdown(f"[{paper_name_18}]({paper_link_18})")



elif choose == "Extra Academic Activities":
    st.header("Extra Academic Activities")
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_ieee)
        with text_column:
            st.subheader("Senior Member, [IEEE ENIT STUDENT BRANCH ]")
            st.write("October 2021 Until Now")
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_gdsc)
        with text_column:
            st.subheader("Senior Member, [GOOGLE DEVELOPER STUDENT CLUBS , ENIT]")
            st.write("October 2021 Until Now ")


elif choose == "Resume":   
    resume_url = "https://drive.google.com/file/d/1DPwtSv5JUY2IRflcZX9wCfgFZFa9SR3M/view?usp=drive_link"
    st.header("Resume")
    st.write("*In case your current browser cannot display the PDF documents, do refer to the hyperlink below!*")

    st.markdown(pdf_link(resume_url, "**Resume (2 pages)**"), unsafe_allow_html=True)
    show_pdf("Amen_Allah_Berrejeb (3).pdf")
    with open("Amen_Allah_Berrejeb (3).pdf", "rb") as file:
        btn = st.download_button(
            label="Download Resume (2 pages)",
            data=file,
            file_name="AMENALLAH.pdf",
            mime="application/pdf"
        )
elif choose == "Contact":
# Create section for Contact
    st.header("Contact")
    def social_icons(width=24, height=24, **kwargs):
        icon_template = '''
        <a href="{url}" target="_blank" style="margin-right: 10px;">
            <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
        </a>
        '''

        icons_html = ""
        for name, url in kwargs.items():
            icon_src = {
                "linkedin": "https://cdn-icons-png.flaticon.com/512/174/174857.png",
                "github": "https://cdn-icons-png.flaticon.com/512/25/25231.png",
                "email": "https://cdn-icons-png.flaticon.com/512/561/561127.png"
            }.get(name.lower())

            if icon_src:
                icons_html += icon_template.format(url=url, icon_src=icon_src, alt_text=name.capitalize(), width=width, height=height)

        return icons_html
    with st.container():
        text_column, mid, image_column = st.columns((1,0.2,0.5))
        with text_column:
            st.write("Let's connect! You may either reach out to me at amenallah.berrejeb@etudiant-enit.utm.tn or use the form below!")
            def create_database_and_table():
                conn = sqlite3.connect('contact_form.db')
                c = conn.cursor()
                c.execute('''CREATE TABLE IF NOT EXISTS contacts
                            (name TEXT, email TEXT, message TEXT)''')
                conn.commit()
                conn.close()
            create_database_and_table()

            st.subheader("Contact Form")
            if "name" not in st.session_state:
                st.session_state["name"] = ""
            if "email" not in st.session_state:
                st.session_state["email"] = ""
            if "message" not in st.session_state:
                st.session_state["message"] = ""
            st.session_state["name"] = st.text_input("Name", st.session_state["name"])
            st.session_state["email"] = st.text_input("Email", st.session_state["email"])
            st.session_state["message"] = st.text_area("Message", st.session_state["message"])


            column1, column2= st.columns([1,5])
            if column1.button("Submit"):
                conn = sqlite3.connect('contact_form.db')
                c = conn.cursor()
                c.execute("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)",
                        (st.session_state["name"], st.session_state["email"], st.session_state["message"]))
                conn.commit()
                conn.close()
                st.success("Your message has been sent!")
                # Clear the input fields
                st.session_state["name"] = ""
                st.session_state["email"] = ""
                st.session_state["message"] = ""
            def fetch_all_contacts():
                conn = sqlite3.connect('contact_form.db')
                c = conn.cursor()
                c.execute("SELECT * FROM contacts")
                rows = c.fetchall()
                conn.close()
                return rows
            
            if "show_contacts" not in st.session_state:
                st.session_state["show_contacts"] = False
            if column2.button("View Submitted Forms"):
                st.session_state["show_contacts"] = not st.session_state["show_contacts"]
            
            if st.session_state["show_contacts"]:
                all_contacts = fetch_all_contacts()
                if len(all_contacts) > 0:
                    table_header = "| Name | Email | Message |\n| --- | --- | --- |\n"
                    table_rows = "".join([f"| {contact[0]} | {contact[1]} | {contact[2]} |\n" for contact in all_contacts])
                    markdown_table = f"**All Contact Form Details:**\n\n{table_header}{table_rows}"
                    st.markdown(markdown_table)
                else:
                    st.write("No contacts found.")


            st.write("Alternatively, feel free to check out my social accounts below!")
            linkedin_url = "https://www.linkedin.com/in/amen-berrjeb-639101256/"
            github_url = "https://github.com/berrejebamen"
            email_url = "mailto:amenallah.berrejeb@etudiant-enit.utm.tn"
            st.markdown(
                social_icons(32, 32, LinkedIn=linkedin_url, GitHub=github_url, Email=email_url),
                unsafe_allow_html=True)
            st.markdown("")
        with mid:
            st.empty()
        with image_column:
            st.image(img_utown)
st.markdown("*Copyright © 2023 Amen Allah Berrejeb*")

