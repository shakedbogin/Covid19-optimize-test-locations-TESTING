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

import requests

url= 'https://github.com/shakedbogin/covid-optimize-map/blob/83c28e5f5a5bc3a7b01771451a160a376680e64b/distance-matrix-TEST.xlsx'
# myfile = requests.get(url)
myfile = xlsx.File(requests.get(url).body)

df=pd.read_excel(myfile.content,index_col=0)

# df = pd.read_excel('./distance-matrix-TEST.xlsx',index_col=0)
# df =  df.reset_index(drop=True)

st.write('# bla')
st.markdown('#')  
st.write('### bla')
st.write('bla')
st.markdown('#') 

st.write(df)

 

# st.write('### View samples of the data you uploaded')
# st.dataframe(df.head(),3000,500)


