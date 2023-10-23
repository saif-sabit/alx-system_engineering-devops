#!/usr/bin/python3
import requests
import sys
if __name__ == '__main__':
        API = 'https://jsonplaceholder.typicode.com/users/';
        API2 = 'https://jsonplaceholder.typicode.com/todos/';
        if (len(sys.argv) > 1):
                id = int(sys.argv[1])
                url = API+str(id)
                r = requests.get(url).json()
                url2 = API+str(id)
                r2 = requests.get(url2).json()
                name = r.get('name')
                total = len(r2)
                #completed = list(filter(lambda x:x.get('userId') == id,r2))
                print("{0} is done with tasks({1}/{2}):".format(name,1,total))# len(completed),total))
                for item in completed:
                        print("\t {0}".format(item.get('title')))
                        
