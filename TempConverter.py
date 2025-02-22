import streamlit as st
from PIL import Image

# Function to convert temperatures
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Celsius":
            return value
        elif to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Fahrenheit":
            return value
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        elif to_unit == "Kelvin":
            return value

# Streamlit user interface
st.set_page_config(page_title="Temperature Converter 🌡️", page_icon="🌡️")

# Logo - Optional (Handle image load gracefully)
try:
    image = Image.open('your_logo.png')  # Replace with your logo path
    st.image(image, width=200)
except:
    st.warning("Logo not found! Using default layout.")

st.title("Temperature Converter App 🌡️❄️🔥")

# Input section with emojis for better user interaction
value = st.number_input("Enter temperature value 🌡️:", value=0.0)
from_unit = st.selectbox("Convert from 🔄:", ["Celsius", "Fahrenheit", "Kelvin"])
to_unit = st.selectbox("Convert to 🔁:", ["Celsius", "Fahrenheit", "Kelvin"])

# Convert and show result with emojis
if value is not None:
    result = convert_temperature(value, from_unit, to_unit)
    st.write(f"{value} {from_unit} is equal to {result:.2f} {to_unit} 🎉")

# Footer with emoji
st.markdown("""
---
Made with ❤️ by [Ahmad Rajpoot] 😊
""")
