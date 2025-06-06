import streamlit as st
from PIL import Image
import os

def education_page():
    st.markdown("""
        <style>
        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        .gradient-bar {
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
        
        .gradient-text {
            font-size: 3rem;
            font-weight: bold;
            text-transform: uppercase;
            color: #4B0082;
        }

        .education-section {
            background: linear-gradient(45deg, #E8B8B7, #F7C9D3, #B5ABCC, #B8D7EE);
            padding: 20px;
            border-radius: 15px;
            margin: 20px 0;
            line-height: 1.6;
        }
        .undergrad-section {
            background: linear-gradient(45deg, #FAE0DD, #E8B8B7, #A9A4C8, #90ADC5);
            padding: 20px;
            border-radius: 15px;
            margin: 20px 0;
        }

        .slide-container {
            display: flex !important;
            flex-direction: row !important;
            overflow-x: auto !important;
            gap: 20px !important;
            padding: 20px 0 !important;
            scroll-snap-type: x mandatory !important;
            direction: ltr !important;
            scroll-behavior: smooth !important;
            width: 100% !important;
        }
        .slide {
            flex: 0 0 auto !important;
            width: 60% !important;
            scroll-snap-align: center !important;
            min-width: 60% !important;
            transition: transform 0.3s ease, box-shadow 0.3s ease !important;
            position: relative !important;
        }
        .slide:hover {
            transform: translateY(-10px) !important;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2) !important;
        }
        .slide img {
            width: 100% !important;
            height: auto !important;
            border-radius: 15px !important;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1) !important;
            max-height: 500px !important;
            object-fit: contain !important;
            transition: all 0.3s ease !important;
        }
        .slide:hover img {
            border-radius: 20px !important;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2) !important;
        }
        .slide::after {
            content: '' !important;
            position: absolute !important;
            top: 0 !important;
            left: 0 !important;
            right: 0 !important;
            bottom: 0 !important;
            border-radius: 15px !important;
            box-shadow: 0 0 0 0 rgba(0, 0, 0, 0) !important;
            transition: box-shadow 0.3s ease !important;
            pointer-events: none !important;
        }
        .slide:hover::after {
            box-shadow: 0 0 0 4px rgba(165, 180, 204, 0.3) !important;
        }
        .slide-container::-webkit-scrollbar {
            height: 8px !important;
        }
        .slide-container::-webkit-scrollbar-track {
            background: #f1f1f1 !important;
            border-radius: 4px !important;
        }
        .slide-container::-webkit-scrollbar-thumb {
            background: #888 !important;
            border-radius: 4px !important;
            transition: background 0.3s ease !important;
        }
        .slide-container::-webkit-scrollbar-thumb:hover {
            background: #555 !important;
        }
        .project-container {
            border: 3px solid #B5ABCC !important;
            border-radius: 20px !important;
            background: rgba(181, 171, 204, 0.1) !important;
            box-shadow: 0 0 15px rgba(181, 171, 204, 0.2) !important;
            padding: 20px !important;
            margin: 20px 0 !important;
            width: 70% !important;
            max-width: 1000px !important;
        }
        .education-section strong, .undergrad-section strong {
            font-size: 1.2rem;
            font-weight: 700;
            line-height:1.6;
        }
        .education-section h2, .undergrad-section h2 {
            font-size: 1.5rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }
        </style>
        <div class="gradient-bar">
            <div class="gradient-text">Where and what I learn?</div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("## Education")
    
    st.markdown("""
        <div class="education-section">
            <h2>Master of Science in Marketing</h2>
            <p><strong>Chinese University of Hong Kong</strong></p>
            <p>2024 - 2025</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="education-section">
        <strong>Curriculum:</strong><br>
        Customer Analytics, Digital Marketing, Integrated Marketing, Machine Learning in Marketing, Social Media Analytics, Big Data Strategy
        
        <strong>Relevant Coursework:</strong><br>
        Marketing Mix Modeling, Data Visualization, R for Marketing Analytics, Plan and Execution of IMC, Customer Classification, Sentiment Analysis
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="undergrad-section">
            <h2>Bachelor of Science in Accounting</h2>
            <p><strong>Xiamen University</strong></p>
            <p>2017 - 2021</p>
            <p>GPA: 3.3/4.0</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="education-section">
        <strong>Curriculum:</strong><br> Financial Accounting, Management Accounting, Cost Accounting, Auditing, Taxation, Financial Management<br>
        <strong>Honors and Awards:</strong><br>
        Excellent Academic Scholarship for Undergraduates, Xiamen University, Class of 2020-2021, 06/2021<br>
        Merits Student, Xiamen University, Class of 2021, 06/2021<br>
        Excellent Academic Scholarship for the 2nd Semester of the 2020 Academic Year, Xiamen University, 12/2020<br>
        Outstanding Student Cadre, Management School, Xiamen University, 2018-2019 Academic Year, 07/2019
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("## Academic Projects")
    
    st.markdown("""
        ### Word Frequency and Sentiment Analysis of UCG Content
        <div class="project-container">
        <strong>- Explore the social buzz brought to the brand</strong><br>
        &nbsp;&nbsp;- Total 20131 text were collected and cleaned<br>
        &nbsp;&nbsp;- 16612 text from Weibo and 506 posts from RED were analyized<br><br>
        <strong>- Evaluate the effectiveness of campaign through word frequency andsentiment analysis</strong><br>
        &nbsp;&nbsp;- Attitude comparison acorss different time periods<br>
        &nbsp;&nbsp;- Engagement trend analysis during the campaign<br><br>
        <strong>- Provide advice on future marketing strategy based on the analysis</strong>

        <div class="slide-container">
    """, unsafe_allow_html=True)
    
    # 加载并显示三张PPT图片
    ppt_images = ["Bawang1.png", "Bawang2.png", "Bawang3.png"]
    for img_name in ppt_images:
        image_path = os.path.join("static", "images", img_name)
        if os.path.exists(image_path):
            image = Image.open(image_path)
            st.markdown(f'<div class="slide"><img src="data:image/png;base64,{image_to_base64(image)}" alt="{img_name}"></div>', unsafe_allow_html=True)
        else:
            st.warning(f"Image {img_name} not found")
    
    st.markdown('</div></div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
        ### Analysis of Owned Media Strategy in DOUYIN Live-Streaming
        <div class="project-container">
        <strong>- Live-streaming rooms teardown</strong><br>
        &nbsp;&nbsp;- Matrix operation analysis<br>
        &nbsp;&nbsp;- Generate word cloud for different rooms<br>
        &nbsp;&nbsp;- Audience Behavior analysis, including duration time of stay and viewers amount<br><br>
        <strong>- Evaulation the success of livestreaming martix strategy</strong><br>
        &nbsp;&nbsp;- User profile analysis<br>
        &nbsp;&nbsp;- Sales data analysis<br><br>
        <strong>- Identify potential problems and provide recommendations for live-streaming strategy</strong>

        <div class="slide-container">
    """, unsafe_allow_html=True)
    
    # 加载并显示三张PPT图片
    douyin_images = ["Hanshu1.png", "Kans2.png", "Kans3.png"]
    for img_name in douyin_images:
        image_path = os.path.join("static", "images", img_name)
        if os.path.exists(image_path):
            image = Image.open(image_path)
            st.markdown(f'<div class="slide"><img src="data:image/png;base64,{image_to_base64(image)}" alt="{img_name}"></div>', unsafe_allow_html=True)
        else:
            st.warning(f"Image {img_name} not found")
    
    st.markdown('</div></div>', unsafe_allow_html=True)
    
    st.markdown("---") 
    
    st.markdown("""
        ### IMC Campaign Project
        <div class="project-container">
        <strong>- STP analysis and 5-box positioning statement</strong><br>
        &nbsp;&nbsp;- Survey consumers' current impression<br>
        &nbsp;&nbsp;- Reword consumer proposition and USP for brand<br>
        <strong>- Design the IMC campaign</strong><br>
        &nbsp;&nbsp;- Generate big idea and roadmap<br>
        &nbsp;&nbsp;- Design promotion activities: Ad video, out-of-home, influencer marketing<br><br>
        <strong>- Layout evaluation plan</strong>

        <div class="slide-container">
    """, unsafe_allow_html=True)
    
    # 加载并显示三张PPT图片
    douyin_images = ["Jinro1.png", "Jinro2.png", "Jinro3.png"]
    for img_name in douyin_images:
        image_path = os.path.join("static", "images", img_name)
        if os.path.exists(image_path):
            image = Image.open(image_path)
            st.markdown(f'<div class="slide"><img src="data:image/png;base64,{image_to_base64(image)}" alt="{img_name}"></div>', unsafe_allow_html=True)
        else:
            st.warning(f"Image {img_name} not found")
    
    st.markdown('</div></div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("## Other Projects")
    
    projects = [
        {
            "title": "Customer Clustering",
            "description": "Used K-means clustering to segment customers based on demographic features and purchasing behavior.",
            "skills/methods": ["Python", "Pandas", "Matplotlib","Random Forest","Elbow"],
            "outcome": "Identified 3 distinct customer segments and identify the most valuable group."
        },
        {
            "title": "Choice Model Design and Analysis",
            "description": "Developed the choice model questions, ran logistic regression and analyzed its result.",
            "skills/methods": ["Sawtooth"],
            "outcome": "Identify the most important features through coefficient analysis and predict the share of preference."
        }
    ]
    
    for i, project in enumerate(projects):
        with st.expander(f"{project['title']}", expanded=i==0):
            st.markdown(f"**Description:** {project['description']}")
            st.markdown(f"**Skills Used:** {', '.join(project['skills/methods'])}")
            st.markdown(f"**Outcome:** {project['outcome']}")
    
    st.markdown("---")
    
    st.markdown("## 3 Core Knowledge Mastered")
    
    cert1, cert2, cert3 = st.columns(3)
    
    with cert1:
        st.markdown("""
        ### Marketing theoretical knowledge
        
        Grasped knowledge in strategic brand management, digital marketing, buyer behavior and big data marketing.
        """)
        
    with cert2:
        st.markdown("""
        ### Analytics and processing skills 
        
        Demonstrated expertise in data collecting, pre-processing, analysis and visualization.
        """)
        
    with cert3:
        st.markdown("""
        ### Business economics
        
         Acquired knowledge in micro/macro-economic, financial analysis and global business management.
        """)
    
    st.markdown("---")

def image_to_base64(image):
    """将PIL图像转换为base64字符串"""
    import base64
    from io import BytesIO
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode() 