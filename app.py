import streamlit as st
import joblib

# Load trained model
model = joblib.load("threat_model.pkl")

# Page settings
st.set_page_config(
    page_title="Cyber Threat Intelligence",
    page_icon="🛡️",
    layout="centered"
)

# Title
st.title("🛡️ Cyber Security Threat Intelligence System")

st.write(
    "Enter a cyber security related message below to identify "
    "the possible threat type and risk level."
)

st.divider()

# Threat description input
user_text = st.text_area(
    "🔍 Enter Threat Description",
    placeholder="Example: I received a fake email asking me to click a link and enter my password."
)

# Detect button
if st.button("🚨 Detect Threat"):

    if user_text.strip() == "":
        st.warning("Please enter a threat description.")

    else:
        # Predict threat
        prediction = model.predict([user_text])[0]

        # Threat information
        threat_info = {
            "Phishing": {
                "risk": "High",
                "explanation": "A phishing attack attempts to trick users into revealing sensitive information.",
                "action": "Do not click suspicious links or provide passwords."
            },
            "Malware": {
                "risk": "High",
                "explanation": "Malware is malicious software that can damage systems or steal information.",
                "action": "Avoid unknown files and scan the system with security software."
            },
            "Ransomware": {
                "risk": "Critical",
                "explanation": "Ransomware can encrypt files and demand payment from victims.",
                "action": "Disconnect the affected system and contact the security team."
            },
            "Brute Force": {
                "risk": "High",
                "explanation": "Brute-force attacks try many passwords to gain unauthorized access.",
                "action": "Use strong passwords and enable multi-factor authentication."
            },
            "Data Theft": {
                "risk": "Critical",
                "explanation": "Data theft involves unauthorized access or copying of sensitive information.",
                "action": "Secure accounts, restrict access and report the incident."
            }
        }

        info = threat_info.get(
            prediction,
            {
                "risk": "Unknown",
                "explanation": "The system detected a possible security threat.",
                "action": "Investigate the activity carefully."
            }
        )

        # Display results
        st.subheader("🔎 Threat Analysis")

        st.success(f"🛡️ Threat Type: {prediction}")

        st.warning(f"⚠️ Risk Level: {info['risk']}")

        st.info(f"📝 Explanation: {info['explanation']}")

        st.error(f"🔒 Recommended Action: {info['action']}")

st.divider()

st.caption("Cyber Security Threat Intelligence System | Mini Project")