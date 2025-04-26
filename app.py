# Streamlit 
import streamlit as st 

st.set_page_config(page_title="growth mindset project", page_icon="★")
st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header("🚀 Welcome to Your Own Growth Journey!")
st.write("Embrace challenges,learn from  mistake, and unlock your full potential.!🌟")

# quotr section
st.header("💡 Today's Growth Mindset Quote" )
st.write("Success is not final, failure is not fatal: it is the courage to continue that counts.- Winston Churchill")

st.header("🔧 What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're faing:")


# condition
if user_input:
    st.success (f"💪 Your'e facing:{user_input}.keep pushing forward towards your goal!🚀" )
else:
    st.warning("Tell us about your challenge tp get started!")

    # reflexing
    st.header("🧠Reclect on Your Learning")
    reflection = st.text_area("Write your reflections here:")

    if reflection:
        st.success(f"✨ Great Insight! Your reflection:{reflection}")
    else:
        st.info("Reflection on past experience help you grow! Share youe difficulties")


# acheivements
st.header("🏆 Celebrate Your Wins!")
acheivement = st.text_input("Share something you;ve recently accomplished:")

if acheivement:
    st.success (f"⭐ Amazing! You achieved:{acheivement}")
else:
    st.info("Big or small, every acheivement counts! Share one now😍")

    # footer
st.write ("- - -")
st.write("🚀 Keep believing in yourself,Growth is a journey, not a destination! 🌟")
st.write("**Created by Afsheen Afridi**")