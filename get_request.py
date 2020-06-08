#!/usr/bin/env python3

from bottle import route, run, request, get

@get('/msg')
def message():

    name = request.query.name
    age = request.query.age

    return "{0} is {1} years old".format(name, age)

run(host='localhost', port=8080, debug=True)
