import streamlit as st

# Custom styles: Very dark black text, all bold, large font sizes, and highlighted
st.markdown("""
<style>
/* Background image */
body {
    background-image: url('https://images.unsplash.com/photo-1570129477492-45c003edd2be');
    background-size: cover;
    background-attachment: fixed;
    background-position: center;
    background-repeat: no-repeat;
    color: #000000;
    font-weight: bold;
    font-size: 20px;
}

/* App container */
.stApp {
    background-color: rgba(255, 255, 255, 0.75);
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0px 6px 20px rgba(0, 0, 0, 0.3);
    backdrop-filter: blur(2px);
}

/* Title styling */
h1 {
    font-size: 3rem;
    color: #000000;
    font-weight: bold;
    text-align: center;
    margin-bottom: 2rem;
    text-shadow: 1px 1px 2px #999;
}

/* Label text (select, slider, etc.) */
label, .stSlider label, .stSelectbox label, .stTextInput label {
    color: #000000;
    font-weight: bold;
    font-size: 20px;
}

/* Buttons */
.stButton>button {
    background-color: #ffc107;
    color: #000000;
    font-weight: bold;
    font-size: 18px;
    padding: 0.75rem 1.5rem;
    border: none;
    border-radius: 8px;
    margin-top: 1rem;
}

.stButton>button:hover {
    background-color: #e0a800;
}

/* Output text block */
.stMarkdown > div {
    font-size: 22px;
    font-weight: bold;
    color: #000000;
    background-color: rgba(255, 255, 255, 0.95);
    padding: 1.2rem;
    border-radius: 12px;
    border: 2px solid #000000;
    box-shadow: 3px 3px 12px rgba(0, 0, 0, 0.2);
    margin-top: 1.5rem;
}
</style>
""", unsafe_allow_html=True)

# App title
st.title("🏠 Maharashtra Real Estate Price Estimator")

# Rate map (₹ per sqft)
rate_map = {
    "Mumbai": {
        "Andheri": 35000,
        "Bandra": 42000,
        "Borivali": 28000,
        "Dadar": 38000,
        "Goregaon": 30000,
        "Juhu": 45000,
        "Malad": 29000
    },
    "Pune": {
        "Kothrud": 16000,
        "Hinjewadi": 11000,
        "Hadapsar": 12000,
        "Baner": 15000,
        "Wakad": 13000,
        "Viman Nagar": 15500,
        "Kharadi": 14500
    },
    "Nagpur": {
        "Dharampeth": 9500,
        "Manish Nagar": 8500,
        "Sitabuldi": 8000,
        "Trimurti Nagar": 8200
    },
    "Nashik": {
        "Canada Corner": 10000,
        "Gangapur Road": 10500,
        "Indira Nagar": 9500,
        "Panchavati": 8700
    },
    "Solapur": {
        "Hotgi Road": 6000,
        "Akkalkot Road": 6200,
        "Shelgi": 5800,
        "Railway Lines": 6300
    },
    "Aurangabad": {
        "CIDCO": 9000,
        "Garkheda": 8800,
        "Shahganj": 8600,
        "Osmanpura": 9100
    }
}

# User inputs
district = st.selectbox("📍 Select District", sorted(rate_map.keys()))
area = st.selectbox("🏘️ Select Area", sorted(rate_map[district].keys()))
area_sqft = st.slider("📏 Enter Property Area (in sqft)", 300, 5000, 1000)

# Price calculation
rate_per_sqft = rate_map[district][area]
estimated_price = rate_per_sqft * area_sqft

# Result
if st.button("💡 Estimate Price"):
    st.success(f"🏷️ **Rate**: ₹{rate_per_sqft:,} per sqft")
    st.success(f"💰 **Estimated Property Price in {area}, {district}**: ₹{estimated_price:,.0f}")
