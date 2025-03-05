import re
import random
import string
import streamlit as st
from streamlit_option_menu import option_menu

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 4:
        return "Strong", "✅ Strong Password!", feedback
    elif score == 3:
        return "Moderate", "⚠️ Moderate Password - Consider adding more security features.", feedback
    else:
        return "Weak", "❌ Weak Password - Improve it using the suggestions below.", feedback

def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(characters) for _ in range(length))

# Streamlit UI
st.title("🔐 Password Strength & Generator")

# Tabs
selected = option_menu(
    menu_title=None,
    options=["Check Password Strength", "Generate Password"],
    icons=["shield-lock", "key"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)

if selected == "Check Password Strength":
    st.subheader("🔍 Check Password Strength")
    st.write("Enter your password below to check its strength and receive security recommendations.")

    password = st.text_input("Enter your password", type="password")
    if st.button("Check Strength"):
        if password:
            strength, message, feedback = check_password_strength(password)
            st.markdown(f"### {message}")
            if strength != "Strong":
                st.markdown("**Suggestions:**")
                for tip in feedback:
                    st.write(f"- {tip}")

elif selected == "Generate Password":
    st.subheader("🔑 Generate a Strong Password")
    st.write("Use the slider below to set your password length and generate a secure password.")
    length = st.slider("Select password length", min_value=8, max_value=20, value=12)
    if st.button("Generate Password"):
        st.write("💡 Suggested Strong Password:")
        st.code(generate_strong_password(length), language='python')