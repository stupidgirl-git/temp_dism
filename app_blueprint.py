# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 15:49:29 2024

@author: 2632
"""

from flask import Blueprint, render_template,  request, redirect, session, send_file, url_for, jsonify
import plotly.graph_objects as go 
import pandas as pd
import json
from jinja2 import Template
import plotly.express as px
import random
import pandas as pd
import numpy as np
import datetime
import os
# from pandas.core.json_utils import jsonable_encoder
# from pandas.io.json import jsonable_encoder

app_blueprint= Blueprint('app_blueprint',__name__)


database_home= pd.read_excel('/home/stupid/DISM/files/database_home.xlsx', engine='openpyxl')

x_data = [1, 2, 3, 4, 5]
y_data = [10, 26, 85, 28, 72]

layout = {
  'title': 'Line Chart with Layout',
  'xaxis_title': 'X-Axis',
  'yaxis_title': 'Y-Axis'
}


labels = ["A", "B", "C", "D", "E"]
sizes = [20, 40, 30, 50, 20]

@app_blueprint.route('/')
def index():
    fig1 = go.Figure(data=[go.Scatter(x=x_data, y=y_data)], layout=layout)  
    graphing_stuff1 = fig1.to_json() 
    
    fig2 = px.pie(values=sizes, names=labels, title='Random Pie Chart')
    graphing_stuff2 = fig2.to_json()
    
    fig3 = go.Figure(data=[go.Bar(x=['A', 'B', 'C', 'D', 'E'], y=[52,45,86,32,54,78])])
    fig3.update_layout(title='Random Number Sequence', xaxis_title='Categories', yaxis_title='Values')
    graphing_stuff3 = fig3.to_json()
    
    return render_template('index.html', graphJSON1=graphing_stuff1, graphJSON2=graphing_stuff2, graphJSON3=graphing_stuff3)
    
@app_blueprint.route('/database')
def database():    
    return render_template('database.html')

# define dataframe to store excel file
excel_files = database_home[['Table','Internal_links']]




# Define a route for downloading the Excel files
@app_blueprint.route('/database/<file_name>/download')
def download_excel(file_name):
    if file_name not in excel_files['Table'].values:
        return jsonify({'error': 'File not found'}), 404

    excel_file =  excel_files.loc[excel_files['Table'] == file_name, 'Internal_links'].reset_index(drop=True)[0]

    return send_file(excel_file, as_attachment=True)

@app_blueprint.route('/database/api/data', methods=['GET'])
def fetch_data():
    # Fetch data from your repository (e.g., database, file, etc.)
    database_home_local = database_home.iloc[:,1:]
    database_home_local= database_home_local.iloc[:,:-2]
    database_home_local['From']= database_home_local['From'].dt.strftime('%Y-%m-%d')
    database_home_local['To']= database_home_local['To'].dt.strftime('%Y-%m-%d')
    database_home_local= database_home_local.to_dict(orient='records')
    return jsonify({'data':database_home_local})




@app_blueprint.route('/database/filter/<section>')
def fetch_data_filter(section):
    database_home_filter= database_home.iloc[:,1:]
    database_home_filter= database_home_filter.iloc[:,:-2]
    database_home_filter['From']= database_home_filter['From'].dt.strftime('%Y-%m-%d')
    database_home_filter['To']= database_home_filter['To'].dt.strftime('%Y-%m-%d')
    database_home_filter= database_home_filter.loc[database_home['Category_copy'].str.lower().str.contains(section, na=False)].reset_index(drop=True)
    database_home_filter= database_home_filter.to_dict(orient='records')
    return jsonify({'data_filtered':database_home_filter})
    

@app_blueprint.route('/upload')
def upload():
    return render_template('upload.html')
    
root_dir = '/home/stupid/DISM/files/'
file_path = os.path.join(root_dir, '%s.csv')

@app_blueprint.route('/database/<file_name>')
def process_file(file_name):
    file_path = '/home/stupid/DISM/files/'+file_name+'.csv'
    print(file_path)
    df = pd.read_csv(file_path)
    df = df.iloc[:, 1:]
    df = df.fillna('')
    print(df.columns)
    df= df.round(2)
    table_name_html = database_home.loc[database_home['Table'] == file_name, 'Name'].reset_index(drop=True)[0]
    return render_template('get_table.html', table_name_html=table_name_html, file_name=file_name)

@app_blueprint.route('/<file_name>/api/df')
def fetch_data_table(file_name):
    file_path = '/home/stupid/DISM/files/'+file_name+'.csv'
    print(file_path)
    df = pd.read_csv(file_path)
    df = df.iloc[:, 1:]
    df = df.fillna('')
    df= df.round(2)
    df_local = df.tail(5).to_dict(orient='records')
    df_headers = df.columns.tolist()
    return jsonify({'df': df_local, 'df_headers': df_headers})



