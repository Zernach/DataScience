<<<<<<< HEAD
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
            id      = 'Type',
            options = [
                {'label': 'Indica', 'value': 0},
                {'label': 'Sativa', 'value': 1},
                {'label': 'Hybrid', 'value': 2}
                ],
            value       = 2,
            className   = 'mb-3',
            placeholder = 'Select Indica, Sativa, or Hybrid...'
        ),

        dcc.Markdown('##### **HOW DO YOU WANT TO FEEL?**'),
        dcc.Dropdown(
            id      = 'Feelings',
            options = [
                {'label': 'Happy',     'value': 1},
                {'label': 'Relaxed',   'value': 2},
                {'label': 'Euphoric',  'value': 3},
                {'label': 'Uplifted',  'value': 4},
                {'label': 'Creative',  'value': 5},
                {'label': 'Sleepy',    'value': 6},
                {'label': 'Energetic', 'value': 7},
                {'label': 'Focused',   'value': 8},
                {'label': 'Hungry',    'value': 9},
                {'label': 'Talkative', 'value': 10},
                {'label': 'Tingly',    'value': 11},
                {'label': 'Giggly',    'value': 12},
                {'label': 'Aroused',   'value': 13},
            ],
            value     = [1],
            multi     = True,
            className = 'mb-3',
            #placeholder='Select Preferred Feelings...'
        ),

        dcc.Markdown('##### **WHICH TASTES DO YOU LIKE?**'),
        dcc.Dropdown(
            id      = 'Tastes',
            options = [
                {'label': 'Earth',      'value': 14},
                {'label': 'Sweet',      'value': 15},
                {'label': 'Citrus',     'value': 16},
                {'label': 'Pungent',    'value': 17},
                {'label': 'Berry',      'value': 18},
                {'label': 'Pine',       'value': 19},
                {'label': 'Wood',       'value': 20},
                {'label': 'Floral',     'value': 21},
                {'label': 'Diesel',     'value': 22},
                {'label': 'Herbal',     'value': 23},
                {'label': 'Spicy',      'value': 24},
                {'label': 'Lemon',      'value': 25},
                {'label': 'Skunk',      'value': 26},
                {'label': 'Tropical',   'value': 27},
                {'label': 'Blueberry',  'value': 28},
                {'label': 'Grape',      'value': 29},
                {'label': 'Orange',     'value': 30},
                {'label': 'Cheese',     'value': 31},
                {'label': 'Pepper',     'value': 32},
                {'label': 'Lime',       'value': 33},
                {'label': 'Strawberry', 'value': 34},
                {'label': 'Minty',      'value': 35},
                {'label': 'Pineapple',  'value': 36},
                {'label': 'Sage',       'value': 37},
                {'label': 'Grapefruit', 'value': 38},
                {'label': 'Chemical',   'value': 39},
                {'label': 'Lavender',   'value': 40},
                {'label': 'Fruity',     'value': 41},
                {'label': 'Vanilla',    'value': 42},
                {'label': 'Mango',      'value': 43},
                {'label': 'Honey',      'value': 44},
                {'label': 'Ammonia',    'value': 45},
                {'label': 'Nutty',      'value': 46},
                {'label': 'Coffee',     'value': 47},
                {'label': 'Menthol',    'value': 48},
                {'label': 'Butter',     'value': 49},
                {'label': 'Mint',       'value': 50},
                {'label': 'Tea',        'value': 51},
                {'label': 'Apple',      'value': 52},
                {'label': 'Rose',       'value': 53},
                {'label': 'Apricot',    'value': 54},
                {'label': 'Tobacco',    'value': 55},
                {'label': 'Violet',     'value': 56},
                {'label': 'Chestnut',   'value': 57},
                {'label': 'Tar',        'value': 58},
                {'label': 'Peach',      'value': 59},
                {'label': 'Sour',       'value': 60},
                {'label': 'Pear',       'value': 61},
                {'label': 'Plum',       'value': 62},
                {'label': 'Tangy',      'value': 63},
                {'label': 'Candy',      'value': 64},
                
            ],
            value     = [14],
            multi     = True,
            className = 'mb-3',
            #placeholder='Select your Preferred Tastes...'
        ),
    ],
    md = 4,
)

