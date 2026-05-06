import streamlit as st
from context_parser import extract_context
from decision_engine import get_food_recommendation
from maps_service import get_nearby_food

st.set_page_config(page_title="Food Decision Engine")

st.title("🍽️ Smart Food Decision Engine")
st.caption("Real-time food decisions based on context")

user_input = st.text_area("Describe your situation")

if st.button("Get Suggestion"):

    if not user_input.strip():
        st.warning("Please enter input")
    else:
        context = extract_context(user_input)

        st.subheader("🧠 Detected Context")
        st.write(context)

        recommendation = get_food_recommendation(context, user_input)

        st.subheader("🥗 Recommendations")
        st.write(recommendation)

        st.subheader("📍 Nearby Options")
        places = get_nearby_food()

        for p in places:
            st.write(f"{p['name']} (⭐ {p['rating']})")