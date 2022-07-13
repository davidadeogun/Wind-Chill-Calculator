#function to calculate windchilll for given T and V
def weather(T,V):   #where T and V are the parameters
    windchill = 35.74 + 0.6215 * T - 35.75 * (V **0.16) + 0.4275 * T * (V ** 0.16)
    return windchill    #returns the value of the windchill

#function to convert celcius to fahrenheit
def celsius2Fahrenheit(C):
    converted = C * 9/5 + 32
    return converted


#Takes temperature in celcius or fahrenheit
T = float(input("What is the temperature? "))
option = input("Fahrenheit or Celsius (F/C) ? ")

#Converts to F if the user provides the temp in C
if(option == "C"):
    T = celsius2Fahrenheit(T)

#Prints windchill for wind speeds from 5 to 60 with a 5 increment
for i in range(5,65,5):
    windchill = weather(T,i)
    print("At temperature {}, the wind speed is {} mph, and the windchill is: {:.2f}F".format(T,i,windchill)) #prints the values of the temp, wind speed and windchill