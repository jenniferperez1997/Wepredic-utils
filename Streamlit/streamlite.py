import streamlit as st
import numpy as np
import pandas as pd
from utils import *

st.title('Eurosafe Patch History')

data_load_state = st.text('Loading data...')
all_sessions = Session().all()

#df = pd.DataFrame.from_dict(all_sessions)
#all_commanditaries = Commanditary().all()
all_products = Product().all()
print(all_products)
dico_list = []
for produc in all_products:
    dico_list.append(produc['attributes'])
df = pd.DataFrame.from_dict(dico_list)

data_load_state.text('Loading data...done!')

st.dataframe(df)