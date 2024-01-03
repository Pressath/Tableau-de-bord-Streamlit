import mysql.connector
import streamlit as st

conn = mysql.connector.connect(
    host='localhost', 
    port='3306', 
    user ='root', 
    password='',
    db='luiz_lab'
    )

c = conn.cursor()

def view_patient_data():
    c.execute('SELECT * FROM patient')
    data = c.fetchall()
    return data
