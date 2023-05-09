def main(city):
    import json, requests

    base_URL = "http://api.openweathermap.org/data/2.5/weather"
    appid = "d4463de4cefb6d542ee2810c3b787989"

    URL = f"{base_URL}?q={city}&units=imperial&appid={appid}"
    #print(URL)
    #print()  
#lines 14-15 are the call to and response from the URL     
    response = requests.get(URL)
    unformated_data = response.json ()
#lines 17-31 is the data requested from the URL, has if else built into for ERROR so it will loop around   
    if response.status_code == 200:
      print()
    else:
      print(f"\nError Please check Spelling or Zip Code\n")
      return

    #print(unformated_data)
    name = unformated_data["name"]
    print(f"For the city of: {name}")
    temp = unformated_data["main"]["temp"]
    print(f"The current temperature is: {temp}")
    temp_max = unformated_data["main"]["temp_max"]
    print(f"The forecast high is: {temp_max}")
    temp_min = unformated_data["main"]["temp_min"]
    print(f"The forecast low is: {temp_min}\n")
while True:
    city = input("What city would you like to check the weather for?\n please enter a city or zip code.")
    main(city)
    print("Would you like to check the weather for another city?\n Y for yes\n N for no")
    option = input("y/n > ")
    print()