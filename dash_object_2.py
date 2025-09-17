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


app = Dash()
app.layout = [
    html.Div(
    style={'background-color': 'red', 
           'height':250, 'width':250}),
    html.Div(
        children=[
        html.H1("This box"),
        html.H2("Another title")],
        style={'background-color': 'lightblue',
               'height': 250, 'width': 520})
    ]

bar_fig_country = px.bar(sales_country, x="Sale", y="Country", color="Country",
                         color_discrete_map={"India": "red", "Qatar": "green", "Bahrain": "blue",
                                            "Kuwait": "yellow", "Oman": "orange"})

app = Dash()
app.layout = [
    html.H1("Sales by Country"),
    dcc.Graph(
        id='bar_graph',
        figure=bar_fig_country
    )
]

app.run(debug=True)