import streamlit as st

st.title("FinTech Fraud Detection App")
st.write("Enter transaction details below.")

amount = st.number_input("Transaction Amount", min_value=0.0)
time = st.number_input("Transaction Time", min_value=0.0)

if st.button("Check Transaction"):
    if amount > 1000:
        st.error("This transaction looks suspicious.")
    else:
        st.success("This transaction looks normal.")