# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from os import chdir, getcwd
import os

wd=getcwd()
chdir(wd)
csv_dir = os.path.join(wd, 'Conavi','202012.csv')
print(csv_dir)
df_conavi2020= pd.read_csv(csv_dir,  encoding='latin-1')

#df_conavi2019['Monto']=df_conavi2019['Monto'].str.replace(',','')
df_conavi2020['Monto']=df_conavi2020['Monto'].str.replace(',','')
#df_conavi2019['Monto']=df_conavi2019['Monto'].astype(float)
df_conavi2020['Monto']=df_conavi2020['Monto'].astype(float)

df_conavibygen=df_conavi2020.groupby(['Mes acumulado','Genero'],as_index=False)['Monto'].mean()
Month=df_conavibygen[df_conavibygen['Genero']=='Hombre']['Mes acumulado']
Hombre=df_conavibygen[df_conavibygen['Genero']=='Hombre']['Monto']
Mujer=df_conavibygen[df_conavibygen['Genero']=='Mujer']['Monto']

app = dash.Dash(__name__)
server = app.server

app = dash.Dash()
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Creditos de Vivienda',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.P(children="Analizar la diferencia entre creditos otorgado por genero"),
    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    dcc.Graph(
        id='Credito promedio por genero por mes',
        figure={
            'data': [
                {'x': Month, 'y': Hombre, 'type': 'bar', 'name': 'Hombre'},
                {'x': Month, 'y': Mujer, 'type': 'bar', 'name': 'Mujer'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
    
