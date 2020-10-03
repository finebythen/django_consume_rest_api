import requests
from django.shortcuts import render


"""
Introduction
A REST API defines a set of functions which developers can perform requests and receive responses via HTTP protocol such as GET, POST, PUT and DELETE

Think REST API as a web service that provides you the data you want to use in your application(mobile or front-end client).

The key components for a REST API request are:

GET — The most common option, returns some data from the API based on the given endpoint.
POST — Creates a new record and add it to the database.
PUT — Update an existing record.
DELETE — Deletes the record on the given endpoint.

In this guide, we will use JSONPlaceholder API.
"""


def home(request):
    # --> get the list of todos
    response = requests.get('https://jsonplaceholder.typicode.com/todos/')
    # --> transfer the response to json objects
    todos = response.json()

    context = {'todos': todos}
    return render(request, 'app_rest_api/home.html', context)
