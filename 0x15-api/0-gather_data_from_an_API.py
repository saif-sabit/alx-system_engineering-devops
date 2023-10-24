#!/usr/bin/python3
'''
Write a Python script that, using this REST API,
 for a given employee ID
, returns information about his/her TODO list progress
'''
import requests
import sys
if __name__ == '__main__':
    API = 'https://jsonplaceholder.typicode.com/users/'
    API2 = 'https://jsonplaceholder.typicode.com/todos/'
    if (len(sys.argv) > 1):
        id = int(sys.argv[1])
        url = API+str(id)
        r = requests.get(url).json()
        url2 = API2
        r2 = requests.get(url2).json()
        name = r.get('name')
        completed = []
        userTasks = list(filter(lambda x: x.get('userId') == id, r2))
        total = len(userTasks)
        completed = list(filter(lambda x: x.get(
                                              'completed') is True, userTasks))
        print("Employee {} is done with tasks({}/{}):".format(
                                                  name, len(completed), total))
        for item in completed:
            print("\t {0}".format(item.get('title')))
