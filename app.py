import streamlit as st
import pandas as pd
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("Chat with Your Data")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file:
    bytes_data = uploaded_file.getvalue()
    import io
    df = pd.read_csv(io.BytesIO(bytes_data))
    st.success("File uploaded successfully!")
    st.dataframe(df.head())

    question = st.chat_input("Ask anything about your data...")

    if question:
        with st.chat_message("user"):
            st.write(question)
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": f"You are a data analyst. Columns: {list(df.columns)}. Stats: {df.describe().to_string()}. First rows: {df.head().to_string()}. Answer clearly."},
                        {"role": "user", "content": question}
                    ],
                    temperature=0.3
                )
            st.write(response.choices[0].message.content)
else:
    st.info("Upload a CSV file to get started!")
