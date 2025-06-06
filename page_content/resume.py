import streamlit as st
import base64
import os
from PIL import Image

def resume_page():
    # Add custom CSS
    st.markdown("""
        <style>
        .contact-info {
            background: linear-gradient(45deg, #9ff2fc, #cdb7f7, #8579ec);
            padding: 20px;
            border-radius: 15px;
            margin: 20px 0;
        }
        .contact-info h3 {
            color: #4B0082;
            margin-bottom: 15px;
        }
        .contact-info p {
            margin: 10px 0;
            line-height: 1.6;
        }
        </style>
    """, unsafe_allow_html=True)

    pdf_file_path = os.path.join("static", "docs", "Chen Congxuan.pdf")

    if os.path.exists(pdf_file_path):
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        # Display the download button
        st.download_button(label="Download Resume",
                        data=PDFbyte,
                        file_name="CHEN_Congxuan_Resume.pdf",
                        mime='application/octet-stream')
    else:
        st.warning("Resume PDF file not found")

    st.title("Congxuan CHEN")

    # Create two columns
    left_col, right_col = st.columns(2)

    # Contact Information in left column
    left_col.markdown("""
    <div class="contact-info">
        <h3>Contact Information</h3>
        <p><strong>Email:</strong> chencongxuan@163.com</p>
        <p><strong>Phone:</strong> (86) 187-0683-3143/(852)9792-7808</p>
        <p><strong>Wechat:</strong> 18706833143</p>
        <p><strong>Address:</strong> City one - Shatin Block45</p>
    </div>
    """, unsafe_allow_html=True)

    # Profile image in right column
    image_path = os.path.join("static", "images", "image.jpg")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        right_col.image(image, width=200)
    else:
        right_col.warning("Profile image not found")

    st.markdown("---")

    st.header("Professional Summary")
    st.markdown("""
    Have a bachelor's degree in accounting and a master's degree in marketing.Have received well education and training in data analysis and insights generation. Expect to work as a marketing analyst in the marketing department of an FMCG or retail giant, focusing on digital marketing and brand management and dedicating myself to optimizing AI and algorithms to help better establish branding insights, gaining valuable insights into customer behaviour preferences and needs .
    """)

    # Add decorative gradient bar
    st.markdown("""
        <style>
        .decorative-bar {
            background: linear-gradient(45deg, #9ff2fc, #cdb7f7, #8579ec);
            height: 10px;
            width: 100%;
            margin: 20px 0;
            border-radius: 5px;
        }
        </style>
        <div class="decorative-bar"></div>
    """, unsafe_allow_html=True)

    st.header("Education")
    st.markdown("""
    **Master of Science in Marketing**
    - The Chinese University of Hong Kong
    - *Graduated:October 2025*
    """)
    st.markdown("""
    **Bachelor of Science in Accounting**
    - Xiamen University
    - *Graduated:June 2021*
    - GPA: 3.3/4.0
    """)
    
    # Add decorative gradient bar
    st.markdown('<div class="decorative-bar"></div>', unsafe_allow_html=True)
    
    st.header("Internship Experience")
    st.markdown("""
    **Western Advantage Capital Investment Company**
    - *11/2023-02/2024*
    - Participated in the daily accounting work of more than 20 funds, including preparing the account voucher in fourth quarter of 2023, sorting and checking the bank receipts, and drafting business agreements and other contracts.  
    - Encoded the accounts of a fund for 6 years into system, including processing 500+ voucher information and assisting in transition for the accounting software of the fund.  
    - Assisted in the year-end accounting work and annual statement, including handling the work papers of internal controls in 2023, fixed asset inventory charts, low-value consumables charts, etc. of the 3 branches of the investment company to verify and rectify records; participated in the business operation budget statement in 2024.

    **Yanchang Petroleum Sale Company**
    - *01/2021-04/2021*
    - Assisted the budget management team in processing funding applications and working capital requests from 4 subsidiaries and 5 affiliated companies. 
    - Helped to produce the company's 2021 comprehensive budget management manual, including verifying budget amounts and digital indicators for each subsidiary.  
    - Organized thousands of sales data for the first quarter, completed the economic analysis(e.g.expense statistics and economic indicator calculations), and created visualized charts and table to analyze business operations.
    
    **Da Hua CPAs LLP. Shaanxi Branch**
    - *06/2019-08/2019*
    - Collected and organized organizational structure information of the audited entities, verified the amounts of more than 20 financial statement items, including fund management, detailed receivables, and internal cash flow details. 
    - Assisted in preparing interim notes for the financial statements. Participated in mid-term audit work, inputted and verified the financial statement amounts of 12 subsidiaries and 19 construction projects of the audited entities. Utilized Excel and financial software for data processing.
    """)
    
    st.markdown('<div class="decorative-bar"></div>', unsafe_allow_html=True)

    st.header("Skills&Certifications")
    st.markdown("""
    - **IT skills:** Python, R, SPSS
    - **Databases:** MySQL
    - **Certificates:** : Computer Level 2 MS Office Advanced Application and Design Certificate (2020)
    """)
    
    st.markdown('<div class="decorative-bar"></div>', unsafe_allow_html=True)

    st.header("Projects&Campus Activity")
    st.markdown("""
    **College of Materials Science, Petroleum Anti-Corrosion Innovation Project**
    - Conducted in-depth research on the petroleum industry from multiple ways(e.g.interview industry professionals). Evaluated the feasibility and innovation of the project through market trend analysis and financial budget analysis.
    - Utilized multiple models such as PEST and SWOT frameworks, etc., to conduct the qualitative analysis. Determined market positioning and conducted product life-cycle analysis. 
    - Assessed potential risks associated with the market entry of the technology and proposed corresponding measures to mitigate those risks.  The project won the Excellence Award at the 6th Energy Technology Competition of Xiamen University.

    **Student Union, Department of Psychological Development, School of Management**
    - Led a team of 20 people to perceive students' psychological needs. Organized 7 mental health education events for the school, with 600 participants, reaching nearly 10,000 views on publicity notifications. 
    - Innovated the publicity approach through new media platforms by establishing a dedicated WeChat official account. Published promotional materials for each event, resulting in an 80% increase in event exposure and influence. Estimated the scale of student participation based on the number of views. 
    - Led the team to participate in the "Xiamen University Psychological Drama Competition" and won second place.
    """)
    
    st.markdown('<div class="decorative-bar"></div>', unsafe_allow_html=True)

    st.header("Languages")
    st.markdown("""
    - **Mandarin:** Native
    - **English:** Fluent, IELTS7.5 and 8.0 in spoken
    """)

    st.markdown("---") 