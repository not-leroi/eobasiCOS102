#Python program to swap two cities

#To take the inputs from the user
city_1 = input("Enter the name of City 1: ")
city_2 = input("Enter the name of City 2: ")

#create a temporary variable and swap the cities
temp = city_1
city_1 = city_2
city_2 = temp

print(f"The name of City 1 after swapping is {city_1} ")
print(f"The name of City 2 after swapping is {city_2}")