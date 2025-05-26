import streamlit as st

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("Travel Concierge App")

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
prompt = st.chat_input("Say something...")

if prompt:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant response (basic echo bot here)
    response = f"You said: {prompt}"
    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.markdown(response)