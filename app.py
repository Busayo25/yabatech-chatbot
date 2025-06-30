import streamlit as st
from utils.feedback_handler import initialize_feedback_file

# Initialize feedback system
initialize_feedback_file()



st.set_page_config(
    st.sidebar.image("assets/yabatech_logo.png", width=120)
    st.image("assets/banner.jpg", use_column_width=True)
    page_title="YabaTech Assistant",
    page_icon="🎓",
    layout="wide",
    menu_items={
        'About': "YabaTech Student Chatbot v1.0"
    }
)

st.title("🎓 Yaba College of Technology")
st.markdown("""
    **Navigate using the sidebar** to:
    - 💬 Chat with the assistant
    - 📊 View feedback analytics
    - ℹ️ Learn about this project
""")
