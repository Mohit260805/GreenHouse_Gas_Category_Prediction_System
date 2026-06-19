import streamlit as st
import joblib

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Green House Gas Predictor",
    page_icon="🌍",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------
model = joblib.load("model.pkl")

# ---------------- COUNTRY MAPPING ----------------
country_map = {
    'Australia':1, 'Austria':2, 'Belarus':3, 'Belgium':4, 'Bulgaria':5,
    'Canada':6, 'Croatia':7, 'Cyprus':8, 'Czech Republic':9, 'Denmark':10,
    'Estonia':11, 'European Union':12, 'Finland':13, 'France':14,
    'Germany':15, 'Greece':16, 'Hungary':17, 'Iceland':18, 'Ireland':19,
    'Italy':20, 'Japan':21, 'Latvia':22, 'Liechtenstein':23,
    'Lithuania':24, 'Luxembourg':25, 'Malta':26, 'Monaco':27,
    'Netherlands':28, 'New Zealand':29, 'Norway':30, 'Poland':31,
    'Portugal':32, 'Romania':33, 'Russian Federation':34, 'Slovakia':35,
    'Slovenia':36, 'Spain':37, 'Sweden':38, 'Switzerland':39,
    'Turkey':40, 'Ukraine':41, 'United Kingdom':42,
    'United States of America':43
}

# ---------------- CATEGORY LABELS ----------------
categories = {
    0: "CO₂ Emissions Without LULUCF",
    1: "GHG Emissions Including Indirect CO₂",
    2: "GHG Emissions Without LULUCF",
    3: "Hydrofluorocarbons (HFCs) Emissions",
    4: "Methane (CH₄) Emissions",
    5: "Nitrogen Trifluoride (NF₃) Emissions",
    6: "Nitrous Oxide (N₂O) Emissions",
    7: "Perfluorocarbons (PFCs) Emissions",
    8: "Sulphur Hexafluoride (SF₆) Emissions",
    9: "Mixed HFCs & PFCs Emissions"
}

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.main {
    background: linear-gradient(to right,#E8F5E9,#F1F8E9);
}

.title-box{
    background: linear-gradient(90deg,#1B5E20,#4CAF50);
    padding:20px;
    border-radius:15px;
    text-align:center;
    color:white;
    font-size:40px;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:#2E7D32;
    font-size:20px;
    margin-bottom:20px;
}

.card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.15);
}

.result{
    background:linear-gradient(90deg,#2E7D32,#66BB6A);
    color:white;
    padding:25px;
    border-radius:15px;
    text-align:center;
    font-size:24px;
    font-weight:bold;
    margin-top:20px;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:50px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="title-box">
🌍 Green House Gas Category Prediction System
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="subtitle">
🤖 AI Powered Environmental Analytics Dashboard
</div>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.title("📊 Dashboard")

    st.success("🟢 Model Loaded")

    st.metric("🌍 Countries", "43")
    st.metric("📂 Categories", "10")

    st.markdown("---")

    st.info("""
    This AI model predicts the greenhouse gas emission category based on:

    • Country  
    • Year  
    • Emission Value
    """)

# ---------------- INPUT SECTION ----------------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("📥 Enter Input Data")

col1, col2 = st.columns(2)

with col1:
    country_name = st.selectbox(
        "🌍 Select Country",
        list(country_map.keys())
    )

with col2:
    year = st.number_input(
        "📅 Select Year",
        min_value=1990,
        max_value=2026,
        value=2026,
        step=1
    )

value = st.number_input(
    "📈 Emission Value",
    min_value=0.0,
    max_value=9999999.0,
    value=205547.0,
    step=0.01
)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- INPUT SUMMARY ----------------
st.subheader("📋 Input Summary")

c1, c2, c3 = st.columns(3)

c1.metric("Country", country_name)
c2.metric("Year", year)
c3.metric("Value", f"{value:,.2f}")

# ---------------- PREDICTION ----------------
if st.button("🔮 Predict Category", use_container_width=True):

    data = [[country_map[country_name], year, value]]

    with st.spinner("Analyzing environmental data..."):
        prediction = model.predict(data)

    result = categories.get(prediction[0], "Unknown Category")

    st.markdown(f"""
    <div class="result">
    ✅ Prediction Result<br><br>
    {result}
    </div>
    """, unsafe_allow_html=True)

    # Confidence (if supported)
    try:
        prob = model.predict_proba(data)
        confidence = max(prob[0]) * 100

        st.success(
            f"🎯 Prediction Confidence: {confidence:.2f}%"
        )
    except:
        pass

# ---------------- DATASET INFO ----------------
with st.expander("ℹ️ About This Model"):
    st.write("""
    This machine learning model predicts greenhouse gas emission categories
    using:

    - 🌍 Country
    - 📅 Year
    - 📈 Emission Value

    The model classifies emissions into 10 greenhouse gas categories.
    """)

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
<hr>
🚀 Developed by <b>Mohit Gaur</b><br>
Green House Gas Prediction Dashboard
</div>
""", unsafe_allow_html=True)