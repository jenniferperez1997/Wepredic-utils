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

def format_products(all_products):
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
tabs = st.tabs(["Home","Graphics","Add Product"])

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
    col6, col7, col8 = st.columns(3)
    with col6:
        categorie = st.selectbox('Categorie',('1', '2','3','4','5','6','7','8','9','10','11','12','13','14','15'))
    with col7:
        dilution = st.selectbox('Dilution',('PUR', 'DIL'))
    with col8:
        result = st.selectbox('Result',('Occlusive', 'Semi-occlusive'))
        


    if result == 'Occlusive':
        result_value = ['Occlusive','O','SO/O','occlusive','o + so']
    if result == 'Semi-occlusive':
        result_value = ['Semi-occlusive','SO','SO/O','semi_occlusive','o + so']
    
    dilution_value = ['100%', '100', 'PUR']
    if dilution == 'PUR':
        request = "&filters[category][category_number][$eq]="+categorie
        for i in result_value:
            request += "&filters[soo][$in]["+str(result_value.index(i))+"]="+i
        for x in dilution_value:
            request += "&filters[dilution][$in]["+str(dilution_value.index(x))+"]="+x
    else:
        request = "&filters[category][category_number][$eq]="+categorie
        for i in result_value:
            request += "&filters[soo][$in]["+str(result_value.index(i))+"]="+i
        for x in dilution_value:
            request += "&filters[dilution][$notIn]["+str(dilution_value.index(x))+"]="+x
    data = format_products(Product().getByRequest(request))
    st.text("Number of products: "+str(len(data)))
    if len(data) > 0:
        st.bar_chart(data['result'].value_counts(),height=500,width=500)
        st.dataframe(data['result'].value_counts())
    st.dataframe(data)

with tabs[2]:
    st.title('Add Product')
    name = st.text_input('Product name', '')
    product_number = st.text_input('Product number', '')
    dilution = st.text_input('Dilution', '')
    soo = st.text_input('Occlusive', '')
    result = st.text_input('Result', '')
    score = st.text_input('Score', '')