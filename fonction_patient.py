import streamlit as st
import plotly.express as px
import plotly.subplots as sp
import pandas as pd
from requette import *






	
# sidebar


gp_ethnique = st.sidebar.multiselect(
        label = 'filtre par Groupe ethnique',
        options = df_employee['Ethnicity'].unique(),
        default = df_employee['Ethnicity'].unique(),
    )


# process queries
def_selection = df_employee.query(
    "Gender ==@genre_employe & Ethnicity ==@gp_ethnique"
)


#metrics_employe()

div1, div2 = st.columns(2)
def employe_cam_genre():
    with div1:
        theme_plotly = None
        fig = px.pie(def_selection, values = "EEID", names ="Gender" , title ="employe par genre")
        fig.update_layout(legend_title="employe", legend_y = 0.9)
        fig.update_traces(textinfo='percent+label', textposition = 'inside')
        st.plotly_chart(fig, use_container_width=True, theme= theme_plotly)

def employe_cam_gp_sanguin():
    with div2:
        theme_plotly = None
        fig = px.bar(def_selection, y = "EEID", x ="Ethnicity", text_auto ='.2s', title ="employe par Groupe Ethnique")
        fig.update_traces(textfont_size = 18,textangle = 0, textposition = 'outside', cliponaxis = False)
        st.plotly_chart(fig, use_container_width=True, theme= theme_plotly)

#employe_cam_genre()
#employe_cam_gp_sanguin()


def employe_table():
    with st.expander('TUPLE DES EMPLOYE'):
        data = st.multiselect('FILTER', def_selection.columns, default = lc_employee)
        st.dataframe(def_selection[data], use_container_width=True)



