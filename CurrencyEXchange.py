import streamlit as st

# Dummy conversion function for testing
def convert_currency(from_currency, to_currency, amount):
    # Example dummy conversion rates (replace with actual rates or add more)
    conversion_rates = {
        ('USD', 'EUR'): 0.85,
        ('USD', 'INR'): 75.0,
        ('EUR', 'USD'): 1.18,
        ('INR', 'USD'): 0.013,
        ('PKR', 'USD'): 0.0057,
        ('USD', 'PKR'): 175.0
    }
    
    # Look up conversion rate
    rate = conversion_rates.get((from_currency, to_currency))
    if rate:
        return amount * rate
    else:
        return "Error: Invalid conversion pair."

# Streamlit UI
st.title("💱 Currency Converter 🌍")

# Add logo at the top (you can upload your logo or use a placeholder logo)

st.markdown("### Convert between currencies easily! 💰")

# Get user input, including PKR (Pakistani Rupee)
currencies = ['USD', 'EUR', 'INR', 'GBP', 'AUD', 'CAD', 'JPY', 'PKR']
from_currency = st.selectbox("From Currency 💵", currencies)
to_currency = st.selectbox("To Currency 💸", currencies)
amount = st.number_input("Amount 💵", min_value=1, value=1)

# Conversion and display
if st.button("Convert 🚀"):
    # Ensure that the from_currency and to_currency are not the same
    if from_currency == to_currency:
        st.warning("⚠️ Please select different currencies for conversion.")
    else:
        result = convert_currency(from_currency, to_currency, amount)
        
        # Check if result is a valid conversion
        if isinstance(result, float):
            st.write(f"✅ {amount} {from_currency} = {result:.2f} {to_currency} 💵")
        else:
            st.error(f"❌ {result}")
