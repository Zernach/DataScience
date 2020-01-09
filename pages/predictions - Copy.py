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
                {'label': 'Indica', 'value': 0},
                {'label': 'Sativa', 'value': 1},
                {'label': 'Hybrid', 'value': 2}
                ],
            value = 2,
            className='mb-3',
            placeholder='Select Indica, Sativa, or Hybrid...'
        ),

        dcc.Markdown('##### **HOW DO YOU WANT TO FEEL?**'),
        dcc.Dropdown(
            id='Feelings',
            options = [
                {'label': 'Happy',     'value': 'Happy'},
                {'label': 'Relaxed',   'value': 'Relaxed'},
                {'label': 'Euphoric',  'value': 'Euphoric'},
                {'label': 'Uplifted',  'value': 'Uplifted'},
                {'label': 'Creative',  'value': 'Creative'},
                {'label': 'Sleepy',    'value': 'Sleepy'},
                {'label': 'Energetic', 'value': 'Energetic'},
                {'label': 'Focused',   'value': 'Focused'},
                {'label': 'Hungry',    'value': 'Hungry'},
                {'label': 'Talkative', 'value': 'Talkative'},
                {'label': 'Tingly',    'value': 'Tingly'},
                {'label': 'Giggly',    'value': 'Giggly'},
                {'label': 'Aroused',   'value': 'Aroused'},
            ],
            value = ['Happy'],
            multi=True,
            className='mb-3',
            #placeholder='Select Preferred Feelings...'
        ),

        dcc.Markdown('##### **WHICH TASTES DO YOU LIKE?**'),
        dcc.Dropdown(
            id='Tastes',
            options = [
                {'label': 'Earth',      'value': 'Earth'},
                {'label': 'Sweet',      'value': 'Sweet'},
                {'label': 'Citrus',     'value': 'Citrus'},
                {'label': 'Pungent',    'value': 'Pungent'},
                {'label': 'Berry',      'value': 'Berry'},
                {'label': 'Pine',       'value': 'Pine'},
                {'label': 'Wood',       'value': 'Wood'},
                {'label': 'Floral',     'value': 'Floral'},
                {'label': 'Diesel',     'value': 'Diesel'},
                {'label': 'Herbal',     'value': 'Herbal'},
                {'label': 'Spicy',      'value': 'Spicy'},
                {'label': 'Lemon',      'value': 'Lemon'},
                {'label': 'Skunk',      'value': 'Skunk'},
                {'label': 'Tropical',   'value': 'Tropical'},
                {'label': 'Blueberry',  'value': 'Blueberry'},
                {'label': 'Grape',      'value': 'Grape'},
                {'label': 'Orange',     'value': 'Orange'},
                {'label': 'Cheese',     'value': 'Cheese'},
                {'label': 'Pepper',     'value': 'Pepper'},
                {'label': 'Lime',       'value': 'Lime'},
                {'label': 'Strawberry', 'value': 'Strawberry'},
                {'label': 'Minty',      'value': 'Minty'},
                {'label': 'Pineapple',  'value': 'Pineapple'},
                {'label': 'Sage',       'value': 'Sage'},
                {'label': 'Grapefruit', 'value': 'Grapefruit'},
                {'label': 'Chemical',   'value': 'Chemical'},
                {'label': 'Lavender',   'value': 'Lavender'},
                {'label': 'Fruity',     'value': 'Fruity'},
                {'label': 'Vanilla',    'value': 'Vanilla'},
                {'label': 'Mango',      'value': 'Mango'},
                {'label': 'Honey',      'value': 'Honey'},
                {'label': 'Ammonia',    'value': 'Ammonia'},
                {'label': 'Nutty',      'value': 'Nutty'},
                {'label': 'Coffee',     'value': 'Coffee'},
                {'label': 'Menthol',    'value': 'Menthol'},
                {'label': 'Butter',     'value': 'Butter'},
                {'label': 'Mint',       'value': 'Mint'},
                {'label': 'Tea',        'value': 'Tea'},
                {'label': 'Apple',      'value': 'Apple'},
                {'label': 'Rose',       'value': 'Rose'},
                {'label': 'Apricot',    'value': 'Apricot'},
                {'label': 'Tobacco',    'value': 'Tobacco'},
                {'label': 'Violet',     'value': 'Violet'},
                {'label': 'Chestnut',   'value': 'Chestnut'},
                {'label': 'Tar',        'value': 'Tar'},
                {'label': 'Peach',      'value': 'Peach'},
                {'label': 'Sour',       'value': 'Sour'},
                {'label': 'Pear',       'value': 'Pear'},
                {'label': 'Plum',       'value': 'Plum'},
                {'label': 'Tangy',      'value': 'Tangy'},
                {'label': 'Candy',      'value': 'Candy'},
                
            ],
            value = ['Sweet'],
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
def predict(input_type = '', input_feelings = [], input_tastes = []):

    df = pd.DataFrame(
        columns = ['Type', 'Aroused', 'Creative', 'Energetic', 'Euphoric',
       'Focused', 'Giggly', 'Happy', 'Hungry', 'Relaxed', 'Sleepy',
       'Talkative', 'Tingly', 'Uplifted', 'Ammonia', 'Apple', 'Apricot',
       'Berry', 'Blueberry', 'Butter', 'Candy', 'Cheese', 'Chemical',
       'Chestnut', 'Citrus', 'Coffee', 'Diesel', 'Earthy', 'Floral', 'Fruity',
       'Grape', 'Grapefruit', 'Herbal', 'Honey', 'Lavender', 'Lemon', 'Lime',
       'Mango', 'Melon', 'Menthol', 'Mint', 'Minty', 'Nutty', 'Orange',
       'Peach', 'Pear', 'Pepper', 'Pine', 'Pineapple', 'Plum', 'Pungent',
       'Rose', 'Sage', 'Skunk', 'Sour', 'Spicy', 'Strawberry', 'Sweet',
       'Tangy', 'Tar', 'Tart', 'Tea', 'Tobacco', 'Tropical', 'Vanilla',
       'Violet', 'Wood'],
        data    = [[input_type, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    )
    
    
    pipeline = load('assets/pipeline.joblib')
    y_pred   = pipeline.predict(df)[0]
    
    return f'{input_type}, {y_pred}'
    
    
#     if y_pred == '':
#         y_pred_proba = pipeline.predict_proba(df)[0][0]
#         return f'{y_pred_proba*100:.0f}% chance of {y_pred}'
#     else:
#         y_pred_proba = pipeline.predict_proba(df)[0][1]
#         return f'{y_pred_proba*100:.0f}% chance of {y_pred}'
    
    
    
    
# def search(input_type = '', input_effects = [], input_flavor = []):

#     import pandas as pd


#     df = pd.read_csv('Data/cannabis_slim.csv')
#     # Search type
#     if input_type != '':
#         df      = df.loc[df['Type'] == input_type]

#     # Search effects
#     if input_effects != []:
#         for thing in input_effects:
#             df  = df.loc[df[thing] == 1]

#     # Search flavor
#     if input_flavor != []:
#         for thing in input_flavor:
#             df  = df.loc[df[thing] == 1]
    

#     if len(df) == 0:
#         return 'No results.'
#     else:
#         return str(df['Strain'] + ' ')