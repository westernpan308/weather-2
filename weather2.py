import json, requests
def main():
    
#lines 3-10 are call to the URL web-service    
  base_url = "http://api.openweathermap.org/data/2.5/weather"
  appid = "d4463de4cefb6d542ee2810c3b787989"
  city = input("\nWhat city would you like to check the weather for?\n please enter a city or zip code.")
    
  url = f"{base_url}?q={city}&units=imperial&appid={appid}"
  #print(url)
  print()  
    
  response = requests.get(url)
  unformated_data = response.json ()
  
  if response.status_code == 200:
    print()
  else:
    print(f"Error Please check Spelling or Zip Code")
    main()
  
    #print(unformated_data)
  name = unformated_data["name"]
  print(f"For the city of: {name}")
  temp = unformated_data["main"]["temp"]
  print(f"The current temperature is: {temp}")
  temp_max = unformated_data["main"]["temp_max"]
  print(f"The forecast high is: {temp_max}")
  temp_min = unformated_data["main"]["temp_min"]
  print(f"The forecast low is: {temp_min}\n")
main()
while True:
  print("Would you like to check the weather for another city?\n Y for yes\n N for no")
  option = input("y/n > ")
  print()
      
  if option == "y" or option == "Y":
    main()
  elif option == "n" or option == "N":
    print("Thank you and have a great day please return for more weather updates")
    break
  else:
    print("Error invalid entry please check spelling or ZIP code ")
    continue
