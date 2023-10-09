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
st.set_page_config(page_title="Siham Rouabah", page_icon = "desktop_computer", layout = "wide", initial_sidebar_state = "auto")

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
#"""def local_css(file_name):
    #with open(file_name) as f:
    #  st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

##local_css("style.css")"""

footer = """
footer{
    visibility:visible;
}
footer:after{
    content:'Copyright © 2023 Siham Rouabah';
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
img_utown = Image.open("avatar.JPG")
img_lh = Image.open("avatar.JPG")
# Assets for education
img_nus = Image.open("enit.jpg")
img_poc = Image.open("ipein.png")
# Assets for experiences
img_IHU = Image.open("uni-logo.png")
img_OT = Image.open("OL.jpeg")
img_UB = Image.open("UB.jpeg")
img_UE = Image.open("UE.jpeg")
img_ASJP = Image.open("ASJP.png")
img_KOC = Image.open("KidsOut-Logo.png")
img_MD = Image.open("MD.png")
img_CELTA = Image.open("CELTA_png.gif")
img_UB1 = Image.open("UB1.png")
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
                "twitter": "https://img.icons8.com/ios-filled/100/ff8c00/twitter.png",
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
#"""def add_bg_from_local(image_file):
    #with open(image_file, "rb") as image_file:
        #encoded_string = base64.b64encode(image_file.read())
    #st.markdown(
    #f"""
    #<style>
    #.stApp {{
        #background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        #background-size: cover
    #}}
    #</style>
    #""",
    #unsafe_allow_html=True
    #)
#add_bg_from_local('bg.png')   


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
                        "Siham Rouabah ", 
                                  ["About Me","Publications", "Experience", "Skills", "Education", "Conference and Research Experience", "Extra Academic Activities", "Resume",  "Contact"],
                         icons=['person fill',  'globe' ,  'clock history','tools', 'book half','lightbulb', 'clipboard', 'heart', 'paperclip',  'envelope'],
                         menu_icon="mortarboard", 
                         default_index=0
                         #styles={
        #"container": {"padding": "0!important", "background-color": "#f5f5dc"},
        #"icon": {"color": "darkorange", "font-size": "20px"}, 
        #"nav-link": {"font-size": "17px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        #"nav-link-selected": {"background-color": "#cfcfb4"},
    #}
    )
    linkedin_url = "https://www.linkedin.com/in/Rouabah-Siham/"
    twitter_url = "https://twitter.com/SihemRo"
    email_url = "siham.rouabah@outlook.fr"
    with st.container():
        l, m, r = st.columns((0.11,2,0.1))
        with l:
            st.empty()
        with m:
            st.markdown(
                social_icons(30, 30, LinkedIn=linkedin_url, Twitter=twitter_url,  Email=email_url),
                unsafe_allow_html=True)


st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)
st.title("Siham Rouabah, PhD")
# Create header
if choose == "About Me":
    #aboutme.createPage()
    with st.container():
        left_column, middle_column, right_column = st.columns((1,0.2,0.5))
        with left_column:
            st.header("About Me")
            st.subheader(" Sociolinguist, Lecturer of English")
            st.write("👋🏻 Welcome to my Website! I am a passionate sociolinguist with a PhD in Sociolinguistics from the University of Essex. ")
            st.write("💼 My academic journey has honed my expertise in multilingualism, language policies, and sociocultural dynamics. As a lecturer and EFL instructor, I have fostered a passion for language education and empowering learners to embrace linguistic diversity. I take pride in my published works which showcase my commitment to driving meaningful change in language practices. ")
            st.write("👨🏼‍💻 Skilled in SPSS, Nvivo, and fluent in English, Tamazight, Arabic, and French, I thrive in multilingual environments and I advocate for diversity.")
            st.write("💭 Beyond academia, I actively volunteer in teaching, mentoring, and organizing academic events.")
            st.write("📄 [Resume (3 pages)](https://drive.google.com/file/d/1cZO1jUAa569lU6k9VFldlILICf9YqFG1/view?usp=sharing")
        with middle_column:
            st.empty()
        with right_column:
            st.image(img_utown)

