import requests, json

for x in range(0,10):
  result = requests.get("https://randomuser.me/api/")
  if result.status_code != 200:
    print("Error with the API")
  else:
    user = result.json()    
    name = ""
    for person in user['results']:
      name = f"""{person["name"]["first"]}{person["name"]["last"]}"""
  
    imageName = f"{name}.jpg"
    imageURL = f"""{user["results"][0]["picture"]["large"]}"""
    picture = requests.get(imageURL)
    f = open(imageName, "wb")
    f.write(picture.content)
    f.close() 
