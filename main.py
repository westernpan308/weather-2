import json, requests
  
#lines 4-10 are call to the URL web-service    
base_url = "http://api.openweathermap.org/data/2.5/weather"
appid = "d4463de4cefb6d542ee2810c3b787989"

def main():
  url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={appid}"
  response = requests.get(url)
  data = response.json()
  if response.status_code == 200 and data:
      state = data[0].get("state")
      return state
  return None

  #f"{base_url}?q={city}&units=imperial&appid={appid}"

city = input("\nWhat city would you like to check the weather for?\n please enter a city or zip code.")
  
  #location = "http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={appid}"   
url = f"{base_url}?q={city}&units=imperial&appid={appid}"
  #print(url)
print()  
    
response = requests.get(url)
unformated_data = response.json ()
  
if response.status_code == 200:
  print("Successful Connection!")
else:
  print("Error not found")
  print(f"Error Please check Spelling or Zip Code")
  #main()
# line 24-30 are for pulling geolocation help from fellow student from class David call to web servicer     

if response.status_code == 200:
    # Display city, state, country information
    city = unformated_data["name"]
    state = main()
    print(f"For the following location: {city}, {state}")

    #print(unformated_data)
    #name = unformated_data["name"]
    #print(f"For the city of: {name}")
    lon = unformated_data["coord"]["lon"]
    print(f"The longitude location is: {lon}")
    lat = unformated_data["coord"]["lat"]
    print(f"The latitude location is: {lat}")
    
    temp = unformated_data["main"]["temp"]
    print(f"\nThe current temperature is: {temp}") 
    temp_max = unformated_data["main"]["temp_max"]
    print(f"The forecast high is: {temp_max}")
    temp_min = unformated_data["main"]["temp_min"]
    print(f"The forecast low is: {temp_min}\n")
    weather = unformated_data["weather"][0]["description"]
    print(f"Todays forecast: {weather}")
  
  
while True:
  print("\nWould you like to check the weather for another city?\n Y for yes\n N for no")
  option = input("y/n > ")
  print()
      
  if option == "y" or option == "Y":
    city = input("\nWhat city would you like to check the weather for?\n please enter a city or zip code.")
    url = f"{base_url}?q={city}&units=imperial&appid={appid}"
    response = requests.get(url)
    unformated_data = response.json ()
    if response.status_code == 200:
      print("Successful Connection!")
    else:
      print("Error not found")
      print("Error Please check Spelling or Zip Code")
  elif option == "n" or option == "N":
    print("Thank you and have a great day please return for more weather updates")
    break
  else:
    print("Error invalid entry please check spelling or ZIP code ")
    continue

main()