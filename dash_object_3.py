import plotly.express as px
import pandas as pd
from dash import Dash, dcc, html

import warnings
warnings.filterwarnings('ignore')

# Load the dataset
df = pd.read_csv("Data_Participants.csv")


# Convert to datetime
df['Month'] = pd.to_datetime(df['Month'], format='%d-%b-%y')
# Covert to categorical variable
cat_list = ['Location', 'Country','Sales_Manager', 'Salesman', 'Customer', 'Cust_Type', 'Product']
for col in cat_list:
    df[col] = df[col].astype('category')

num_list = ['Sale', 'Profit', 'Cost']
for col in num_list:
    df[col] = df[col].str.replace(',', '').astype(float)

sales_country = df.groupby(["Month", "Country"])["Sale"].sum().reset_index()
max_country = sales_country.sort_values(by='Sale', ascending=False).loc[0]['Country']

# Create a line chart
line_fig = px.line(sales_country, x="Month", y="Sale", color="Country",
                     title="Sales Over Time")

# Create a bar chart     
bar_fig = px.bar(sales_country, x="Sale", y="Country", color="Country",
                 title="Sales by Country")

app = Dash()

# Set up the layout
app.layout = [
    html.H1('Sales Figures'), 
    # Add the line figure
    dcc.Graph(id='my-line-fig', figure=line_fig), 
    # Add the bar figure
    dcc.Graph(id='my-bar-fig', figure=bar_fig), 
    # Add the H3 title
    html.H3(f'The largest country by sales was {max_country}!')
    ]

if __name__ == '__main__':
    app.run(debug=True)