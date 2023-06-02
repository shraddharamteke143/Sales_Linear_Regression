import numpy as np
import pandas as pd
import pickle
import json
import warnings
warnings.filterwarnings('ignore')
import config as config

class Sales_Prediction():
    def __init__(self,Item_Weight, Item_Fat_Content, Item_Visibility,
       Item_Type, Item_MRP, Outlet_Identifier,
       Outlet_Establishment_Year, Outlet_Size, Outlet_Location_Type,
       Outlet_Type):
        
        self.Item_Weight =  Item_Weight
        self.Item_Fat_Content = Item_Fat_Content
        self.Item_Visibility = Item_Visibility
        # self.Item_Type = Item_Type
        self.Item_MRP = Item_MRP
        # self.Outlet_Identifier = Outlet_Identifier
        # self.Outlet_Establishment_Year = Outlet_Establishment_Year
        self.Outlet_Size = Outlet_Size
        self.Outlet_Location_Type = Outlet_Location_Type
        # self.Outlet_Type = Outlet_Type

        self.Item_Type ="IT_" + Item_Type
        self.Outlet_Establishment_Year = "OEY_" + str(Outlet_Establishment_Year)
        self.Outlet_Type ="OT_" + Outlet_Type
        self.Outlet_Identifier ="OT_" + Outlet_Identifier
    
    def model_load(self):
        print("***********************************",config.Model_file_path)
        # with open("linear_ridge_regularisation_model.pkl","rb") as f:
        with open(config.Model_file_path,"rb") as f:
            self.model = pickle.load(f)

        # with open("Project_data.json","r") as f:
        with open(config.Json_file_path,"r") as f:
            self.json_data = json.load(f)
    
    def predicted_outlet_sales(self):
        self.model_load()
        print("json_data",self.json_data['columns'])
        Item_Type_index = list(self.json_data['columns']).index(self.Item_Type)
        Outlet_Identifier_index = list(self.json_data['columns']).index(self.Outlet_Identifier)
        Outlet_Establishment_Year_index = list(self.json_data['columns']).index(self.Outlet_Establishment_Year)
        Outlet_Type_index = list(self.json_data['columns']).index(self.Outlet_Type)

        test_array = np.zeros(len(self.json_data["columns"]))

        test_array[0] = self.Item_Weight
        test_array[1] = self.json_data['Item_Fat_Content'][self.Item_Fat_Content]
        test_array[2] = self.Item_Visibility
        test_array[3] = np.cbrt(self.Item_MRP)
        test_array[4] = self.json_data['Outlet_Size'][self.Outlet_Size]
        test_array[5] = self.json_data["Outlet_Location_Type"][self.Outlet_Location_Type]
        test_array[Item_Type_index] = 1
        test_array[Outlet_Identifier_index] = 1
        test_array[Outlet_Establishment_Year_index] = 0
        test_array[Outlet_Type_index] = 0


        sales = round(self.model.predict([test_array])[0],2)
        return sales
    

if __name__ == "__main__":
    Item_Weight = 10
    Item_Fat_Content = "Low Fat"
    Item_Visibility = 0.08
    Item_Type = "Household"
    Item_MRP = 46
    Outlet_Identifier = "OUT035"
    Outlet_Establishment_Year = 2007
    Outlet_Size = "Small"
    Outlet_Location_Type = "Tier 2"
    Outlet_Type = "Supermarket Type1"
    prediction = Sales_Prediction(Item_Weight, Item_Fat_Content, Item_Visibility,Item_Type, Item_MRP,
                                         Outlet_Identifier,Outlet_Establishment_Year, Outlet_Size, 
                                         Outlet_Location_Type,Outlet_Type)
    outlet_sales = prediction.predicted_outlet_sales()
    print("Predicted Item Outlet Sales is :", outlet_sales, "/- Rs. Only")



        