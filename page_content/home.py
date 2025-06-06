import streamlit as st
from PIL import Image
import os

def home_page():
    # 添加自定义CSS样式
    st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
        <style>
        .top-gradient-bar {
            background: linear-gradient(45deg, #FAE0DD, #E8B8B7, #A9A4CB, #90ADC5);
            background-size: 300% 300%;
            animation: gradient 15s ease infinite;
            height: 100px;
            width: 100%;
            margin-bottom: 30px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .top-gradient-bar h1 {
            color: #4B0082;
            font-family: 'Playfair Display', serif;
            font-size: 3rem;
            font-weight: 700;
            letter-spacing: 2px;
            text-transform: uppercase;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
            margin: 0;
            background: linear-gradient(45deg, #4B0082, #2E0854);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: textGradient 15s ease infinite;
        }
        .about-me-box {
            background: linear-gradient(45deg, #E6E6FA, #EEC1DD, #969BE7);
            background-size: 200% 200%;
            animation: gradient 15s ease infinite;
            padding: 30px;
            border-radius: 15px;
            margin: 20px 0;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }
        .about-me-box h3 {
            color: #4B0082;
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 20px;
            text-align: center;
            letter-spacing: 1px;
        }
        .about-me-box p {
            color: #2E0854;
            font-family: 'Montserrat', sans-serif;
            font-size: 1.1rem;
            line-height: 1.8;
            margin: 0;
        }
        @keyframes textGradient {
            0% {
                background-position: 0% 50%;
            }
            50% {
                background-position: 100% 50%;
            }
            100% {
                background-position: 0% 50%;
            }
        }
        @keyframes gradient {
            0% {
                background-position: 0% 50%;
            }
            50% {
                background-position: 100% 50%;
            }
            100% {
                background-position: 0% 50%;
            }
        }
        .gradient-background {
            background: linear-gradient(45deg, #E6E6FA, #EEC1DD, #969BE7);
            background-size: 200% 200%;
            animation: gradient 15s ease infinite;
            padding: 20px;
            border-radius: 10px;
            margin: 10px 0;
        }
        .gradient-background h4 {
            color: #4B0082;
            margin: 0;
        }
        .gradient-background p {
            color: #2E0854;
            margin: 10px 0;
        }
        .gradient-background a {
            color: #4B0082;
            text-decoration: none;
        }
        .gradient-background a:hover {
            text-decoration: underline;
        }
        .skills-box {
            background: linear-gradient(45deg, #E6E6FA, #EEC1DD, #969BE7);
            background-size: 200% 200%;
            animation: gradient 15s ease infinite;
            padding: 25px;
            border-radius: 15px;
            margin: 20px 0;
        }
        .skills-box h3 {
            color: #4B0082;
            font-family: 'Montserrat', sans-serif;
            font-size: 1.5rem;
            margin-bottom: 15px;
        }
        .skills-box ul {
            color: #2E0854;
            font-size: 1.1rem;
            line-height: 1.8;
            margin: 0;
            padding-left: 20px;
        }
        .skills-box li {
            margin-bottom: 8px;
        }
        </style>
    """, unsafe_allow_html=True)

    # 添加顶部渐变条和文字
    st.markdown('<div class="top-gradient-bar"><h1>Who am I?</h1></div>', unsafe_allow_html=True)

    left_col, right_col = st.columns(2)
    left_col.markdown(
        """
        <div class="gradient-background">
            <h4>Congxuan CHEN</h4>
            <h4>陈丛萱</h4>
            <p>Recent Master's Graduate in Marketing<br>
            the Chinese University of Hong Kong<br>
            12 Chak Cheung St., Ma Liu Shui<br>
            <a href="mailto:chencongxuan@163.com">chencongxuan@163.com</a></p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # add a photo to the right column
    image_path = os.path.join("static", "images", "me.jpg")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        right_col.image(image, width=200)
    else:
        right_col.warning("Profile image not found")

    st.markdown("---")

    # About Me section with fancy design
    st.markdown(
        """
        <div class="about-me-box">
            <h3>About Me</h3>
            <p>I am a recent postgraduate student majoring in Marketing at CUHK, with an undergraduate degree in Accounting, skilled in digital marketing and data analysis(Python,R). <br>
            I am a strong learner with excellent analytical skills, the spirit of teamwork and creative thinking ability.<br> I am adept at extracting core information from data and making business predictions and decisions based on analysis results.<br> I am eager to scientifically analyze changes in consumer psychology and behaviour in the era of digital media and big data, optimize content output and delivery channels, help companies effectively convey brand value to customers, and even inspire consumers to create content that benefits brand promotion.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Skills section with gradient background
    st.markdown(
        """
        <div class="skills-box">
            <h3>Skills</h3>
            <ul>
                <li>Languages: Mandarin, IELTS 7.5(Spoken 8.0)</li>
                <li>Programming Languages: Python, R</li>
                <li>Data Analysis: Pandas, NumPy, Matplotlib</li>
                <li>Statistical Analysis: Descriptive Statistics, Regression Analysis, Logistic Regression</li>
                <li>Other Skills: SQL, SPSS, Photoshop</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")
    
    # Interactive component has been moved to the experience page 