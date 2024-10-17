import streamlit as st
from spam import spam

st.title("My Google Form Submitter")
number_of_submissions=st.number_input("Number of submissions", min_value=1, value=1)
emails=st.text_area("email", "Enter emails")

if st.button("Spam"):
    spam(number_of_submissions, emails)
    st.write(f"Completed {number_of_submissions} submissions")