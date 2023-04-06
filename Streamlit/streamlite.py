import streamlit as st
import numpy as np
import pandas as pd
from utils import *
import operator

def getValue(val):
    return operator.itemgetter(val)


def intialize_products(page_number,pagesize):
    all_products = Product().getByPage(pagenumber=page_number,pagesize=pagesize)
    dico_list = []
    for produc in all_products:
        dico_list.append(produc['attributes'])
    return pd.DataFrame.from_dict(dico_list)

categories_total = Category().getTotal()
product_total = Product().getTotal()
commanditaries_total = Commanditary().getTotal()



### set variables in session state
#
#  Variables:
#  - projects
#
###



st.title('Eurosafe Patch History')
data_load_state = st.text('Loading data...')


### Init Tabs
#
#  Tabs: 
#  - Home
#  - Tab 1
#  - Tab 2
#  - Tab 3
#
###
tabs = st.tabs(["Home","Graphics"])

### Tab 1
#
#  Main Tab
#
###
with tabs[0]:
    

    ### Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Categories", categories_total)
    col2.metric("Products", product_total)
    col3.metric("Commanditaries", commanditaries_total)
    
    col4, col5 = st.columns(2)
    with col4:
        page_entries = st.number_input('Entries per page', min_value=1, value=10, max_value=100, step=1,key='page_entries')
    with col5:
        page_count = Product().getPageCount(page_entries)
        page_number = st.number_input('Page number', min_value=1, value=1, max_value=page_count, step=1,key='page_number')

    st.dataframe(intialize_products(page_number,page_entries))
  
    data_load_state.text('Loading data...done!')

with tabs[1]:
    st.title('Graphics')
    col6, col7 = st.columns(2)
    with col6:
        dilution = st.selectbox('Dilution',('PUR', 'DIL'))
    with col7:
        result = st.selectbox('Result',('Occlusive', 'Semi-occlusive'))

#print(df.value_counts("result"))
#st.bar_chart(chart_data)