
import requests
import json
import os 
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()#envoking this function loads contents of the ".env" file into the script's environment... 

#... where they can be accessed /read via the os module as usual: 


APP_ID= os.getenv("APP_ID")
APP_KEY= os.getenv("APP_KEY")



def format_pct(my_number):
    """
    Formats a decimal number like 3.6555554 as a decimal rounded to two decimal places.

    Param my_number (float) like 3.6555554

    Returns (float) like '3.66'
    """
    return f"{my_number:.2f}"

def fetch_data(query):

    url = f"https://api.edamam.com/search?q={query}&app_id={APP_ID}&app_key={APP_KEY}"
    print(url)

    #url = 'https://api.edamam.com/search?q=' + query + '&app_id=' + app_id + '&app_key=' + app_key

    r = requests.get(url)
    data = json.loads(r.text)
    print(type(data))
    print(data)

    results = data["hits"]
    return results 

if __name__=="__main__":
    # instructions to only run the code below if we run this file from the command line
    # otherwise if we are just importing some functions from this file 
    # don't run this code


    #url = f"https://api.edamam.com/api/v2/recipies.json?app_id={app_id}&app_key={app_key}"
    #print(url)


    query = "coffee"
   
    results = fetch_data(query)
    print(type(results))
    print(len(results))



    #pprint(results[0])

    recipe = results[0]["recipe"]
    print(recipe.keys())
    print(recipe["label"])
    #testing def format_pct to clean up numerical format
    print(format_pct(recipe["calories"]))

