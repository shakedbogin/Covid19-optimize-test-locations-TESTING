#!pip install PuLP

from pulp import *
import pandas as pd
import numpy as np
import str 
import re
from geopy.geocoders import Nominatim
import folium
import math
import pickle
from IPython.display import Image
import datetime 
import timeit
import streamlit as st


df = pd.read_excel('./distance-matrix-TEST.xlsx',index_col=0)
df =  df.reset_index(drop=True)

st.write('# bla')
st.markdown('#')  
st.write('### bla')
st.write('bla')
st.markdown('#') 

st.write(df)

 

# st.write('### View samples of the data you uploaded')
# st.dataframe(df.head(),3000,500)


