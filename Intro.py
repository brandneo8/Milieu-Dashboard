import streamlit as st
import pandas as pd
from pyairtable import Api
from datetime import datetime

st.set_page_config(
    page_title="Milieu Sales Dashboard",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

today = datetime.today().strftime("%Y")

#Airtable API Key
AIRTABLE_API_KEY = "patKvBSBUaWVdmY59.811346d6e0eb96cae4e306d71de2d85f995b6c2445ffed74b57e38bc998659f5"
#st.secrets["airtable_key"]

#Airtable Base
AIRTABLE_BASE_ID = "apploU6sePuvAvr9G"

api=Api(AIRTABLE_API_KEY)
tblsales = api.table(AIRTABLE_BASE_ID,'actual sales')
tblsalestracker = api.table(AIRTABLE_BASE_ID,'month comparison')

print(tblsalestracker)