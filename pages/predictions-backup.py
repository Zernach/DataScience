# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
from joblib import load

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

#gunicorn = "*"
#spacy = "*"
#flask = "*"
#dash = "*"
#dash-bootstrap-components = "*"
#joblib = "*"
#pandas = "*"
#scikit-learn = "*"
#category-encoders = "*"
#dash-core-components = "*"
#dash-html-components = "*"
#dash.dependencies = "*"

pipeline = load('assets/pipeline.joblib')

column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            # **PREDICTIONS**

            To predict which strains of marijuana would be best for you, select your preferences and input:

            """
        ),
        html.Br(),

        dcc.Dropdown(
            id='Type',
            options = [
                {'label': 'Indica', 'value': 1},
                {'label': 'Sativa', 'value': 2},
                {'label': 'Hybrid', 'value': 3}
                ],
            value = 3,
            className='mb-3',
            placeholder='Select Indica, Sativa, or Hybrid...'
        ),

        dcc.Markdown('##### **HOW DO YOU WANT TO FEEL?**'),
        dcc.Dropdown(
            id='Feelings',
            options = [
                {'label': 'Happy', 'value': 1},
                {'label': 'Relaxed', 'value': 2},
                {'label': 'Euphoric', 'value': 3},
                {'label': 'Uplifted', 'value': 4},
                {'label': 'Creative', 'value': 5},
                {'label': 'Sleepy', 'value': 6},
                {'label': 'Energetic', 'value': 7},
                {'label': 'Focused', 'value': 8},
                {'label': 'Hungry', 'value': 9},
                {'label': 'Talkative', 'value': 10},
                {'label': 'Tingly', 'value': 11},
                {'label': 'Giggly', 'value': 12},
                {'label': 'Aroused', 'value': 13},
            ],
            value = 1,
            multi=True,
            className='mb-3',
            #placeholder='Select Preferred Feelings...'
        ),

        dcc.Markdown('##### **WHICH TASTES DO YOU LIKE?**'),
        dcc.Dropdown(
            id='Tastes',
            options = [
                {'label': 'Earth', 'value': 0},
                {'label': 'Sweet', 'value': 1},
                {'label': 'Citrus', 'value': 2},
                {'label': 'Pungent', 'value': 3},
                {'label': 'Berry', 'value': 4},
                {'label': 'Pine', 'value': 5},
                {'label': 'Wood', 'value': 6},
                {'label': 'Floral', 'value': 7},
                {'label': 'Diesel', 'value': 8},
                {'label': 'Herbal', 'value': 9},
                {'label': 'Spicy', 'value': 10},
                {'label': 'Lemon', 'value': 11},
                {'label': 'Skunk', 'value': 12},
                {'label': 'Tropical', 'value': 13},
                {'label': 'Blueberry', 'value': 14},
                {'label': 'Grape', 'value': 15},
                {'label': 'Orange', 'value': 16},
                {'label': 'Cheese', 'value': 17},
                {'label': 'Pepper', 'value': 18},
                {'label': 'Lime', 'value': 19},
                {'label': 'Strawberry', 'value': 20},
                {'label': 'Minty', 'value': 21},
                {'label': 'Pineapple', 'value': 22},
                {'label': 'Sage', 'value': 23},
                {'label': 'Grapefruit', 'value': 24},
                {'label': 'Chemical', 'value': 25},
                {'label': 'Lavender', 'value': 26},
                {'label': 'Fruity', 'value': 27},
                {'label': 'Vanilla', 'value': 28},
                {'label': 'Mango', 'value': 29},
                {'label': 'Honey', 'value': 30},
                {'label': 'Ammonia', 'value': 31},
                {'label': 'Nutty', 'value': 32},
                {'label': 'Coffee', 'value': 33},
                {'label': 'Menthol', 'value': 34},
                {'label': 'Butter', 'value': 35},
                {'label': 'Mint', 'value': 36},
                {'label': 'Tea', 'value': 37},
                {'label': 'Apple', 'value': 38},
                {'label': 'Rose', 'value': 39},
                {'label': 'Apricot', 'value': 40},
                {'label': 'Tobacco', 'value': 41},
                {'label': 'Violet', 'value': 42},
                {'label': 'Chestnut', 'value': 43},
                {'label': 'Tar', 'value': 44},
                {'label': 'Peach', 'value': 45},
                {'label': 'Sour', 'value': 46},
                {'label': 'Pear', 'value': 47},
                {'label': 'Plum', 'value': 48},
                {'label': 'Tangy', 'value': 49},
                {'label': 'Candy', 'value': 50},
            ],
            value = 1,
            multi=True,
            className='mb-3',
            #placeholder='Select your Preferred Tastes...'
        ),
    ],
    md=4,
)

column2 = dbc.Col(
    [
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    #html.Img(src='assets/Shapley Force Plots used for explaining decision tree outcome of individual instances -- Ryan Zernach Zernach.com -- Airline Price Predictions.png', className='img-fluid', height=500, width=750),
    html.H2('Predicted Marijuana Strains for Your Preferences', className= 'mb-3'),
    html.Div(id='prediction-content', className='lead'),
    html.Div(id='image')
    ]
    #md=6,
)

layout = dbc.Row([column1, column2])

@app.callback(
    Output('prediction-content', 'children'),
    [Input('Type', 'value'),
    Input('Feelings', 'value'),
    Input('Tastes', 'value')]
)


def predict(predict_bundle):

    df = pd.DataFrame(
        data=[[MktID, Quarter, Origin, OriginWac, Dest, DestWac, Miles, ContiguousUSA, NumTicketsOrdered, AirlineCompany]],
        columns=['MktID', 'Quarter', 'Origin', 'OriginWac', 'Dest', 'DestWac', 'Miles', 'ContiguousUSA', 'NumTicketsOrdered', 'AirlineCompany']
    )

    PricePerTicket = pipeline.predict(df)[0]
    return PricePerTicket
