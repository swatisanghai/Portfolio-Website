import streamlit as st

def main():
    # Set page title and favicon
    st.set_page_config(page_title="My Portfolio", page_icon="🚀")

    # Header
    st.title("My Portfolio")
    st.write("Welcome to my portfolio website!")

    # About Me section
    st.header("About Me")
    st.write("I am a passionate developer with expertise in Python, Flask, Django, and Streamlit. "
             "I enjoy building web applications and solving challenging problems.")

    # Projects section
    st.header("Projects")

    st.subheader("Project 1: Streamlit Portfolio")
    st.write("A portfolio website built using Streamlit. [GitHub](https://github.com/swatisanghai)")

    st.subheader("Project 2: Stock Price Prediction using LSTM and RNN")
    st.write("A  Stock Price Prediction using LSTM and RNN web app built with Streamlit. [GitHub](https:github.com/swatisanghai)")

    # Contact Me section
    st.header("Contact Me")

    st.write("Feel free to reach out to me using the contact form below:")

    name = st.text_input("Name", placeholder="Enter your name")
    email = st.text_input("Email", placeholder="Enter your email")
    message = st.text_area("Message", placeholder="Enter your message here")

    if st.button("Send Message"):
        # Logic to send the message (you can implement this part using a backend service)
        st.success("Message sent successfully!")

    # Footer
    st.markdown("---")
    st.write("Developed by Swati Sanghai(https://www.linkedin.com/in/swati-sanghai)")

if __name__ == "__main__":
    main()
