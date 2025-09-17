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

# Create a line chart
line_chart = px.line(sales_country, x="Month", y="Sale", color="Country",
                     title="Sales Over Time")

# Create a bar chart
bar_chart = px.bar(sales_country, x="Sale", y="Country", color="Country",
                   title="Sales by Country", orientation="h")


app = Dash()

# Set up the layout
app.layout = [
  # Add a H1
  html.H1('Sales by Country & Over Time'),
  # Add both graphs
  dcc.Graph(id='line_graph', figure=line_chart),
  dcc.Graph(id='bar_graph', figure=bar_chart)
  ]

if __name__ == '__main__':
    app.run(debug=True)