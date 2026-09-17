import streamlit as st
from agent import ask_question


st.set_page_config(
    page_title="Agentic RAG Assistant",page_icon="🤖")

st.title("🤖 Agentic RAG Assistant")
st.caption("RAG + Gemini + Conversation History | Ask me anything about your file.")
st.info("""
  **Example questions**

• What is overfitting?  
• What is cross-validation?  
• What is a neural network?  
• What is RAG?  
• What is an embedding?  
• How can overfitting be reduced?
""")


if "messages" not in st.session_state:
    st.session_state.messages = []

if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if (message["role"] == "assistant"
            and message.get("sources")):
            with st.expander("📚 Sources"):

                for source in message["sources"]:
                    st.write(f"- {source}")


question = st.chat_input("Ask a question...")

if question:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question })

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer, sources = ask_question(question)

        st.markdown(answer)
        if sources:
            with st.expander("📚 Sources"):
                for source in dict.fromkeys(sources):
                    st.write(f"- {source}")


    st.session_state.messages.append(
         {  "role": "assistant",
            "content": answer,
            "sources": sources})
