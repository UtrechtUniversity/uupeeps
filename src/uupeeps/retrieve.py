import json
import time

import pandas as pd
import requests


def get_employees_url(faculty_number):
    """Collect employees per faculty"""
    url = f"https://www.uu.nl/medewerkers/RestApi/Public/GetEmployeesOrganogram?f={faculty_number}&l=EN&fullresult=true"
    json_nested  = requests.get(url)
    df = pd.DataFrame(json_nested.json()["Employees"])
    return df["Url"].tolist()


def get_employee_info(url):
    API_link = requests.get(f"https://www.uu.nl/medewerkers/RestApi/Public/getEmployeeData?page={url}")
    API_json = API_link.json()
    return API_json["Employee"]
