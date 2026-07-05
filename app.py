import streamlit as st
import plotly.graph_objects as go
import time

from backend.pdf_utils import extract_text_from_pdf
from backend.summarizer import summarize_document
from backend.chatbot import ask_question
from backend.clause_detector import detect_clauses
from backend.risk_detector import calculate_risk
from backend.report_generator import generate_report
from backend.translator import translate_text


# -----------------------------
# Page Configuration
# -----------------------------
# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Lexora AI",
    page_icon="assets/favicon.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

/* ==========================================================
   LEXORA AI UI
========================================================== */

:root{
    --accent:#2563EB;
    --border:#CBD5E1;
}

/* Main Layout */

.block-container{
    max-width:1200px;
    padding-top:5rem;
    padding-bottom:2rem;
    padding-left:2rem;
    padding-right:2rem;
}

/* Sidebar */

section[data-testid="stSidebar"]{
    border-right:2px solid var(--accent);
}

/* Headings */

h1,h2,h3,h4{
    font-weight:700;
}

/* Metric Cards */

div[data-testid="metric-container"]{
    border:1px solid var(--border);
    border-radius:14px;
    padding:18px;
    box-shadow:0 2px 8px rgba(0,0,0,.06);
    transition:0.2s ease;
}

div[data-testid="metric-container"]:hover{
    border-color:var(--accent);
    transform:translateY(-2px);
}

/* Metric Font Sizes */

div[data-testid="metric-container"] label{
    font-size:14px !important;
    font-weight:600 !important;
}

div[data-testid="stMetricValue"]{
    font-size:28px !important;
    font-weight:700 !important;
}

/* Buttons */

.stButton > button{
    width:100%;
    height:46px;
    border-radius:10px;
    font-weight:600;
}

/* File Uploader */

[data-testid="stFileUploader"]{
    border:2px dashed var(--accent);
    border-radius:16px;
    padding:18px;
}

/* Tabs */

button[data-baseweb="tab"]{
    font-weight:600;
    border-radius:10px;
}

button[data-baseweb="tab"][aria-selected="true"]{
    border-bottom:3px solid var(--accent);
}

/* Expander */

details{
    border-radius:12px;
}

/* Progress Bar */

.stProgress > div > div > div{
    background:var(--accent);
}

/* Clause Cards */

.clause-card{
    border-left:5px solid var(--accent);
    border-radius:12px;
    padding:16px;
    margin-bottom:12px;
    box-shadow:0 2px 8px rgba(0,0,0,.05);
}

/* Images */

img{
    border-radius:10px;
}

/* Footer */

.footer{
    text-align:center;
    opacity:.75;
    padding:20px;
}

</style>
""", unsafe_allow_html=True)
# ==========================================================
# SESSION STATE
# ==========================================================

if "summary" not in st.session_state:
    st.session_state.summary = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "last_file" not in st.session_state:
    st.session_state.last_file = None
# ==========================================================
# RISK GAUGE
# ==========================================================

def create_risk_gauge(score):

    if score >= 75:
        color = "#DC2626"
        level = "High Risk"

    elif score >= 50:
        color = "#F59E0B"
        level = "Medium Risk"

    else:
        color = "#16A34A"
        level = "Low Risk"

    fig = go.Figure(go.Indicator(

        mode="gauge+number",

        value=score,

        number={
            "suffix": "/100",
            "font":{
                "size":28
            }
        },

        title={
            "text":level,
            "font":{
                "size":16
            }
        },

        gauge={

            "shape":"angular",

            "axis":{
                "range":[0,100],
                "tickwidth":1
            },

            "bar":{
                "color":color,
                "thickness":0.25
            },

            "bgcolor":"rgba(0,0,0,0)",

            "borderwidth":0,

            "steps":[
                {"range":[0,40],"color":"#D1FAE5"},
                {"range":[40,70],"color":"#FEF3C7"},
                {"range":[70,100],"color":"#FEE2E2"},
            ],

            "threshold":{

                "line":{
                    "color":"#1E293B",
                    "width":4
                },

                "thickness":0.8,

                "value":score

            }

        }

    ))

    fig.update_layout(

        height=240,

        margin=dict(
            l=15,
            r=15,
            t=35,
            b=5
        ),

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(size=14)

    )

    return fig


# ==========================================================
# HEADER
# ==========================================================

header_left, header_right = st.columns([5,2])

with header_left:

    logo_col, text_col = st.columns([1,6])

    with logo_col:
        st.image("assets/logo.png", width=90)

    with text_col:

        st.markdown("""
