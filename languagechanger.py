import streamlit as st
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema.runnable import Runnable
from langchain_core.messages import HumanMessage, SystemMessage

# --- Set Gemini API Key directly here ---
GOOGLE_API_KEY = "YOUR_API_KEY_HERE"  # 🔒 Replace with your actual key

# --- Streamlit Page Config ---
st.set_page_config(page_title="English to French Translator", layout="centered")
st.title("🌍 English to French Translator")
st.markdown("Translate any English sentence into French using Gemini + LangChain.")

# --- Input from user ---
english_sentence = st.text_input("📝 Enter English sentence:", "")

# --- Translate Button ---
if st.button("Translate to French"):

    if not english_sentence.strip():
        st.warning("Please enter a sentence to translate.")
    else:
        try:
            # --- Initialize Gemini Model (Free Tier) ---
            llm = ChatGoogleGenerativeAI(
                model="models/chat-bison-001",  # ✅ Free-supported model
                google_api_key=GOOGLE_API_KEY,
                temperature=0.3,
            )

            # --- Define Prompt Template ---
            prompt = ChatPromptTemplate.from_messages([
                SystemMessage(content="You are a translation assistant. Translate any English sentence to French."),
                HumanMessage(content="{sentence}")
            ])

            # --- Chain ---
            chain: Runnable = prompt | llm

            # --- Run chain with input ---
            response = chain.invoke({"sentence": english_sentence})

            # --- Output ---
            st.success("✅ Successfully translated!")
            st.markdown("**🇫🇷 French Translation:**")
            st.write(response.content)

        except Exception as e:
            st.error(f"❌ Error dur
