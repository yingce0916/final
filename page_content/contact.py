import streamlit as st

def contact_page():
    st.markdown("""
        <style>
        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        .gradient-bar {
            background: linear-gradient(45deg, #fcf2eb, #ffb9b3, #9f97cb);
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

        .contact-section {
            background: linear-gradient(45deg, rgba(252, 242, 235, 0.3), rgba(255, 185, 179, 0.3), rgba(159, 151, 203, 0.3));
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
            backdrop-filter: blur(5px);
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }
        </style>
        <div class="gradient-bar">
            <div class="gradient-text">Get in Touch</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("## Contact Me")
    
    # Contact Information
    st.markdown("""
    <div class="contact-section">
        <h3>Direct Contact</h3>
        <ul>
            <li><strong>Email</strong>: <a href="mailto:chencongxuan@163.com">chencongxuan@163.com</a></li>
            <li><strong>Phone</strong>: (86) 187-0683-3143/(852)9792-7808</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Office Hours
    st.markdown("""
    ### Office Hours
    I'm always here and waiting for your message!
    """)
    
    st.markdown("### Send Me a Message")
    
    with st.form("contact_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Name")
            email = st.text_input("Email")
            
        with col2:
            subject = st.text_input("Subject")
            
        message = st.text_area("Message", height=150)
        
        submitted = st.form_submit_button("Send Message")
        
        if submitted:
            st.success("Thanks for your message! I'll get back to you soon.")
            # In a real application, you would process the form data here
            # For example, send an email or store in a database
    
    st.markdown("---")
