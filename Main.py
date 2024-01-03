import streamlit as st
import plotly.express as px
import plotly.subplots as sp
import pandas as pd
from mysql_con import *


#creation page de configuration
st.set_page_config("TABLEAU DE BORD", page_icon='labico.png', layout='wide')
st.subheader("TABLEAU DE BORD D'ANALYSES BIOMEDICALES")

resultat = view_patient_data()
df_patient = pd.DataFrame(resultat,columns=['ID','Nom (s)','Prénom (s)','Date naissance','Genre','Adresse','Téléphone','Email'])
st.dataframe(df_patient)


#pages = ["Accueil", "Analyse", "Visualisation", "Prédictions"]


