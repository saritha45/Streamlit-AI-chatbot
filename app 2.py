import streamlit as st
st.title("my AI chatbot")
question=st.text_input("Ask something:")
if st.button("send"):
    if question:
        st.success("your question submitted!")
        st.write(question)
    else:
        st.error("Error! please enter your question")