# Create section for Work Experience
elif choose == "Experience":
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_IHU)
        with text_column:
            st.subheader("Lecturer of English, Ibn Haldun University, Istanbul, Turkey")
            st.write("October 2022 to  Present")
            
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_OT)
        with text_column:
            st.subheader("Online ESL Instructor, Various platforms")
            st.write("January 2021 to Present")

    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_UB)
        with text_column:
            st.subheader("Lecturer of English, University of Batna2, Batna, Algeria")
            st.write("October 2021 to  September 2022")
            
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_UE)
        with text_column:
            st.subheader("Research Fellow, University of Essex, Essex, UK")
            st.write("January 2021 to  February 2022")

    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_ASJP)
        with text_column:
            st.subheader("Reviewer and Associate Editor, ASJP, Algeria")
            st.write("February 2020 to  Present")
            
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_UE)
        with text_column:
            st.subheader("Graduate Teaching Assistant, University of Essex, Essex, UK")
            st.write("January 2019 to  June 2020")


    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_UE)
        with text_column:
            st.subheader("Laboratory Assistant (SPSS), University of Essex, Essex, UK")
            st.write("January 2020 to  April 2020")
            
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_UE)
        with text_column:
            st.subheader("Outreach Academic Skills Tutor, University of Essex, Essex, UK")
            st.write("January 2018 to  July 2020")
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_UE)
        with text_column:
            st.subheader("Course Representative, Student Union, University of Essex, Essex, UK")
            st.write("January 2019 to  December 2019")
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_UE)
        with text_column:
            st.subheader("VTeam DVC Project Manager, University of Essex, Essex, UK")
            st.write("January 2019 to  December 2019")
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_UE)
        with text_column:
            st.subheader("Graduation Assistant, University of Essex, Essex, UK")
            st.write("July 2018")
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_UE)
        with text_column:
            st.subheader("Reviewer for ESTRO Journal, University of Essex, Essex, UK")
            st.write("January 2018 to  December 2018")        
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_UE)
        with text_column:
            st.subheader("Spicer Library Manager, University of Essex, Essex, UK")
            st.write("January 2017 to  December  2018")
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_KOC)
        with text_column:
            st.subheader("Translator Arabic/English, Algeria and the UK (KidsOut Charity)")
            st.write("2015 to  2018")
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_MD)
        with text_column:
            st.subheader("EFL Teacher, (volunteering), Algeria")
            st.write("2015 to 2016 ")
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_MD)
        with text_column:
            st.subheader("EFL Teacher, Base 04 Middle School, Batna, Algeria")
            st.write("2013 to 2014")




    st.markdown('''
    <style>
    [data-testid="stMarkdownContainer"] ul{
        padding-left:0px;
    }
    </style>
    ''', unsafe_allow_html=True)


# Create section for Technical Skill
elif choose == "Skills":  
     st.header("Skills")
     txt3("Research: ","`Quantitative`, `qualitative`, `mixed methods`.")
     txt3("ESL Teaching","`Lesson planning`, `curriculum design`")
     txt3("IT", "`SPSS`, `Nvivo`, `Microsoft`, `ELAN`, `Rbrul`, `InDesign`, `Stata`, `Affinity Publisher`")
     txt3("Languages", " `English`, `Arabic`, `French`, `Berber`")
     txt3("Event Organisation", "`SLX2017`, `SLX2018`, `SLX2019`")
    
