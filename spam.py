import requests
import random
import time
import streamlit as st
# Read names from the file
with open('indian_names.txt', 'r') as file:
    names = [line.strip() for line in file.readlines()]

used_names = set()

def generate_fake_email():
    global names
    if not names:
        raise ValueError("No more names available to generate emails.")
    
    name = random.choice(names)
    names.remove(name)
    used_names.add(name)
    
    name_parts = name.split()
    if len(name_parts) > 1:
        base_email = f"{name_parts[0].lower()}.{name_parts[1].lower()}"
    else:
        base_email = f"{name_parts[0].lower()}"
    
    # Randomly decide whether to add a number
    if random.choice([True, False, True]):
        number = random.randint(1, 9999)
        email = f"{base_email}{number}@gmail.com"
    else:
        email = f"{base_email}@gmail.com"
    
    return email




unused_sentinel={
    "entry.1097232235_sentinel": "",
    "entry.1775936384_sentinel": "",
    "entry.1312496218_sentinel": "",
    "entry.672473732_sentinel": "",
    "entry.1793582539_sentinel": "",
    "entry.582838725_sentinel": "",
    "entry.1607478328_sentinel": "",
    "entry.1438499932_sentinel": "",
    "entry.333169858_sentinel": "",
    "entry.918804851_sentinel": "",
    "entry.1866907028_sentinel": "",
    "entry.175638577_sentinel": "",
    "entry.918991321_sentinel": "",
    "entry.1068938674_sentinel": "",
    "entry.1021659187_sentinel": "",
}



form_url="https://docs.google.com/forms/d/e/1FAIpQLSeeZlP0pUdkqzvKezhEsi8OaEUcxf-Ut3AOmGLmWMncNfS_gw/formResponse"

#entry id for last openended question
# "entry.854294622": "NA",
#   "entry.1760652446": time_stamp,
# time_stamp= generate_unique_timestamp()
age_groups = [
    "Less than 18 years",
    "18 - 25 years",
    "18 - 25 years",
    "25 - 45 years",
    "25 - 45 years",
    "45 - 60 years"
]

user_types = [
    "Business Owner/Decision Maker",
    "IT Administrator/Technical Staff",
    "End User/Employee",
    "End User/Employee",
    "End User/Employee"
]

importance_levels = [
    "Extremely Important",
    "Very Important",
    "Very Important",
    "Moderately Important"
]

user_training_importance_levels = [
    "Extremely Important",
    "Very Important",
    "Somewhat Important",
    "Somewhat Important",
    "Not Important"
]

experience_levels = [
    "Very Experienced",
    "Some Experience",
    "No Experience but Willing to Learn",
    "Some Experience",
    "No Experience but Willing to Learn",
    "Prefer Commercial Support Solutions"
]

authentication_methods = [
    "Multi-factor Authentication (MFA)",
    "Single Sign-On (SSO)",
    "Basic Username/Password",
    "Single Sign-On (SSO)",
    "Basic Username/Password",
    "Basic Username/Password",
    "Token-based Authentication"
]

frequency_of_use = [
    "Several times a day",
    "Once a day",
    "Several times a week",
    "Once a day",
    "Several times a week",
    "Rarely"
]

current_tools_difficulty = [
    "Very Difficult",
    "Somewhat Difficult",
    "Somewhat Difficult",
    "Neutral"
    "Somewhat Difficult",
    "Neutral"
]

security_monitor = [
    "Critical for Compliance",
    "Important for Security",
    "Nice to have",
    "Important for Security",
    "Nice to have",
    "Not necessary"
]

features_use = [
    "Ease of use",
    "Ease of use",
    "Ease of use",
    "Speed of upload/download",
    "Security of shared files",
    "Security of shared files",
    "Security of shared files",
    "Ability to collaborate in real time"
]



mobile_device = [
    "Occasionally (Weekly)",
    "Rarely",
    "Never",
    "Rarely",
    "Never"
]

technical_knowledge = [
    "Strongly Agree",
    "Agree",
    "Neutral",
    "Strongly Agree",
    "Agree",
    "Neutral",
    "Disagree"
]

user_permission = [
    "Extremely Important",
    "Very Important",
    "Somewhat Important",
    "Very Important",
    "Somewhat Important",
    "Not Important"
]

data_privacy = [
    "Extremely Concerned",
    "Very Concerned",
    "Extremely Concerned",
    "Very Concerned",
    "Somewhat Concerned"
]

main_challenge = [
    "Cost",
    "Cost",
    "Security",
    "Ease of use",
    "Ease of use",
    "Limited integration with other tools"
]

def spam(num, emails):

    success=0
    emails_lst=emails.split(",")
    for i in range(num):
        time.sleep(0.1)
        actual_features_use = random.sample(features_use, 2)
        if len(emails_lst)>2:
            fake_email=emails_lst[i]
        else:
            fake_email=generate_fake_email()



        form_data={
        "entry.1097232235": random.choice(age_groups),
        "entry.1775936384": random.choice(user_types),
        "entry.1312496218": random.choice(importance_levels),
        "entry.672473732": random.choice(user_training_importance_levels),
        "entry.1793582539": random.choice(experience_levels),
        "entry.582838725": random.choice(authentication_methods),
        "entry.1607478328": random.choice(frequency_of_use),
        "entry.1438499932": random.choice(current_tools_difficulty),
        "entry.333169858": random.choice(security_monitor),
        "entry.918804851": actual_features_use,
        "entry.1866907028": random.choice(mobile_device),
        "entry.175638577": random.choice(technical_knowledge),
        "entry.918991321": random.choice(user_permission),
        "entry.1068938674": random.choice(data_privacy),
        "entry.1021659187": random.choice(main_challenge),
        "emailAddress": fake_email,
        }

        response = requests.post(form_url, data=form_data)

        if response.status_code == 200:
            print("Form submitted successfully!")
            success+=1
        else:
            print(f"Failed to submit the form. Status code: {response.status_code}")
            print()

    st.write(f"Successfully submitted {success} forms.")