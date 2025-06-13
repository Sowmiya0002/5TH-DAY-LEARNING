import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable
from langchain_google_genai import ChatGoogleGenerativeAI

# --- SET GEMINI API KEY DIRECTLY ---
GOOGLE_API_KEY = "AIzaSyAPSM-tjDDFZcCploLoXiJ8MkjxAA5ukwk"  # Replace this with your real key

# --- STREAMLIT UI CONFIG ---
st.set_page_config(page_title="English to French Translator", layout="centered")
st.title("🌍 English to French Translator")
st.markdown("Translate any English sentence into French using Gemini + LangChain.")

# --- TEXT INPUT ---
sentence = st.text_input("📝 Enter English sentence:")

# --- TRANSLATE BUTTON ---
if st.button("Translate to French"):

    if not sentence.strip():
        st.warning("Please enter a sentence to translate.")
        st.stop()

    # --- Initialize Gemini Model ---
    try:
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",  # Free-tier friendly model
            google_api_key=GOOGLE_API_KEY,
            temperature=0.3
        )
    except Exception as e:
        st.error(f"❌ Failed to load Gemini model: {e}")
        st.stop()

    # --- Prompt Template ---
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant that translates English to French."),
        ("user", "Translate the following sentence to French: {text}")
    ])

    # --- Chain: prompt | llm ---
    chain: Runnable = prompt | llm

    # --- Run Chain ---
    try:
        response = chain.invoke({"text": sentence})
        french = response.content
        st.success("✅ Translation successful!")
        st.markdown(f"**French:** {french}")
    except Exception as e:
        st.error(f"❌ Error during translation: {e}")
