def preprocess(df):
  #Preprocess data
  import pandas as pd
  df_raw = pd.read_csv('STUDENT.csv', index_col=0)
  df = df_raw.drop(['InitialName', 'reason'], axis=1)
  #Map binaries
  address_map = { 'U':0, 'R':1 }
  df['address'] = df['address'].map(address_map)

  sex_map = { 'M':0, 'F':1 }
  df['sex'] = df['sex'].map(sex_map)

  famsize_map = { 'LE3':0, 'GT3':1 }
  df['famsize'] = df['famsize'].map(famsize_map)

  Pstatus_map = { 'A':0, 'T':1 }
  df['Pstatus'] = df['Pstatus'].map(Pstatus_map)

  schoolsup_map = { 'no':0, 'yes':1 }
  df['schoolsup'] = df['schoolsup'].map(schoolsup_map)

  famsup_map = { 'no':0, 'yes':1 }
  df['famsup'] = df['famsup'].map(famsup_map)

  paid_map = { 'no':0, 'yes':1 }
  df['paid'] = df['paid'].map(paid_map)

  activities_map = { 'no':0, 'yes':1 }
  df['activities'] = df['activities'].map(activities_map)

  nursery_map = { 'no':0, 'yes':1 }
  df['nursery'] = df['nursery'].map(nursery_map)

  higher_map = { 'no':0, 'yes':1 }
  df['higher'] = df['higher'].map(higher_map)

  internet_map = { 'no':0, 'yes':1 }
  df['internet'] = df['internet'].map(internet_map)

  romantic_map = { 'no':0, 'yes':1 }
  df['romantic'] = df['romantic'].map(romantic_map)

  g3_map = { 'FAIL': 0, 'PASS': 1 }
  df['G3'] = df['G3'].map(g3_map)

  #Flag school for missing vals (Dont need this cause no school is already 0)
  #df['school_nan'] = pd.isnull(df['school'])
  #df['school'].fillna(0, inplace=True)

  #Fill via median for age
  df['age'].fillna(df['age'].median(), inplace=True)

  #Hot encode
  df = pd.get_dummies(df)
  return df