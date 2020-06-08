#!/usr/bin/env python3

from bottle import route, run, static_file

@route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./public/')

run(host='localhost', port=8080, debug=True)
