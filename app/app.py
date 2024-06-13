import streamlit as st
import login
import main

def run():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if st.session_state["logged_in"]:
        main.main()
    else:
        login.login()

if __name__ == "__main__":
    run()
