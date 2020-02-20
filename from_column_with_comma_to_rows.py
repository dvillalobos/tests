import pandas as pd

csv_list = ['["SH001"]','["SH002"]','["SS002","SS009"]']
pos_list = ['["Pro"]','["Cashier"]','["Lumber"]']

a = pd.DataFrame(list(zip(csv_list,pos_list)), columns =['jobs','pos_list'])
a


# Need function that reshapes the comma separated values from a column into rows
def split_into_rows(df,col_name):
    reshaped = df.set_index(df.columns.drop(col_name,1).tolist())[col_name].str.split(',', expand=True).stack().reset_index().rename(columns={0:col_name}).loc[:, df.columns]
    
    return(reshaped)
    
# Split/reshape column into rows
a1 = split_into_rows(df=a,col_name='jobs')
a1

# Replace non-needed symbols 
a1['jobs'] = a1['jobs'].str.replace('[', '', regex=True)
a1['jobs'] = a1['jobs'].str.replace(']', '', regex=True)
a1['jobs'] = a1['jobs'].str.replace('"', '', regex=True)
#a2 = a2['jobs'].str.replace(']', '', regex=True)
a1

# Leed to create a list
a2 = list(a1['jobs'])
a2
