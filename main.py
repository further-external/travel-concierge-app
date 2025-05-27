import streamlit as st
import gemini

st.set_page_config(page_title="Travel Concierge App")
st.title("Travel Concierge App")

with st.sidebar:
    st.markdown("""
    Plan your trip in detail! Here are a few example requests you can try:
    
    - Plan my trip to Paris.
    - Plan a trip to Japan for 2 adults, 7 days, relaxed, mid-range price.
    - Find cheapest direct one way flight for 2 adults from London to Paris on June 1st
    
    Just type your travel request in the chat box below.
    """)

    if st.button("Start New Chat", type="primary"):
        del st.session_state.session
    
    
if "session" not in st.session_state:
    chat_session = gemini.start_chat_session()
    st.session_state.session = {
        "chat": chat_session,
        "messages": []
    }

# Display chat history
for msg in st.session_state.session["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
prompt = st.chat_input("Where do you wan to go?")

if prompt:
    # Save user message
    st.session_state.session["messages"].append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    response = st.session_state.session["chat"].send_message(prompt)
    with st.chat_message("assistant"):
        st.markdown(response.text)
    
    st.session_state.session["messages"].append({"role": "assistant", "content": response.text})