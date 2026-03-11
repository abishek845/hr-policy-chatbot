# app.py - Streamlit Chat Interface

import streamlit as st
from chatbot import ask_bot

# Page config
st.set_page_config(page_title="HR Policy Bot", page_icon="🤖")

# Title
st.title("🤖 HR Policy Assistant")
st.caption("Ask me anything about company policies!")

# 👇 ADD YOUR BRANDING HERE 👇
st.markdown("---")
st.caption("👨‍💻 **Built by Abishek Pandian** | GitHub: [@abishek845](https://github.com/abishek845)")
st.markdown("---")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask about leave, WFH, salary, onboarding..."):
    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = ask_bot(prompt)
            st.markdown(response)
    
    # Save assistant message
    st.session_state.messages.append({"role": "assistant", "content": response})

# 👇 ADD FOOTER AT BOTTOM 👇
st.markdown("---")
st.caption("🔗 Source Code: [GitHub](https://github.com/abishek845/hr-policy-chatbot)")