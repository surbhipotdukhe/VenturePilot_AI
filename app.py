import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("gCO3ako80EJfmntXhqkIZgzw_C6RuTheL_Kr1zCnq23Q")
INSTANCE_URL = os.getenv("https://api.us-south.watson-orchestrate.cloud.ibm.com/instances/6d0a1428-dd3a-49ae-8521-661bfbe200a8")
AGENT_ID = os.getenv("dce69e84-1236-4ac7-9509-7f283d892954")

st.title("🚀 VenturePilot AI")
st.write("IBM watsonx Orchestrate Powered Startup Assistant")