import streamlit as st
from datetime import datetime

# Function to calculate age based on birthdate
def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# Set up Streamlit page
st.set_page_config(page_title="Age Calculator", page_icon=":calendar:", layout="centered")

# Title and introduction with emojis
st.title("🎉 Age Calculator App 🎂")
st.markdown("Welcome to the **Age Calculator App**! 😎🎉")
st.write("Enter your birthdate below to calculate your **current age**. Let's see how young or old you are! 🌟")

# User input for the birthdate
birthdate = st.date_input("📅 Select your birthdate", min_value=datetime(1900, 1, 1))

# Button to calculate the age
if st.button("Calculate Age 🕰️"):
    if birthdate:
        age = calculate_age(birthdate)
        st.success(f"🎉 Your age is: **{age} years** 🥳")
    else:
        st.warning("⚠️ Please select a valid birthdate.")

# Footer with some fun emojis
st.markdown("---")
st.markdown("👨‍💻 Built with ❤️ by [Ahmad Rajpoot] 🚀")
