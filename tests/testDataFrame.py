import pandas as pd

def test_fileRead_Panda():
    dict ={}
    file_name = r"C:\Users\wahid\PycharmProjects\pythonProjectFinal\TestData\HomePageTestData.xlsx"
    df =pd.read_excel(file_name ,"Profiles" ,engine="openpyxl")
    #print (df)
    for index, row in df.iterrows():

        dict["firstname"] = row["firstname"]
        dict["lastname"] = row["lastname"]
        dict["gender"] = row["gender"]
        return dict







