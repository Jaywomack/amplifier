import pandas as pd 
import json 

def returnDataframe(jsonFileName):
    with open(jsonFileName) as file:
        posts = json.load(file)

    df = pd.DataFrame(posts)

    df = df['posts']
    newDf = pd.DataFrame()
    for i in range(df.count()):
        tmp = pd.DataFrame.from_dict(df[i])
        newDf = newDf.append(tmp)
    newDf = newDf.drop(columns="tags")
    newDf = newDf.drop_duplicates()

    return newDf
