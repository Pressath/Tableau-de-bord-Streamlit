from mysql_con import *
import pandas as pd
# lc : liste_champs
lc_employee = ['EEID','FullName','JobTitle','Department','BusinessUnit','Gender','Ethnicity','Age','HireDate','AnnualSalary','PercentBonus','Country','City','ExitDate']	

def view_employee_sample_data():
    c.execute('SELECT * FROM employee_sample_data')
    data = c.fetchall()
    return data

def view_data(table : str):
    req = f"SELECT * FROM {table}"
    cursor.execute(req)
    resultat = cursor.fetchall()
    return resultat

resultat_employee = view_data('employee_sample_data')
df_employee = pd.DataFrame(resultat_employee, columns = lc_employee)


