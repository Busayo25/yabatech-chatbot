import streamlit as st
from chat_engine import get_response
from feedback_handler import save_feedback

# Configure page
st.set_page_config(
    page_title="YabaTech Assistant",
    page_icon="🎓",
    layout="wide"
)

# Load images (now in root folder)
st.sidebar.image("yabatech_logo.png", width=150)
st.image("banner.jpg", use_column_width=True)

# Chat interface
st.title("🎓 YabaTech Student Assistant")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask about YabaTech..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Generate response (using transformer)
    response = get_response(prompt)
    
    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(response)
    
    # Add to history
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Save for feedback
    save_feedback(prompt, response)

# Feedback buttons
if st.session_state.messages:
    col1, col2 = st.columns(2)
    with col1:
        if st.button("👍 Helpful"):
            save_feedback(st.session_state.messages[-2]["content"], 
                        st.session_state.messages[-1]["content"], 
                        rating=1)
            st.success("Thanks for your feedback!")
    with col2:
        if st.button("👎 Needs Improvement"):
            save_feedback(st.session_state.messages[-2]["content"],
                        st.session_state.messages[-1]["content"],
                        rating=0)
            st.warning("We'll improve this!")
