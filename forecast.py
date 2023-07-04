

def weather_forecast():
    
    dic = {"patana":45 , "hajipur":40 }
    city = input("Enter a city name: ")

    # for key,value in dic:
    #     print(key) 
   

    if city not in dic:
        print("City not found.")
    else:
        temperature = dic[city]
        
        print(f"The current temperature in {city} is {temperature}°C .")

# Call the function to get the weather forecast
weather_forecast()