import streamlit as st
import pdfplumber
import nltk
import re
from sentence_transformers import SentenceTransformer

# ---------------------------
# Setup (run once)
# ---------------------------
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

st.set_page_config(page_title="AI Compliance System", layout="wide")

st.title("🧠 AI Compliance Intelligence System")

# ---------------------------
# Functions
# ---------------------------
def extract_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    return text

def split_sentences(text):
    return nltk.sent_tokenize(text)

def assign_risk(sentence):
    s = sentence.lower()

    # 🔴 HIGH RISK (strict / penalties / restrictions)
    if any(word in s for word in [
        "must not", "shall not", "prohibited", "penalty", "fine",
        "violation", "terminate", "suspend", "legal action"
    ]):
        return "High"

    # 🟡 MEDIUM RISK (obligations / requirements)
    elif any(word in s for word in [
        "must", "shall", "required", "responsible", "obligation",
        "agree", "ensure", "comply"
    ]):
        return "Medium"

    # 🟢 LOW RISK (informational)
    else:
        return "Low"

def explain(risk):
    if risk == "High":
        return "Contains restriction or penalty"
    elif risk == "Medium":
        return "Contains obligation"
    else:
        return "General statement"

# ---------------------------
# Load model (cached ⚡)
# ---------------------------
@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

model = load_model()

# ---------------------------
# Upload Section
# ---------------------------
uploaded_file = st.file_uploader("📂 Upload Policy PDF", type="pdf")

if uploaded_file:

    # Save temp file
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    # Process
    text = extract_text("temp.pdf")
    cleaned = clean_text(text)
    sentences = split_sentences(cleaned)

    embeddings = model.encode(sentences)

    # Build results
    results = []
    for s in sentences:
        risk = assign_risk(s)
        results.append({
            "sentence": s,
            "risk": risk,
            "reason": explain(risk)
        })

    # ---------------------------
    # Filter
    # ---------------------------
    st.subheader("📊 Compliance Analysis")

    risk_filter = st.selectbox(
        "Filter by Risk Level",
        ["All", "High", "Medium", "Low"]
    )

    # ---------------------------
    # Display
    # ---------------------------
    for r in results:

        if risk_filter != "All" and r["risk"] != risk_filter:
            continue

        # Color based on risk
        if r["risk"] == "High":
            st.error(f"📄 {r['sentence']}")
        elif r["risk"] == "Medium":
            st.warning(f"📄 {r['sentence']}")
        else:
            st.success(f"📄 {r['sentence']}")

        st.write(f"⚠️ Risk: {r['risk']}")
        st.write(f"💡 Reason: {r['reason']}")
        st.markdown("---")