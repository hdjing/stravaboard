import os

import streamlit as st
from dotenv import load_dotenv

from stravaboard.streamlit.components import Mileage, SpeedBreakdown, Summary
from stravaboard.streamlit.stravaboard import Stravaboard

# load strava credentials from .env
load_dotenv()

# change the name of the page shown on browser
st.set_page_config(page_title="Stravaboard")

sb = Stravaboard(
    client_id=os.environ.get("103426"),
    client_secret=os.environ.get("fe6a39c8d01d5851c46f86e79dddbb25e4c26494"),
    refresh_token=os.environ.get("9275d76cb08f4cf3170b83687f26f8c499cdbdd1"),
)
sb.display(components=[Summary, SpeedBreakdown, Mileage])
