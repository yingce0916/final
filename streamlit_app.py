import warnings
import streamlit as st

warnings.simplefilter(action="ignore", category=FutureWarning)

# Must be the first Streamlit command
st.set_page_config(page_title="personalsite", layout="wide")

# Import pages from the new directory
from page_content.welcome import welcome_page
from page_content.home import home_page
from page_content.experience import experience_page
from page_content.education import education_page
from page_content.resume import resume_page
from page_content.contact import contact_page

# Import components
from components.footer import display_footer
from components.styles import load_css

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):
        # Load custom CSS
        load_css()

        # Add custom CSS for fancy effects
        st.markdown("""
            <style>
            /* Sidebar styles */
            [data-testid="stSidebar"] {
                background-color: #cdb7f7 !important;
            }
            [data-testid="stSidebar"] h2 {
                color: #4B0082 !important;
                font-size: 1.5rem !important;
                font-weight: 600 !important;
                margin-bottom: 1rem !important;
            }

            /* Main content area styles */
            .main .block-container {
                background: linear-gradient(135deg, rgba(255, 255, 255, 0.9), rgba(255, 255, 255, 0.8));
                backdrop-filter: blur(10px);
                border-radius: 15px;
                padding: 2rem;
                box-shadow: 0 8px 32px rgba(31, 38, 135, 0.15);
                margin: 1rem;
            }

            /* Fancy hover effects for buttons */
            .stButton > button {
                transition: all 0.3s ease;
                border-radius: 10px;
                border: 2px solid #4B0082;
                background: linear-gradient(45deg, #4B0082, #cdb7f7);
                color: white;
            }
            .stButton > button:hover {
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(75, 0, 130, 0.3);
            }

            /* Fancy text styles */
            h1, h2, h3 {
                background: linear-gradient(45deg, #4B0082, #cdb7f7);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-weight: 700;
            }

            /* Fancy card effects */
            .stMarkdown:not(:has(hr)):not(:empty) {
                background: rgba(255, 255, 255, 0.7);
                border-radius: 10px;
                padding: 1rem;
                margin: 0.5rem 0;
                transition: all 0.3s ease;
            }
            .stMarkdown:not(:has(hr)):not(:empty):hover {
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            }

            /* Custom scrollbar */
            ::-webkit-scrollbar {
                width: 10px;
            }
            ::-webkit-scrollbar-track {
                background: #f1f1f1;
                border-radius: 5px;
            }
            ::-webkit-scrollbar-thumb {
                background: #cdb7f7;
                border-radius: 5px;
            }
            ::-webkit-scrollbar-thumb:hover {
                background: #4B0082;
            }
            </style>
        """, unsafe_allow_html=True)

        st.sidebar.markdown("## Main Menu")
        app = st.sidebar.radio(
            "Navigation", self.apps, format_func=lambda app: app["title"]
        )
        st.sidebar.markdown("---")

        app["function"]()
        
        # Display footer at the bottom of each page
        display_footer()

# Initialize the app
app = MultiApp()

# Add pages to the app
app.add_app("Welcome", welcome_page)
app.add_app("Home Page", home_page)
app.add_app("Education Page", education_page)
app.add_app("Experience Page", experience_page)
app.add_app("Resume Page", resume_page)
app.add_app("Contact Page", contact_page)

# Run the app
app.run()
