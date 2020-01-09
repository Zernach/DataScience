# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            #### **🌳 WHICH STRAINS OF MARIJUANA ARE BEST SUITED FOR YOU?**

            Have you ever bought some green from your local dispensary and wondered why recommended a strain?

            Unless you use a machine learning tool such as this one, you're usually going to be stuck testing every strain until you find the one that works.

            After interactively experimenting with MedCabinet+, hopefully you'll more clearly understand the differences between different strains of weed.

            """
        ),
        dcc.Link(dbc.Button("FIND WHICH STRAINS WILL WORK BEST FOR YOU ➡️", color='primary'), href='/predictions'),
        html.Br(),
        html.Br(),
        dcc.Markdown("""Go back to [MedCabinet Home Page](https://frontend-q266youge.now.sh/)""")
    ],
    md=6,
)

column2 = dbc.Col(
    [
        #dcc.Graph(figure=fig)
        html.Img(src='assets/MedCabinet_Logo.png', className='img-fluid', height=200, width=200)
    ]
)

layout = dbc.Row([column1, column2])
