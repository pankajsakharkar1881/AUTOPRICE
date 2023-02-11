import config
import pickle,json 
import numpy as np


class AUTO_PRICE():
    def __init__(self,symboling,normalized_losses,make,fuel_type,aspiration,num_of_doors,body_style,drive_wheels,engine_location,wheel_base,length,width,height,curb_weight,engine_type,num_of_cylinders,engine_size,fuel_system,bore,stroke,compression_ratio,horsepower,peak_rpm,city_mpg,highway_mpg):
        self.symboling                    = symboling
        self.normalized_losses            = normalized_losses
        self.make                         = "make_" + make        # dummy
        self.fuel_type                    = fuel_type        #replace
        self.aspiration                   = aspiration         #replace
        self.num_of_doors                 = num_of_doors        #replace
        self.body_style                   = "body-style_" + body_style # dummy
        self.drive_wheels                 = drive_wheels         #onehot encoder
        self.engine_location              = engine_location         #replace
        self.wheel_base                   = wheel_base 
        self.length                       = length
        self.width                        = width
        self.height                       = height
        self.curb_weight                  = curb_weight
        self.engine_type                  = "engine-type_" + engine_type        # dummy
        self.num_of_cylinders             = num_of_cylinders        #onehot encoder
        self.engine_size                  = engine_size
        self.fuel_system                  = "fuel-system_"+ fuel_system        # dummy
        self.bore                         = bore
        self.stroke                       = stroke
        self.compression_ratio            = compression_ratio
        self.horsepower                   = horsepower
        self.peak_rpm                     = peak_rpm
        self.city_mpg                     = city_mpg 
        self.highway_mpg                  = highway_mpg 
    
    def load_model(self):
        with open(config.model_file_path,"rb")as f1:
            self.model = pickle.load(f1)     # loading model
        with open(config.json_file_path,"r")as f2:
            self.json_data = json.load(f2)       # loading all encoded factors

    def get_predicted_price(self):
        self.load_model()
        array = np.zeros(len(self.json_data["columns"]),dtype=int)

    # engine_location_1 =engine_location_value[engine_location]
    # aspiration_1      =aspiration_value[aspiration]
    # num_of_doors_1   =num_of_doors_value[num_of_doors]
    # fuel_type_1       =fuel_type_value[fuel_type]       # ex...>>[fuel_type] input may be "gas" or "disel"
    # drive_wheels_1    =drive_wheels_value[drive_wheels]
    # num_of_cylinders_1=num_of_cylinders_value[num_of_cylinders]
        array[0]=self.symboling
        array[1]=self.normalized_losses 
        array[2]=self.json_data["fuel_type_value"][self.fuel_type]
        array[3]=self.json_data["aspiration_value"][self.aspiration]
        array[4]=self.json_data["num_of_doors_value"][self.num_of_doors] 
        array[5]=self.json_data["drive_wheels_value"][self.drive_wheels] 
        array[6]=self.json_data["engine_location_value"][self.engine_location] 
        array[7]=self.wheel_base
        array[8]=self.length 
        array[9]=self.width 
        array[10]=self.height 
        array[11]=self.curb_weight 
        array[12]=self.json_data["num_of_cylinders_value"][self.num_of_cylinders]
        array[13]=self.engine_size
        array[14]=self.bore
        array[15]=self.stroke 
        array[16]=self.compression_ratio 
        array[17]=self.horsepower
        array[18]=self.peak_rpm
        array[19]=self.city_mpg 
        array[20]=self.highway_mpg

        make_index = self.json_data["columns"].index(self.make)
        array[make_index] = 1

        # make_x = "make_" + make    # user input
        # make_index= np.where(columns_1 == make_x)[0][0]
        # array[make_index] = 1

        body_style_index = self.json_data["columns"].index(self.body_style)
        array[body_style_index] = 1

        # body_style_x = "body-style_" + body_style      #user input
        # body_style_index = np.where(columns_1 == body_style_x )[0][0]
        # array[body_style_index] =1

    
        engine_type_index = self.json_data["columns"].index(self.engine_type)
        array[engine_type_index] = 1

        # engine_type_x = "engine-type_" + engine_type      #user input
        # engine_type_index = np.where(columns_1 == engine_type_x )[0][0]
        # array[engine_type_index] =1

        fuel_system_index = self.json_data["columns"].index(self.fuel_system)
        array[fuel_system_index] = 1

        # fuel_system_x = "fuel-system_" + fuel_system  #user input
        # fuel_system_index = np.where(columns_1 == fuel_system_x )[0][0]
        # array[fuel_system_index] =1

        predicted_price = np.around(self.model.predict([array])[0],2)
        return predicted_price



if __name__ == "__main__":
    symboling                    = 3
    normalized_losses            = 115
    make                         = "audi"        # dummy
    fuel_type                    = "gas"         #replace
    aspiration                   = "std"         #replace
    num_of_doors                 =  "two"        #replace
    body_style                   = "convertible" # dummy
    drive_wheels                 = "rwd"         #onehot encoder
    engine_location              ="rear"         #replace
    wheel_base                   = 88.6
    length                       = 168.8
    width                        = 64.1
    height                       = 48.8
    curb_weight                  = 2548
    engine_type                  = "dohc"        # dummy
    num_of_cylinders             = "four"        #onehot encoder
    engine_size                  = 14
    fuel_system                  = "mpfi"        # dummy
    bore                         = 3.47
    stroke                       = 2.68
    compression_ratio            = 9.0
    horsepower                   = 111
    peak_rpm                     = 5000
    city_mpg                     = 21
    highway_mpg                  = 27

    obj = AUTO_PRICE(symboling,normalized_losses,make,fuel_type,aspiration,num_of_doors,body_style,drive_wheels,engine_location,wheel_base,length,width,height,curb_weight,engine_type,num_of_cylinders,engine_size,fuel_system,bore,stroke,compression_ratio,horsepower,peak_rpm,city_mpg,highway_mpg)
    result = obj.get_predicted_price()
    print(result)
