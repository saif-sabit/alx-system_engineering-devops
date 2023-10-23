#!/usr/bin/python3
import requests
import sys
import json
if __name__ == '__main__':
        API = 'https://jsonplaceholder.typicode.com/users/';
        API2 = 'https://jsonplaceholder.typicode.com/todos/';
        if (sys.argv > 1):
                url = API+sys.argv[1]
                r = requests.get(url).json()
                url2 = API+sys.argv[1]
                r2 = requests.get(url2).json()
                if (r.status_code == 200 and r2.status_code == 200):
                        name = r.get('name')
                        total = len(r2)
                        completed = list(filter(lambda x:x.get('userId') == sys.argv[1],r2))
                        print(f"{0} is done with tasks({1}/{2}):".format(name, len(completed),total))
                        for item in completed:
                                print(f"\t {0}".format(item.get('title')))
                        
