def convert2meter(s, input_unit="in"):
    '''
    Function to convert inches, feet and cubic feet to meters and cubic meters 
    '''
    if input_unit == "in":
        return s*0.0254
    elif input_unit == "ft":
        return s*0.3048
    elif input_unit == "cft":
        return s*0.0283168
    else:
        print("Error: Input unit is unknown.")
        
## Apply function
measurement_unit = {"Girth":"in",
                    "Height":"ft", 
                    "Volume":"cft"}

trees = trees_raw.copy()
for feature in ["Girth", "Height", "Volume"]:
    trees[feature] = trees_raw[feature].apply(lambda x: convert2meter(s=x,
                                 input_unit=measurement_unit.get(feature))) 
                                                 
                                                                      