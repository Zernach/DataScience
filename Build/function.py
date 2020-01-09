# Search function


def search(input_value = '', input_type = '', input_effects_and_flavor = ''):

    import pandas as pd


    df = pd.read_csv('cannabis_slim.csv')
    # Search strain
    if input_value != '':
        df      = df.loc[df['Strain'] == input_value]

    # Search type
    if input_type != '':
        df      = df.loc[df['Type'] == input_type]

    # Search effects/flavor
    if input_effects_and_flavor != '':
        for thing in input_effects_and_flavor:
            df  = df.loc[df[thing] == 1]
    
    if len(df) == 0:
        return 'No results'
    else:
        return df