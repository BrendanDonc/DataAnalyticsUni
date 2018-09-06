# Task 1.2
def preprocess():
    import pandas as pd
    #Preprocess data
    df_raw = pd.read_csv('STUDENT.csv', index_col=0)
    df = df_raw.drop(['InitialName', 'guardian'], axis=1)
    
    #Map binaries
    df['address'] = df['address'].map({ 'U':0, 'R':1 })
    df['sex'] = df['sex'].map({ 'M':0, 'F':1 })
    df['famsize'] = df['famsize'].map({ 'LE3':0, 'GT3':1 })
    df['Pstatus'] = df['Pstatus'].map({ 'A':0, 'T':1 })
    df['schoolsup'] = df['schoolsup'].map({ 'no':0, 'yes':1 })
    df['famsup'] = df['famsup'].map({ 'no':0, 'yes':1 })
    df['paid'] = df['paid'].map({ 'no':0, 'yes':1 })
    df['activities'] = df['activities'].map({ 'no':0, 'yes':1 })
    df['nursery'] = df['nursery'].map({ 'no':0, 'yes':1 })
    df['higher'] = df['higher'].map({ 'no':0, 'yes':1 })
    df['internet'] = df['internet'].map({ 'no':0, 'yes':1 })
    df['romantic'] = df['romantic'].map({ 'no':0, 'yes':1 })
    df['G3'] = df['G3'].map({ 'FAIL': 0, 'PASS': 1 })

    #Fill via median for age
    df['age'].fillna(df['age'].median(), inplace=True)
    
    #Fill via 'none' since hot encode will flag
    df['school'].fillna('none', inplace=True)
    df['reason'].fillna('none', inplace=True)

    #Drop g1 & 2 empty rows
    df = df.drop(['G1', 'G2', 'failures'], axis=1)
    #cols_miss_drop =['G1', 'G2']
    #mask = pd.isnull(df['G1'])
    #for col in cols_miss_drop:
    # mask = mask | pd.isnull(df[col])
    #df = df[~mask]

    #Hot encode
    df = pd.get_dummies(df)
    return df