# Create section for Education
elif choose == "Education":
    st.header("Education")
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_CELTA)
        with text_column:
            st.subheader("Cambridge CELTA, Stafford House, London, UK")
            st.write("February 2022 to  March 2022")
            
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_UE)
        with text_column:
            st.subheader("Ph.D. in Sociolinguistics, University of Essex, UK.")
            st.write("September 2016 to Sebtember 2020")

    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_UB1)
        with text_column:
            st.subheader("MA. in Applied Linguistics, University of Batna 1, Algeria.")
            st.write("September 2013 to June 2015")
            
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_UB1)
        with text_column:
            st.subheader("BA. in English Language and Literature, University of Batna 1, Algeria.")
            st.write("September 2010 to  June 2013")

    st.markdown('''
    <style>
    [data-testid="stMarkdownContainer"] ul{
        padding-left:0px;
    }
    </style>
    ''', unsafe_allow_html=True)

elif choose == "Conference and Research Experience":
    st.header("Conference and Research Experience")
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
              
              
              
              
    
elif choose == "Publications":
    selected_topic = st.selectbox("Choose a Topic:", ["PhD Thesis","Journal Papers", "Conference Papers" ])


    if selected_topic == "PhD Thesis":
       st.header("PhD Thesis")
       # Add your research papers here
       paper_name_3 = "Siham Rouabah. ”Language shift or maintenance in Tamazight: A sociolinguistic study of Chaouia in Batna, Algeria.” PhD Thesis, University of Essex, UK, 2020"
       paper_link_3 = "https://repository.essex.ac.uk/28557/1/SihamRouabah%20Thesis.pdf"
       st.markdown(f"[{paper_name_3}]({paper_link_3})")   
      

    elif selected_topic == "Journal Papers":
        st.header("International Journal Papers")
        paper_name_10 = "Siham Rouabah. ”Multilingualism in Algeria: educational policies, language practices and challenges. Journal of the British Academy, 10 (4), 21-40. London, 2022. https://doi.org/10.5871/jba/010s4.021"
        paper_link_10 = "https://doi.org/10.5871/jba/010s4.021"  
        st.markdown(f"[{paper_name_10}]({paper_link_10})")
        paper_name_11 = " Siham Rouabah.”Language shift: gender differences in Chaouia use in Algeria.” International Journal of the Sociology of Language, 2023(281), 23-49.2023. https://doi.org/10.1515/ijsl-2022-0006"
        paper_link_11 = "https://doi.org/10.1515/ijsl-2022-0006"  
        st.markdown(f"[{paper_name_11}]({paper_link_11})")
        paper_name_12 = "Siham Rouabah.”Transitions in the Linguistic Market of Algerian Universities” In the Bringing the outside in Multilingual realities and eduction, Language Science Press, Under Review (fc.2024)"
        paper_link_12 = "https://langsci-press.org/"  
        st.markdown(f"[{paper_name_11}]({paper_link_11})") 
    # Continue adding more papers as needed

    elif selected_topic == "Conference Papers":
       st.header("Conference Papers")
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
    resume_url = "https://drive.google.com/file/d/1cZO1jUAa569lU6k9VFldlILICf9YqFG1/view?usp=sharing"
    st.header("Resume")
    st.write("*In case your current browser cannot display the PDF documents, do refer to the hyperlink below!*")

    st.markdown(pdf_link(resume_url, "**Resume (3 pages)**"), unsafe_allow_html=True)
    show_pdf("resume.pdf")
    with open("resume.pdf", "rb") as file:
        btn = st.download_button(
            label="Download Resume (3 pages)",
            data=file,
            file_name="resume.pdf",
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
            st.write("Let's connect! You may either reach out to me at siham.rouabah@outlook.fr or use the form below!")
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
            linkedin_url = "https://www.linkedin.com/in/Rouabah-Siham/"
            twitter_url = "https://twitter.com/SihemRo"
            email_url = "siham.rouabah@outlook.fr"
            st.markdown(
                social_icons(32, 32, LinkedIn=linkedin_url, Twitter = twitter_url, Email=email_url),
                unsafe_allow_html=True)
            st.markdown("")
        with mid:
            st.empty()
        with image_column:
            st.image(img_utown)
st.markdown("*Copyright © 2023 Siham Rouabah*")
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
