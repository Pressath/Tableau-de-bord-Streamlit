import streamlit as st
from streamlit_option_menu import option_menu


#creation page de configuration
st.set_page_config("TABLEAU DE BORD", page_icon='labico.png', layout='wide')

def page_creat():
    st.subheader("📉 TABLEAU DE BORD DES SALAIRES")
    st.markdown('---')

def menu():
    with st.sidebar:
        select = option_menu(
            menu_title= "MENU",
            options = ['Accueil','Analyse','Resultat'],
            icons = ["house", "book","cast"],
            menu_icon = None,
            default_index = 0,
            orientation = "vertical",
        )
    return select

