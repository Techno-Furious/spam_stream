import requests
from pprint import pprint
import random


def spam(number_of_submissions=10):
    form_url="https://docs.google.com/forms/d/e/1FAIpQLSdH94eFM9Hy9kV6t2lpVAPxjWpL1eb1XyP-cOiaaYTkGLZDoQ/formResponse"


    age=["Less than 18 years"]
    category=["Student","Patient seeking support","Patient seeking support","Caregiver or family member","Caregiver or family member","Healthcare professional"]
    medical_con=["Mental health issues","Mental health issues","Chronic illness","Physical disability","Addiction"]
    frequency=["Daily","Weekly","Monthly","Monthly","Monthly","Rarely"]
    topics=["Coping strategies","Treatment options","Personal stories","Support for caregivers"]
    sharing=["Personal stories","Expert advice","Emotional support","Resource sharing","Resource sharing","Personal stories"]
    privacy=["Very important","Important","Important","Important","Neutral","Neutral"]
    existing=["Yes","No","No","No","No"]
    improvements=["Better moderation","Better moderation","More resources","Increased privacy options","Improved user interface","Improved user interface"]
    moderation=["Strict moderation","Moderate moderation","Moderate moderation","Moderate moderation","Minimal moderation"]



    for i in range (number_of_submissions):
        form_data= {
            "entry.1598714372": "",  
            "entry.78583603": random.choice(age),  
            "entry.937959837": random.choice(category),
            "entry.570884855": random.choice(medical_con),
            "entry.1800681595": random.choice(frequency),
            "entry.1888392371": random.choice(topics),
            
            
            "entry.1879605886": random.choice(sharing),
            "entry.1879605886": random.choice(sharing),


            "entry.1972885232": random.choice(privacy),
            "entry.2142885591": random.choice(existing),
            
            "entry.197494813": random.choice(improvements) , 
            "entry.197494813": random.choice(improvements),
            "entry.197494813": random.choice(improvements),


            "entry.76239186": random.choice(moderation),
            
            "entry.78583603_sentinel": "",
            "entry.937959837_sentinel": "",
            "entry.570884855_sentinel": "",
            "entry.1800681595_sentinel": "",
            "entry.1888392371_sentinel": "",
            "entry.1879605886_sentinel": "",
            "entry.1972885232_sentinel": "",
            "entry.2142885591_sentinel": "",
            "entry.197494813_sentinel": "",
            "entry.76239186_sentinel": "",
        }



        response = requests.post(form_url, data=form_data)

        if response.status_code == 200:
            print("Form submitted successfully!")
        else:
            print(f"Failed to submit the form. Status code: {response.status_code}")