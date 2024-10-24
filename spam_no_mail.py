import requests
import random
import time
import streamlit as st

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
    "25 - 45 years",
    "45 - 60 years",
    "60+ years"
]
age_groups_weights = [0.15, 0.5, 0.25, 0.095, 0.005]

user_types = [
    "Business Owner/Decision Maker",
    "IT Administrator/Technical Staff",
    "End User/Employee",
]
user_types_weights = [0.2, 0.2, 0.6]

importance_levels = [
    "Extremely Important",
    "Very Important",
    "Moderately Important",
    "Not Important"
]
importance_levels_weights = [0.4, 0.3, 0.25, 0.05]

user_training_importance_levels = [
    "Extremely Important",
    "Very Important",
    "Somewhat Important",
    "Not Important"
]
user_training_importance_levels_weights = [0.4, 0.3, 0.25, 0.05]

experience_levels = [
    "Very Experienced",
    "Some Experience",
    "No Experience but Willing to Learn",
    "Prefer Commercial Support Solutions"
]
experience_levels_weights = [0.1, 0.3, 0.4, 0.2]

authentication_methods = [
    "Multi-factor Authentication (MFA)",
    "Single Sign-On (SSO)",
    "Basic Username/Password",
    "Token-based Authentication"
]
authentication_methods_weights = [0.1, 0.1, 0.75, 0.05]

frequency_of_use = [
    "Several times a day",
    "Once a day",
    "Several times a week",
    "Rarely"
]
frequency_of_use_weights = [0.2, 0.5, 0.2, 0.1]

current_tools_difficulty = [
    "Very Difficult",
    "Somewhat Difficult",
    "Neutral",
    "Easy to Use"
]
current_tools_difficulty_weights = [0.3, 0.35, 0.3, 0.05]

security_monitor = [
    "Critical for Compliance",
    "Important for Security",
    "Nice to have",
    "Not necessary"
]
security_monitor_weights = [0.2, 0.2, 0.5, 0.1]

features_use = [
    "Ease of use",
    "Speed of upload/download",
    "Security of shared files",
    "Ability to collaborate in real time"
]
features_use_weights = [0.4, 0.15, 0.35, 0.1]


mobile_device = [
    "Frequently (Daily)",
    "Occasionally (Weekly)",
    "Rarely",
    "Never",
]
mobile_device_weights = [0.2, 0.25, 0.3, 0.25]


technical_knowledge = [
    "Strongly Agree",
    "Agree",
    "Neutral",
    "Disagree"
]
technical_knowledge_weights = [0.4, 0.3, 0.2, 0.1]

user_permission = [
    "Extremely Important",
    "Very Important",
    "Somewhat Important",
    "Not Important"
]
user_permission_weights = [0.3, 0.4, 0.2, 0.1]

data_privacy = [
    "Extremely Concerned",
    "Very Concerned",
    "Somewhat Concerned",
    "Not Concerned"
]
data_privacy_weights = [0.4, 0.3, 0.25, 0.05]


main_challenge = [
    "Cost",
    "Security",
    "Ease of use",
    "Limited integration with other tools"
]
main_challenge_weights = [0.4, 0.3, 0.2, 0.1]

def spam(num):

    success=0
    for i in range(num):
        actual_features_use = random.choices(features_use,weights=features_use_weights,k=2)
        



        form_data={
        "entry.1097232235": random.choices(age_groups, weights=age_groups_weights,k=1)[0],
        "entry.1775936384": random.choices(user_types, weights=user_types_weights,k=1)[0],
        "entry.1312496218": random.choices(importance_levels, weights=importance_levels_weights,k=1)[0],
        "entry.672473732": random.choices(user_training_importance_levels, weights=user_training_importance_levels_weights,k=1)[0],
        "entry.1793582539": random.choices(experience_levels, weights=experience_levels_weights,k=1)[0],
        "entry.582838725": random.choices(authentication_methods, weights=authentication_methods_weights,k=1)[0],
        "entry.1607478328": random.choices(frequency_of_use, weights=frequency_of_use_weights,k=1)[0],
        "entry.1438499932": random.choices(current_tools_difficulty, weights=current_tools_difficulty_weights,k=1)[0],
        "entry.333169858": random.choices(security_monitor, weights=security_monitor_weights,k=1)[0],
        "entry.918804851": actual_features_use,
        "entry.1866907028": random.choices(mobile_device, weights=mobile_device_weights,k=1)[0],
        "entry.175638577": random.choices(technical_knowledge, weights=technical_knowledge_weights,k=1)[0],
        "entry.918991321": random.choices(user_permission, weights=user_permission_weights,k=1)[0],
        "entry.1068938674": random.choices(data_privacy, weights=data_privacy_weights,k=1)[0],
        "entry.1021659187": random.choices(main_challenge, weights=main_challenge_weights,k=1)[0],
        }

        response = requests.post(form_url, data=form_data)

        if response.status_code == 200:
            print("Form submitted successfully!")
            success+=1
        else:
            print(f"Failed to submit the form. Status code: {response.status_code}")
            print()

    st.write(f"Successfully submitted {success} forms.")
