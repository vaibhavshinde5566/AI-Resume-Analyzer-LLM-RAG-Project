import streamlit as st
from pdf_loader import load_pdf
from vector_store import create_vector_store
from rag_pipeline import ask_resume
import time

st.set_page_config(page_title="ResumeAI Pro", layout="wide", page_icon="✨")

# Custom CSS for a beautiful, colorful UI
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: #ffffff;
    }
    
    /* Header styling */
    h1 {
        background: -webkit-linear-gradient(45deg, #00C9FF, #92FE9D);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 3.5rem !important;
        text-align: center;
        padding-bottom: 20px;
    }
    
    h2, h3 {
        color: #00C9FF !important;
    }
    
    /* Subtitle styling */
    .subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #e0e0e0;
        margin-bottom: 30px;
    }
    
    /* Upload container styling */
    .stFileUploader {
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 20px;
        border: 2px dashed #00C9FF;
    }
    
    /* Input field styling */
    .stTextInput > div > div > input {
        background-color: rgba(255, 255, 255, 0.1);
        color: white;
        border-radius: 10px;
        border: 1px solid #92FE9D;
        padding: 10px 15px;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(45deg, #00C9FF, #92FE9D);
        color: #0f2027;
        border: none;
        border-radius: 25px;
        padding: 10px 25px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0, 201, 255, 0.4);
    }
    
    /* Answer box styling */
    .answer-box {
        background-color: rgba(0, 201, 255, 0.1);
        border-left: 5px solid #92FE9D;
        padding: 20px;
        border-radius: 0 10px 10px 0;
        margin-top: 20px;
    }
    
    /* Sidebar text color fix */
    .css-1d391kg, .css-1dp5vir {
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("<h1>✨ AI Resume Analyzer Pro</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Unlock the power of your resume with AI! Upload your document and ask our intelligent assistant anything.</p>", unsafe_allow_html=True)

# Layout: Split into two columns for a better look
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("### 📤 Upload Document")
    uploaded_file = st.file_uploader("Drop your PDF resume here", type="pdf")
    
    if uploaded_file:
        with st.spinner("Processing your resume..."):
            # Save file temporarily
            with open("temp_resume.pdf", "wb") as f:
                f.write(uploaded_file.read())
            
            # Load & process
            docs = load_pdf()
            st.session_state['vectorstore'] = create_vector_store(docs)
            st.session_state['file_uploaded'] = True
            
        st.success("✅ Resume processed and ready! Ask me anything on the right.")
        
with col2:
    st.markdown("### 💬 Ask the AI")
    
    if st.session_state.get('file_uploaded', False):
        query = st.text_input("What would you like to know about this resume?", placeholder="E.g., What are the key skills highlighted?")
        
        if query:
            with st.spinner("Analyzing..."):
                answer = ask_resume(st.session_state['vectorstore'], query)
                
            st.markdown("### 📌 Insights:")
            st.markdown(f"<div class='answer-box'>{answer}</div>", unsafe_allow_html=True)
    else:
        st.info("👋 Please upload a resume first to start asking questions.")
        
# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #666;'>Powered by GenAI and Agentic AI 🚀</p>", unsafe_allow_html=True)
