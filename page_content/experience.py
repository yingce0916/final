import streamlit as st
import base64
from PIL import Image
import io
import os

def get_image_base64(image_path):
    img = Image.open(image_path)
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

def show_experience():
    st.markdown("""
        <style>
        .experience-container {
            background: rgba(255, 255, 255, 0.9);
            padding: 20px;
            border-radius: 15px;
            margin: 20px 0;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        </style>
    """, unsafe_allow_html=True)

def experience_page():
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
            font-weight: 800;
            text-transform: uppercase;
            color: #4B0082;
        }

        .experience-section {
            background: linear-gradient(45deg, #EEC1DD, #D1D0EF, #FCFBFB);
            padding: 20px;
            border-radius: 15px;
            margin: 20px 0;
        }

        .experience-section h3 {
            font-size: 1.5rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            color: #000000;
        }

        .experience-section strong {
            font-size: 1.2rem;
            font-weight: 700;
            color: #4B0082;
        }

        .experience-section em {
            font-style: italic;
        }

        .experience-section p {
            line-height: 1.8;
            color: #2C3E50;
            margin: 15px 0;
            text-shadow: 0.5px 0.5px 1px rgba(0,0,0,0.1);
        }

        .experience-section ul {
            list-style-type: none;
            padding-left: 0;
            margin: 15px 0;
        }

        .experience-section li {
            line-height: 1.8;
            color: #2C3E50;
            margin: 10px 0;
            padding-left: 20px;
            position: relative;
            text-shadow: 0.5px 0.5px 1px rgba(0,0,0,0.1);
        }

        .experience-section li:before {
            content: "•";
            color: #4B0082;
            font-weight: bold;
            position: absolute;
            left: 0;
        }

        .gallery {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            margin: 20px 0;
        }

        .gallery-item {
            position: relative;
            overflow: hidden;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }

        .gallery-item:hover {
            transform: scale(1.05);
        }

        .gallery-item img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }

        .project-section {
            background: linear-gradient(45deg, #EEC1DD, #D1D0EF, #FCFBFB);
            padding: 25px;
            border-radius: 15px;
            margin: 30px 0;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }

        .project-section h3 {
            font-size: 1.5rem;
            font-weight: 700;
            color: #000000;
            margin-bottom: 1rem;
            border-bottom: 2px solid #4B0082;
            padding-bottom: 8px;
        }

        .project-section strong {
            font-size: 1.2rem;
            font-weight: 700;
            color: #4B0082;
            display: block;
            margin: 15px 0 8px 0;
        }

        .project-section em {
            font-style: italic;
            color: #666;
            display: block;
            margin-bottom: 12px;
        }

        .project-section ul {
            list-style-type: none;
            padding-left: 0;
            margin: 15px 0;
        }

        .project-section li {
            line-height: 1.8;
            color: #2C3E50;
            margin: 12px 0;
            padding-left: 25px;
            position: relative;
            text-shadow: 0.5px 0.5px 1px rgba(0,0,0,0.1);
        }

        .project-section li:before {
            content: "•";
            color: #4B0082;
            font-weight: bold;
            position: absolute;
            left: 0;
        }

        .project-section p {
            line-height: 1.8;
            color: #2C3E50;
            margin: 15px 0;
            text-shadow: 0.5px 0.5px 1px rgba(0,0,0,0.1);
        }
        </style>
        <div class="gradient-bar">
            <div class="gradient-text">What I have Experienced?</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("## Professional Experience")
    
    st.markdown("""
        <div class="experience-section">
        <h3>Western Advantage Capital Investment Company</h3>
        <strong>Intern</strong> | <em>November 2023 - February 2024</em>
        
        - Participated in the daily accounting work of more than 20 funds, including preparing the account voucher in fourth quarter of 2023, sorting and checking the bank receipts, and drafting business agreements and other contracts.  
        - Encoded the accounts of a fund for 6 years into system, including processing 500+ voucher information and assisting in transition for the accounting software of the fund. 
        - Assisted in the year-end accounting work and annual statement, including handling the work papers of internal controls in 2023, fixed asset inventory charts, low-value consumables charts, etc. of the 3 branches of the investment company to verify and rectify records; participated in the business operation budget statement in 2024.
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="experience-section">
        <h3>Yanchang Petroleum Sale Company</h3>
        <strong>Intern</strong> | <em>January 2021 - April 2021</em>
        
        - Assisted the budget management team in processing funding applications and working capital requests from 4 subsidiaries and 5 affiliated companies. 
        - Helped to produce the company's 2021 comprehensive budget management manual, including verifying budget amounts and digital indicators for each subsidiary. 
        - Organized thousands of sales data for the first quarter, completed the economic analysis(e.g.expense statistics and economic indicator calculations), and created visualized charts and table to analyze business operations.
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="experience-section">
        <h3>Da Hua CPAs LLP. Shaanxi Branch</h3>
        <strong>Intern</strong> | <em>June 2019 - August 2019</em>
        
        - Collected and organized organizational structure information of the audited entities, verified the amounts of more than 20 financial statement items, including fund management, detailed receivables, and internal cash flow details. 
        - Assisted in preparing interim notes for the financial statements. 
        - Participated in mid-term audit work, inputted and verified the financial statement amounts of 12 subsidiaries and 19 construction projects of the audited entities. Utilized Excel and financial software for data processing.
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("## Projects and Business Competition")
    
    # 添加expander样式
    st.markdown("""
        <style>
        div[data-testid="stExpander"] {
            background-color: #F8F9FA;
            border-radius: 10px;
            border: 1px solid #E9ECEF;
            margin: 10px 0;
        }
        
        div[data-testid="stExpander"] > div {
            padding: 15px;
        }
        
        div[data-testid="stExpander"] > div > div {
            font-size: 1.1rem !important;
            color: #4B0082 !important;
            font-weight: 600 !important;
        }
        
        div[data-testid="stExpander"] > div > div > div {
            font-size: 1rem !important;
            color: #2C3E50 !important;
            line-height: 1.6 !important;
        }
        
        div[data-testid="stExpander"] > div > div > div > p {
            margin: 8px 0 !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    projects = [
        {
            "title": "College of Materials Science, Petroleum Anti-Corrosion Innovation Project",
            "description": "Conducted in-depth research on the petroleum industry through interview with industry professionals). Determined market positioning and conducted product life-cycle analysis. Assessed potential risks associated with the market entry of the technology and proposed corresponding measures to mitigate those risks.",
            "skills": ["SWOT-analysis", "PEST-analysis"],
            "outcome": "The project won the Excellence Award at the 6th Energy Technology Competition of Xiamen University."
        },
        {
            "title": "P&G CEO Challenge",
            "description": "Led a team to design a marketing plan for a skincare brand that had just entered the Chinese market. ",
            "skills": ["Python"],
            "outcome": "Analyzed and interpreted the user's discussion trends and generated a camapign for the brand. "
        }
    ]
    
    for i, project in enumerate(projects):
        with st.expander(f"{project['title']}", expanded=i==0):
            st.markdown(f"**Description:** {project['description']}")
            st.markdown(f"**Skills Used:** {', '.join(project['skills'])}")
            st.markdown(f"**Outcome:** {project['outcome']}")
    
    st.markdown("---")
    
    st.markdown("## Project Gallery")
    
    # 添加项目图片展示区样式
    st.markdown("""
        <style>
        .gallery-container {
            display: flex !important;
            flex-direction: row !important;
            flex-wrap: wrap !important;
            gap: 20px !important;
            padding: 20px 0 !important;
            justify-content: flex-start !important;
            align-items: flex-start !important;
            width: 100% !important;
            margin: 0 !important;
        }
        .gallery-item {
            flex: 0 0 calc(25% - 20px) !important;
            transition: transform 0.3s ease, box-shadow 0.3s ease !important;
            position: relative !important;
            display: flex !important;
            justify-content: flex-start !important;
            align-items: flex-start !important;
            margin: 0 !important;
        }
        .gallery-item:hover {
            transform: translateY(-5px) !important;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2) !important;
        }
        .gallery-item img {
            width: auto !important;
            height: auto !important;
            max-width: 400px !important;
            max-height: 600px !important;
            border-radius: 15px !important;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1) !important;
            transition: all 0.3s ease !important;
            object-fit: contain !important;
            margin: 0 !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # 创建项目图片展示区
    st.markdown('<div class="gallery-container">', unsafe_allow_html=True)
    
    # 加载项目图片
    project_images = [
        "static/images/PG1.png",
        "static/images/PG2.png",
        "static/images/PG3.png"
    ]
    
    for img_name in project_images:
        if os.path.exists(img_name):
            image = Image.open(img_name)
            st.markdown(f'<div class="gallery-item"><img src="data:image/png;base64,{get_image_base64(img_name)}" alt="{img_name}"></div>', unsafe_allow_html=True)
        else:
            st.warning(f"Image {img_name} not found")
    
    st.markdown('</div></div></div>', unsafe_allow_html=True)  # 关闭所有容器
    
    
    
    
    