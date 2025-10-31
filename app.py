#import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from influxdb_client import InfluxDBClient
import os

# Configuración del tablero
st.set_page_config(page_title="Ecopack - Monitoreo Industrial", layout="wide")
st.title("
