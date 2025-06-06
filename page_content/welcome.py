import streamlit as st
import os
from PIL import Image

def welcome_page():
    st.markdown("""
        <style>
        /* Remove top spacing */
        .main > div:first-child {
            padding-top: 0 !important;
            margin-top: 0 !important;
        }
        
        .welcome-container {
            text-align: center;
            padding: 2rem;
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.9), rgba(255, 255, 255, 0.8));
            border-radius: 15px;
            margin: 2rem 0;
        }
        
        .welcome-text {
            text-align: left;
            margin: 0;
            padding: 2rem;
            background: linear-gradient(135deg, rgba(205, 183, 247, 0.1), rgba(75, 0, 130, 0.1));
            border-radius: 15px;
            box-shadow: 0 8px 32px rgba(31, 38, 135, 0.1);
            backdrop-filter: blur(4px);
            border: 1px solid rgba(255, 255, 255, 0.18);
        }
        
        .greeting {
            background: linear-gradient(45deg, #4B0082, #cdb7f7);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 3rem;
            font-weight: 800;
            margin-bottom: 1rem;
            animation: fadeIn 1s ease-in;
        }
        
        .name {
            color: #4B0082;
            font-size: 2.8rem;
            font-weight: 700;
            margin: 1rem 0;
            animation: slideIn 1s ease-out;
        }
        
        .description {
            color: #666;
            font-size: 1.5rem;
            line-height: 1.6;
            margin: 1rem 0;
            animation: fadeIn 1.5s ease-in;
        }
        
        .highlight {
            color: #4B0082;
            font-weight: 600;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        
        @keyframes slideIn {
            from { transform: translateX(-50px); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
        
        .image-container {
            text-align: right;
        }
        
        .image-container img {
            max-width: 80%;
            height: auto;
            border-radius: 10px;
            box-shadow: 0 8px 32px rgba(31, 38, 135, 0.15);
            transition: transform 0.3s ease;
            margin: 0 auto;
            display: block;
        }
        
        .image-container img:hover {
            transform: scale(1.02);
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Create two columns with 2:1 ratio
    col1, col2 = st.columns([2, 1])
    
    # Left column for text
    with col1:
        st.markdown("""
            <div class="welcome-text">
                <div class="greeting">Hi! Nice to meet you!</div>
                <div class="name">I'm CHEN Congxuan!</div>
                <div class="description">
                    I'm a student who graduated from <span class="highlight">Xiamen university</span> and now study in <span class="highlight">CUHK</span>.<br>
                    I'm ready to start my career life and demonstrate my talent!<br>
                    I'm an <span class="highlight">extroverted</span> person with <span class="highlight">creative talent</span> and <span class="highlight">sense of humor</span>.
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    # Right column for image
    with col2:
        image_path = os.path.join("static", "images", "ccx.jpg")
        if os.path.exists(image_path):
            image = Image.open(image_path)
            st.image(image, width=300)
        else:
            st.warning("Profile image not found")
    
    
    