import mysql.connector
import streamlit as st

conn = mysql.connector.connect(
    host='localhost', 
    port='3306', 
    user ='root', 
    password='',
    db='salaire'
    )

c = conn.cursor()

cursor = conn.cursor(prepared = True)