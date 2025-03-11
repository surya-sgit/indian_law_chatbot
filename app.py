import streamlit as st
import requests

st.title("Legal Assistant Chatbot")
st.write("Ask me about Indian laws and legal matters.")

# Store chat messages in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Type your question here...")
if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    
    api_url = f"https://27f5-34-123-181-84.ngrok-free.app/predict/?query={user_input}"  # Replace with actual API URL

    # **✅ Synchronous request instead of `await requests.post()`**
    try:
        response = requests.post(api_url)
        response_data = response.json().get("prediction", "Sorry, I couldn't fetch a response.")
    except Exception as e:
        response_data = f"Error: {e}"

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(response_data)

    # Store response in session state
    st.session_state.messages.append({"role": "assistant", "content": response_data})
