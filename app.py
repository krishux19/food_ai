import streamlit as st
from decision_engine import get_food_recommendation

st.set_page_config(page_title="Smart Food AI", layout="centered")

st.title("🍽 Smart Food Decision Engine")
st.markdown("### AI-powered, context-aware food recommendations in real time")

st.divider()

user_input = st.text_area(
    "Describe your situation",
    placeholder="e.g. It's late night, I'm hungry but want something healthy",
    help="Tell your current situation to get a smart recommendation"
)

if st.button("🚀 Get Smart Recommendation"):
    if user_input.strip() == "":
        st.warning("Please describe your situation first.")
    else:
        result = get_food_recommendation(user_input)

        st.divider()
        st.subheader("✨ Your Smart Recommendation")

        st.success(result)

        st.caption("Powered by AI • Context-aware • Real-time decision support")
