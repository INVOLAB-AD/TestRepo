####################### this program creates an object with the help of facebook API #############
####################### and prints the information ###############################################

import facebook
import json

ACCESS_TOKEN = "PASTE_ACCESS_TOKEN_HERE"

def run():
    graph = facebook.GraphAPI(ACCESS_TOKEN)
    profile = graph.get_object('me',fields="name,location,link,posts")
    print(type(profile))

    print("printing the data: ")
    print(json.dumps(profile,indent=4))

    print(type(json.dumps(profile,indent=4)))

if __name__ == '__main__':
    run()
