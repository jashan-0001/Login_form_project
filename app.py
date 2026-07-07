import streamlit as st

# ----------------------------
# Page Title
# ----------------------------

st.set_page_config(
    page_title="Login Form",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Login Form")

st.write("Please enter your username and password.")

# ----------------------------
# Login Form
# ----------------------------

username = st.text_input("Username")

password = st.text_input(
    "Password",
    type="password"
)

# ----------------------------
# Login Button
# ----------------------------

if st.button("Login"):

    if username == "admin" and password == "12345":

        st.success("Login Successful!")

        st.balloons()

        st.write("Welcome,", username)

    else:

        st.error("Invalid Username or Password")