<h2 style="margin-bottom:0;">
Lexora AI
</h2>
""", unsafe_allow_html=True)

        st.caption(
            "AI-Powered Legal Document Intelligence"
        )

with header_right:

    language_options = {
        "English": "English",
        "తెలుగు": "Telugu",
        "ಕನ್ನಡ": "Kannada",
        "हिन्दी": "Hindi",
        "தமிழ்": "Tamil"
    }

    selected_language = st.selectbox(
        "🌐 Language",
        list(language_options.keys())
    )

language = language_options[selected_language]

st.divider()
# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.image("assets/logo.png", width=90)

    st.title("Lexora AI")

    st.caption("Legal Intelligence Platform")

    st.divider()

    st.markdown("### Features")

    st.markdown("""
    - 📝 AI Summary
    - ⚠️ Risk Assessment
    - 📑 Clause Detection
    - 🌍 Translation
    - 🤖 AI Assistant
    - 📄 PDF Report
    """)

    st.divider()

    st.caption("Version 1.0")


# ==========================================================
# UPLOAD DOCUMENT
# ==========================================================

st.subheader("📄 Upload Legal Document")

st.caption(
    "Supported: Employment Agreement • NDA • Rental Agreement • Service Agreement • Offer Letter"
)

uploaded_file = st.file_uploader(
    "Choose a PDF",
    type=["pdf"],
    help="Upload a legal agreement in PDF format."
)
# ==========================================================
# PROCESS DOCUMENT
# ==========================================================
if uploaded_file is not None:
    if st.session_state.last_file != uploaded_file.name:
        st.session_state.summary = None
        st.session_state.chat_history = []
        st.session_state.last_file = uploaded_file.name

    start_time = time.time()

    with st.spinner("📄 Analyzing legal document..."):

        extracted_text = extract_text_from_pdf(uploaded_file)

        clauses = detect_clauses(extracted_text)

        risk_score, risk_level = calculate_risk(clauses)

        clauses_count = len(clauses)

    processing_time = round(time.time() - start_time, 2)

    word_count = len(extracted_text.split())

    file_size = uploaded_file.size / 1024

    # ======================================================
    # DASHBOARD
    # ======================================================

    dashboard_left, dashboard_right = st.columns([2,1])

    with dashboard_left:

        m1, m2, m3, m4 = st.columns(4)

        with m1:
            st.metric(
                "⚠ Risk",
                risk_level
            )

        with m2:
            st.metric(
                "📑 Clauses",
                clauses_count
            )

        with m3:
            st.metric(
                "🌐 Language",
                selected_language
            )

        with m4:
            st.metric(
                "📄 Status",
                "Ready"
            )

    with dashboard_right:

        st.plotly_chart(
            create_risk_gauge(risk_score),
            use_container_width=True,
            config={
                "displayModeBar": False
            }
        )

    st.success(
        f"✅ Analysis completed in {processing_time:.2f} seconds."
    )

    # ======================================================
    # DOCUMENT INFORMATION
    # ======================================================

    st.subheader("📄 Document Information")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Size",
        f"{file_size:.1f} KB"
    )

    c2.metric(
        "Words",
        word_count
    )

    c3.metric(
        "Clauses",
        clauses_count
    )

    c4.metric(
        "Time",
        f"{processing_time:.2f}s"
    )

    with st.expander("📖 Preview Extracted Text"):

        st.text_area(
            "Document",
            extracted_text[:1500],
            height=350,
            disabled=True
        )

    tab1, tab2, tab3, tab4 = st.tabs([
        "📝 Summary",
        "⚠️ Risks",
        "📑 Clauses",
        "🤖 Assistant"
    ])
    # ==========================================================
    # SUMMARY TAB
    # ==========================================================

    with tab1:

        st.subheader("📝 AI Executive Summary")

        st.caption(
            "Generate a concise summary of the uploaded legal document."
        )

        if st.button(
            "✨ Generate Summary",
            use_container_width=True
        ):

            with st.spinner("🤖 Generating AI summary..."):

                try:

                    st.session_state.summary = summarize_document(
                        extracted_text
                    )

                    st.success("Summary Ready")

                except Exception:

                    st.error(
                        "AI service is temporarily unavailable. Please try again later."
                    )

        if st.session_state.summary:

            st.markdown("### Summary")

            st.info(st.session_state.summary)

            # --------------------------------------------------
            # Translation
            # --------------------------------------------------

            if selected_language != "English":

                st.markdown("### 🌍 Translated Summary")

                with st.spinner("Translating document..."):

                    try:

                        translated = translate_text(
                            st.session_state.summary,
                            language
                        )

                        st.success(translated)

                    except Exception:

                        st.warning(
                            "Translation service is temporarily unavailable."
                        )

            # --------------------------------------------------
            # Download Report
            # --------------------------------------------------

            generate_report(
                "reports/LexoraAI_Report.pdf",
                st.session_state.summary,
                clauses,
                risk_score,
                risk_level
            )

            st.markdown("### 📥 Export Analysis")

            with open(
                "reports/LexoraAI_Report.pdf",
                "rb"
            ) as pdf:

                st.download_button(
                    "📄 Download PDF Report",
                    pdf,
                    file_name="LexoraAI_Report.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )


    # ==========================================================
    # RISK ANALYSIS TAB
    # ==========================================================

    with tab2:

        st.subheader("⚖️ Legal Risk Assessment")

        st.metric(
            "Overall Risk",
            risk_level,
            f"{risk_score}/100"
        )

        st.caption(
            "The following clauses contributed to the calculated legal risk score."
        )

        risk_details = {

            "Non-Compete": (
                "High",
                "Restricts future employment with competing organizations after resignation."
            ),

            "Liability": (
                "Medium",
                "Employee may be financially responsible for losses caused by intentional misconduct."
            ),

            "Confidentiality": (
                "Low",
                "Employee must protect confidential company information."
            ),

            "Arbitration": (
                "Low",
                "Disputes will be resolved through arbitration instead of court proceedings."
            )
        }

        severity_color = {
            "High": "#DC2626",
            "Medium": "#F59E0B",
            "Low": "#16A34A"
        }

        detected = False

        for clause in clauses:

            if clause in risk_details:

                detected = True

                severity, description = risk_details[clause]

                st.markdown(
                    f"""
    <div style="
    padding:18px;
    margin-bottom:14px;
    border-left:6px solid {severity_color[severity]};
    border-radius:12px;
    box-shadow:0 2px 6px rgba(0,0,0,.05);
    ">

    <h4 style="margin-bottom:6px;">
    📌 {clause}
    </h4>

    <b>Severity:</b> {severity}

    <br><br>

    {description}

    </div>
    """,
                    unsafe_allow_html=True
                )

        if not detected:

            st.success(
                "✅ No significant legal risk factors were detected."
            )

        st.markdown("### 💡 Recommendation")

        if risk_score >= 75:

            st.error(
                "This agreement contains several high-risk clauses. Consider reviewing it with a legal professional before signing."
            )

        elif risk_score >= 50:

            st.warning(
                "This agreement contains moderate legal risks. Review the highlighted clauses carefully."
            )

        else:

            st.success(
                "This agreement appears to have relatively low legal risk. Continue reviewing the document before signing."
            )
    # ==========================================================
    # CLAUSES TAB
    # ==========================================================

    with tab3:

        st.subheader("📑 Detected Legal Clauses")

        st.caption(
            "The following clauses were identified in the uploaded legal document."
        )

        clause_info = {

            "Salary": (
                "💰",
                "Defines employee compensation, salary structure and payment schedule."
            ),

            "Termination": (
                "❌",
                "Specifies conditions under which employment may be terminated."
            ),

            "Confidentiality": (
                "🔒",
                "Protects confidential business information and trade secrets."
            ),

            "Non-Compete": (
                "🚫",
                "Restricts employment with competing organizations after resignation."
            ),

            "Liability": (
                "⚖️",
                "Defines legal responsibilities and financial liabilities."
            ),

            "Arbitration": (
                "🏛️",
                "Disputes will be resolved through arbitration instead of court."
            ),

            "Leave Policy": (
                "🏖️",
                "Explains employee leave entitlement and company holidays."
            ),

            "Working Hours": (
                "🕘",
                "Specifies working schedule and office hours."
            )

        }

        if clauses:

            cols = st.columns(2)

            for index, clause in enumerate(clauses):

                icon, description = clause_info.get(
                    clause,
                    ("📄", "Legal clause detected.")
                )

                with cols[index % 2]:

                    st.markdown(
                        f"""
    <div class="clause-card">

    <h4>{icon} {clause}</h4>

    <p>{description}</p>

    </div>
    """,
                        unsafe_allow_html=True
                    )

        else:

            st.info(
                "No important legal clauses were detected."
            )

    # ==========================================================
    # AI ASSISTANT TAB
    # ==========================================================

    with tab4:

        st.subheader("🤖 AI Legal Assistant")

        st.caption(
            "Ask questions about your uploaded legal document."
        )

        with st.expander("💡 Suggested Questions"):

            st.markdown("""
                - Explain the Non-Compete clause.
                - Summarize the termination clause.
                - What legal risks exist?
                - Explain the confidentiality clause.
                - What is the notice period?
                - Translate the summary into Hindi.
                """)

        question = st.text_input(
            "Ask a question",
            placeholder="Example: Explain the Non-Compete clause"
        )

        ask_ai = st.button(
            "🤖 Ask Lexora AI",
            use_container_width=True
        )

        if ask_ai:

            if not question.strip():

                st.warning("Please enter a question.")

            else:

                with st.spinner("🤖 Thinking..."):

                    try:

                        answer = ask_question(
                            extracted_text,
                            question
                        )

                    except Exception:

                        answer = (
                            "⚠️ AI service is currently unavailable.\n\n"
                            "Please try again later."
                        )

                st.session_state.chat_history.append(
                    ("You", question)
                )

                st.session_state.chat_history.append(
                    ("Lexora AI", answer)
                )

        if st.session_state.chat_history:

            st.markdown("### Conversation")

            for sender, message in st.session_state.chat_history:

                with st.chat_message(
                    "user" if sender == "You" else "assistant"
                ):
                    st.write(message)


# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.caption(
    "Lexora AI • AI-Powered Legal Document Intelligence • Built with Python, Streamlit, Google Gemini & Plotly"
)

st.caption("© 2026 Likitha A")