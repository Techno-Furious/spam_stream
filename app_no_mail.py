import streamlit as st
from spam_no_mail import spam

st.title("My Google Form Submitter")
number_of_submissions=st.number_input("Number of submissions", min_value=1, value=1)

if st.button("Submit"):
    spam(number_of_submissions)
    st.write(f"Completed {number_of_submissions} submissions")