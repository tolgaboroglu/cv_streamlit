from pathlib import Path
import altair as alt
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir /"styles/main.css"
resume_file = current_dir /  "assets/cv_tolga_boroglu_ .pdf"
profile_pic = current_dir / "assets/profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Tolga Boroglu"
PAGE_ICON = ":wave:"
NAME = "Tolga Boroglu"
DESCRIPTION = """
Data Scientist and Machine Learning Developer with 3 years of experience in building statistical and predictive machine learning models, NLP (Natural Language Processing), analyzing noisy datasets, and designing decision support tools and services. Skilled in SQL, Python, and scientific computing languages, with a passion for extracting insights from data and driving data-driven decision-making processes. 
"""
EMAIL = "tolgaboroglu@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "www.youtube.com/@tolgaboroglu",
    "LinkedIn": "https://www.linkedin.com/in/tolgaboroglu/",
    "GitHub": "https://github.com/tolgaboroglu",
    "Twitter": "https://twitter.com/tolgaboroglu", 
    "Medium": "https://medium.com/@tolgaboroglu", 
    
}
PROJECTS = {
    "🏆 Document Scanner App - Web App with OpenCV": "https://github.com/tolgaboroglu/document_scanner_",
    "🏆 Sales Dashboard Power BI - Comparing sales across three stores": "https://github.com/tolgaboroglu/Power_BI_sale_dashboard",
    "🏆 HR Analytics Dashboard  - Tableau Dashboard": "https://public.tableau.com/views/HRDASHBOARD_16784760917540/HRANALYTICSDASBOARD?:language=en-US&:display_count=n&:origin=viz_share_link",

}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Machine Learning Algorithms (PCA, K-means, Random Forest, XGboost, Logistic Regression, SVM , Linear Regression and etc)
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks 
- ✔️ Natural Language Processing (NLP - topics clustering, text generation, sentiment classification) and text analysis. 
- ✔️ Deep Learning (Neural Networks, Convolutional Neural Networks, Recurrent Neural Networks) 
- ✔️ Deep Learning Frameworks (Tensorflow) 
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, 
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Supervised Learning, Unsupervised Learning, Reinforcement Learning
- 🗄️ Databases: MSSQL, Postgres, MongoDB, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", " **Data Analyst | Kodlasam** ")
st.write("03/2023 - 12/2023")
st.write(
    """
- ►  Experienced instructor in Data Analysis using Python, delivering comprehensive instruction to participants in a Bootcamp program.Designed
and developed curriculum materials, lesson plans, and learning resources to effectively convey complex concepts. Provided hands-on training
and guidance, facilitating students' understanding and application of Python for data analysis tasks. Created engaging and interactive learning
experiences through practical exercises and real-world case studies
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", " **BI & DWH Developer | Trive** ")
st.write("06/2023 - 09/2023")
st.write(
    """
- ► Extensive experience in report preparation utilizing Microsoft SQL.
- ►  Demonstrated expertise in the creation and support of Tableau Dashboards.
- ►  Developed and deployed MS SQL and PostgreSQL stored procedures to support ETL processes, resulting in a 15% reduction in manual work
and 20% increase in data loading speed.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", " **Data Scientist - Freelancer | Upwork** ")
st.write("10/2022 - Present")
st.write(
    """
- ► Experienced professional specializing in Natural Language Processing (NLP) and machine learning, providing expert support in developing text and document automation systems. Leveraged Apache Spark for handling big data, building models, and generating reports using machine learning algorithms. Demonstrated proficiency in developing and evaluating advanced algorithms for analyzing text data, achieving an 86% accuracy rate in sentiment analysis. Implemented logistic regression, k-nearest neighbors (k-NN), and gradient boosting models for predictive analytics, achieving a 99% success rate in estimating customer behavior. Skilled in utilizing innovative solutions to streamline processes and enable data-driven decision-making.
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
