#!/usr/bin/python3
'''
Write a Python script that, using this REST API,
 for a given employee ID
, returns information about his/her TODO list progress
'''
import csv
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
        userTasks = list(filter(lambda x: x.get('userId') == id, r2))
        with open('{}.csv'.format(id), 'w') as csvfile:
            for task in userTasks:
                csvfile.write("{},{},{},{}\n".format(
                           id, name, task.get('completed'), task.get('title')))
