import pandas as pd

class HomePageData:
    test_HomePage_data = [{"firstname": "Rahul", "lastname": "shetty", "gender": "Male"},
                          {"firstname": "Amrin", "lastname": "Nargis", "gender": "Female"}]

    @staticmethod
    def fileRead_Panda():
        dict = {}
        file_name = r"C:\Users\wahid\PycharmProjects\pythonProjectFinal\TestData\HomePageTestData.xlsx"
        df = pd.read_excel(file_name, "Profiles", engine="openpyxl")
        # print (df)
        for index, row in df.iterrows():
            dict["firstname"] = row["firstname"]
            dict["lastname"] = row["lastname"]
            dict["gender"] = row["gender"]
            return dict