column2 = dbc.Col(
    [
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    #html.Img(src='assets/Shapley Force Plots used for explaining decision tree outcome of individual instances -- Ryan Zernach Zernach.com -- Airline Price Predictions.png', className='img-fluid', height=500, width=750),
    html.H2('Predicted Marijuana Strains for Your Preferences', className = 'mb-3'),
    html.Div(id = 'prediction-content', className = 'lead'),
    html.Div(id = 'image')
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
    
    data = [[input_type, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    # Feelings
    for feeling in input_feelings:
        data[0][feeling] = 1

    # Tastes
    for taste in input_tastes:
        data[0][taste]   = 1
    
    
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
        data    = data
    )
    
    pipeline     = load('assets/pipeline.joblib')
    y_pred_proba = pipeline.predict_proba(df)

    
    
    output = set(zip(pipeline.predict_proba(df)[0], pipeline.classes_))
    output = sorted(output, reverse = True)[:3]
    
    
    output_useless, output = zip(*output)

    
    return str(output)
    

    
    
    
# Oldie but a goodie
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
=======
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
            id      = 'Type',
            options = [
                {'label': 'Indica', 'value': 0},
                {'label': 'Sativa', 'value': 1},
                {'label': 'Hybrid', 'value': 2}
                ],
            value       = 2,
            className   = 'mb-3',
            placeholder = 'Select Indica, Sativa, or Hybrid...'
        ),

        dcc.Markdown('##### **HOW DO YOU WANT TO FEEL?**'),
        dcc.Dropdown(
            id      = 'Feelings',
            options = [
                {'label': 'Happy',     'value': 1},
                {'label': 'Relaxed',   'value': 2},
                {'label': 'Euphoric',  'value': 3},
                {'label': 'Uplifted',  'value': 4},
                {'label': 'Creative',  'value': 5},
                {'label': 'Sleepy',    'value': 6},
                {'label': 'Energetic', 'value': 7},
                {'label': 'Focused',   'value': 8},
                {'label': 'Hungry',    'value': 9},
                {'label': 'Talkative', 'value': 10},
                {'label': 'Tingly',    'value': 11},
                {'label': 'Giggly',    'value': 12},
                {'label': 'Aroused',   'value': 13},
            ],
            value     = [1],
            multi     = True,
            className = 'mb-3',
            #placeholder='Select Preferred Feelings...'
        ),

        dcc.Markdown('##### **WHICH TASTES DO YOU LIKE?**'),
        dcc.Dropdown(
            id      = 'Tastes',
            options = [
                {'label': 'Earth',      'value': 14},
                {'label': 'Sweet',      'value': 15},
                {'label': 'Citrus',     'value': 16},
                {'label': 'Pungent',    'value': 17},
                {'label': 'Berry',      'value': 18},
                {'label': 'Pine',       'value': 19},
                {'label': 'Wood',       'value': 20},
                {'label': 'Floral',     'value': 21},
                {'label': 'Diesel',     'value': 22},
                {'label': 'Herbal',     'value': 23},
                {'label': 'Spicy',      'value': 24},
                {'label': 'Lemon',      'value': 25},
                {'label': 'Skunk',      'value': 26},
                {'label': 'Tropical',   'value': 27},
                {'label': 'Blueberry',  'value': 28},
                {'label': 'Grape',      'value': 29},
                {'label': 'Orange',     'value': 30},
                {'label': 'Cheese',     'value': 31},
                {'label': 'Pepper',     'value': 32},
                {'label': 'Lime',       'value': 33},
                {'label': 'Strawberry', 'value': 34},
                {'label': 'Minty',      'value': 35},
                {'label': 'Pineapple',  'value': 36},
                {'label': 'Sage',       'value': 37},
                {'label': 'Grapefruit', 'value': 38},
                {'label': 'Chemical',   'value': 39},
                {'label': 'Lavender',   'value': 40},
                {'label': 'Fruity',     'value': 41},
                {'label': 'Vanilla',    'value': 42},
                {'label': 'Mango',      'value': 43},
                {'label': 'Honey',      'value': 44},
                {'label': 'Ammonia',    'value': 45},
                {'label': 'Nutty',      'value': 46},
                {'label': 'Coffee',     'value': 47},
                {'label': 'Menthol',    'value': 48},
                {'label': 'Butter',     'value': 49},
                {'label': 'Mint',       'value': 50},
                {'label': 'Tea',        'value': 51},
                {'label': 'Apple',      'value': 52},
                {'label': 'Rose',       'value': 53},
                {'label': 'Apricot',    'value': 54},
                {'label': 'Tobacco',    'value': 55},
                {'label': 'Violet',     'value': 56},
                {'label': 'Chestnut',   'value': 57},
                {'label': 'Tar',        'value': 58},
                {'label': 'Peach',      'value': 59},
                {'label': 'Sour',       'value': 60},
                {'label': 'Pear',       'value': 61},
                {'label': 'Plum',       'value': 62},
                {'label': 'Tangy',      'value': 63},
                {'label': 'Candy',      'value': 64},
                
            ],
            value     = [14],
            multi     = True,
            className = 'mb-3',
            #placeholder='Select your Preferred Tastes...'
        ),
    ],
    md = 4,
)

column2 = dbc.Col(
    [
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    #html.Img(src='assets/Shapley Force Plots used for explaining decision tree outcome of individual instances -- Ryan Zernach Zernach.com -- Airline Price Predictions.png', className='img-fluid', height=500, width=750),
    html.H2('Predicted Marijuana Strains for Your Preferences', className = 'mb-3'),
    html.Div(id = 'prediction-content', className = 'lead'),
    html.Div(id = 'image')
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
       'Violet', 'Wood']
    
    data    = [[input_type, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    # Feelings
    for feeling in input_feelings:
        data[0][feeling] = 1

    # Tastes
    for taste in input_tastes:
        data[0][taste]   = 1
    
    
    df = pd.DataFrame(
        columns = columns,
        data    = data
    )
    

    
    pipeline     = load('assets/pipeline.joblib')
    y_pred       = pipeline.predict(df)
    y_pred_proba = pipeline.predict_proba(df)

    
    
    zipped       = set(zip(pipeline.predict_proba(df)[0], pipeline.classes_))
    zip_sorted   = sorted(zipped, reverse = True)[:3]
    
    
    unzipped_proba, unzipped_class = zip(*zip_sorted)

    
    return str(unzipped_class)
    

    
    
    
# Oldie but a goodie
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
>>>>>>> f5a05f4a35933ced5d9dec3269bb4191f1fc49c6
#         return str(df['Strain'] + ' ')