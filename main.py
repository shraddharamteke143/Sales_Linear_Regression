from flask import Flask, jsonify,render_template,request
from Project_app.utils import Sales_Prediction

app = Flask(__name__)

@app.route("/")
def home_api():
    print("Welcome to the Sales Prediction System")
    return render_template("index.html")

@app.route("/Sales_prediction",methods = ["POST", "GET"])
def get_prediction_charges():
    if request.method == "GET":
        print("We are in get method")
    # """data = request.form 

    # Item_Weight = eval(data["Item_Weight"])
    # print("*******",data["Item_Weight"])
    # Item_Fat_Content = data["Item_Fat_Content"]
    # Item_Visibility = eval(data["Item_Visibility"])
    # Item_Type = data["Item_Type"]
    # Item_MRP = eval(data["Item_MRP"])
    # Outlet_Identifier = data["Outlet_Identifier"]
    # Outlet_Establishment_Year = eval(data["Outlet_Establishment_Year"])
    # Outlet_Size = data["Outlet_Size"]
    # Outlet_Location_Type = data["Outlet_Location_Type"]
    # Outlet_Type = data["Outlet_Type"]"""
        Item_Weight = float(request.args.get("Item_Weight"))
        print("*******",request.args.get("Item_Weight"))
        Item_Fat_Content = request.args.get("Item_Fat_Content")
        Item_Visibility = float(request.args.get("Item_Visibility"))
        Item_Type = request.args.get("Item_Type")
        Item_MRP = float(request.args.get("Item_MRP"))
        Outlet_Identifier = request.args.get("Outlet_Identifier")
        Outlet_Establishment_Year =int(request.args.get("Outlet_Establishment_Year"))
        Outlet_Size = request.args.get("Outlet_Size")
        Outlet_Location_Type = request.args.get("Outlet_Location_Type")
        Outlet_Type = request.args.get("Outlet_Type")

        prediction = Sales_Prediction(Item_Weight, Item_Fat_Content, Item_Visibility,Item_Type, Item_MRP,
                                         Outlet_Identifier,Outlet_Establishment_Year, Outlet_Size, 
                                         Outlet_Location_Type,Outlet_Type)
        outlet_sales = prediction.predicted_outlet_sales()
    # print("Predicted Item Outlet Sales is :", outlet_sales, "/- Rs. Only")
        # return jsonify({"Result": f"Predicted Sales is {outlet_sales} /- Rs."})
        return render_template("index.html",sales = outlet_sales)
    
    else: 
        print("we are in POST method")
        Item_Weight = float(request.form.get("Item_Weight"))
        print("*******",request.form.get("Item_Weight"))
        Item_Fat_Content = request.form.get("Item_Fat_Content")
        Item_Visibility = float(request.form.get("Item_Visibility"))
        Item_Type = request.form.get("Item_Type")
        Item_MRP = float(request.form.get("Item_MRP"))
        Outlet_Identifier = request.form.get("Outlet_Identifier")
        Outlet_Establishment_Year =request.form.get("Outlet_Establishment_Year")
        Outlet_Size = request.form.get("Outlet_Size")
        Outlet_Location_Type = request.form.get("Outlet_Location_Type")
        Outlet_Type = request.form.get("Outlet_Type")

        prediction = Sales_Prediction(Item_Weight, Item_Fat_Content, Item_Visibility,Item_Type, Item_MRP,
                                         Outlet_Identifier,Outlet_Establishment_Year, Outlet_Size, 
                                         Outlet_Location_Type,Outlet_Type)
        outlet_sales = prediction.predicted_outlet_sales()
        # print("Predicted Item Outlet Sales is :", outlet_sales, "/- Rs. Only")
        # return jsonify({"Result": f"Predicted Sales is {outlet_sales} /- Rs."})
        return render_template("index.html",sales = outlet_sales)


print("__name__ -->", __name__)

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port= 5005, debug = False)  # By default Prameters
