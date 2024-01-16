# -- Importations des bibliotheques --

import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import plotly.subplots as sp
from requette import *
#from conf import *

# -- Creation de page de configuration --

st.set_page_config("TABLEAU DE BORD", page_icon='labico.png', layout='wide')
st.subheader("📉 TABLEAU DE BORD DES SALAIRES")
st.markdown('---')

# -- Creation de la sidebars et des filtres --

st.sidebar.header('SIDEBAR')

genre_employe = st.sidebar.multiselect(
    label = 'filtre des employés par genre',
    options = df_employee['Gender'].unique(),
    default = df_employee['Gender'].unique(),
)

departement_employe = st.sidebar.multiselect(
    label = 'filtre des employés par département',
    options = df_employee['Department'].unique(),
    default = df_employee['Department'].unique()
)

pays_employe = st.sidebar.multiselect(
    label = 'filtre des employés par pays',
    options = df_employee['Country'].unique(),
    default = df_employee['Country'].unique()
)

bu_employe = st.sidebar.multiselect(
    label = 'filtre des employés par unité commerciale',
    options = df_employee['BusinessUnit'].unique(),
    default = df_employee['BusinessUnit'].unique()
)


def_selection = df_employee.query(
    "Gender ==@genre_employe & Department ==@departement_employe &	Country ==@pays_employe & BusinessUnit ==@bu_employe "
)


salaire_employe = def_selection['AnnualSalary'].sum()
nombre_employe = def_selection['EEID'].count()
max_sal_employe = def_selection['AnnualSalary'].max()


def metrics_employe():
    col1, col2, col3= st.columns(3)

    with col1:
        st.info('NOMBRE EMPLOYE', icon ="🌡")
        st.metric(label = "TOTAL EMPLOYE", value =f"{nombre_employe:,.0f}", delta='EMPLOYE')

    with col2:
        st.info('SALAIRE MAX', icon ="🌡")
        st.metric(label = "SALAIRE MAXIMAL", value =f"{max_sal_employe:,.0f}", delta='EMPLOYE')

    with col3:
        st.info('SALAIRE TOTAL', icon ="❤")
        st.metric(label = "SOMME DES SALAIRES", value =f"{salaire_employe}", delta='EMPLOYE')




div1, div2 = st.columns(2)
def pie_sal_dep():
    with div1:
        theme_plotly = None
        fig = px.pie(def_selection, values = "AnnualSalary", names ="Department" , title ="EMPLOYE PAR GENRE")
        fig.update_layout(legend_title="employe", legend_y = 0.9)
        fig.update_traces(textinfo=f'percent+label', textposition = 'inside')
        st.plotly_chart(fig, use_container_width=True, theme= "streamlit")



def employe_gr_sal_genre():
    with div2:
        theme_plotly = None
        fig = px.bar(def_selection, x = "Gender", y ="AnnualSalary", text_auto ='.2s', title ="SALAIRE PAR GENRE")
        fig.update_traces(textfont_size = 18,textangle = 0, textposition = 'outside', cliponaxis = False)
        st.plotly_chart(fig, use_container_width=True, theme= 'streamlit')




div3, div4 = st.columns(2)
def pie_sal_pays():
    with div3:
        theme_plotly = None
        fig = px.pie(def_selection, values = "AnnualSalary", names ="Country" , title ="SALAIRE PAR PAYS")
        fig.update_layout(legend_title="employe", legend_y = 0.9)
        fig.update_traces(textinfo=f'percent+label', textposition = 'inside')
        st.plotly_chart(fig, use_container_width=True, theme= theme_plotly)




def employe_sal_untC():
    with div4:
        theme_plotly = None
        fig = px.bar(def_selection, y = "AnnualSalary", x ="BusinessUnit", text_auto ='.2s', title ="SALAIRE PAR GENRE")
        fig.update_traces(textfont_size = 18,textangle = 0, textposition = 'outside', cliponaxis = False)
        st.plotly_chart(fig, use_container_width=True, theme= theme_plotly)




def employe_table():
    with st.expander('TUPLE DES EMPLOYE'):
        data = st.multiselect('FILTER', def_selection.columns, default = lc_employee)
        st.dataframe(def_selection[data], use_container_width=True)





def menu():
    with st.sidebar:
        select = option_menu(
            menu_title= "MENU",
            options = ['Accueil','Table'],
            icons = ["house", "book"],
            menu_icon = None,
            default_index = 0,
            orientation = "vertical",
        )
    return select

selected =menu()

if selected =='Accueil':
    metrics_employe()

    pie_sal_dep()
    employe_gr_sal_genre()
    #pie_sal_pays()
    #employe_sal_untC()
    
else:
    employe_table()
    def_selection.describe().T