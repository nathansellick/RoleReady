import streamlit as st

# CSS for dark blue background
st.markdown(
    """
    <style>
    .stApp {
        background-color: #00008B;  /* Dark Blue color */
        color: white;  /* Change text color to white for better contrast */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Role Ready")
st.write(
    "Match. Tailor. Succeed."
)


