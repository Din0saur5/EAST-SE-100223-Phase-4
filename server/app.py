#!/usr/bin/env python3

from flask import Flask
app = Flask(__name__)

hotels = [
    {
        "id":1,
        "name": "Marriot"
    },
    {
        "id":2,
        "name": "Hampton"
    },
    
    {
        "id":3,
        "name": "Hilton"
    }
    
]

@app.route('/')
def index():
    return '<h1>Is my backend too big?</h1>'

#flask run --debug

@app.route('/sum/<int:num1>/<int:num2>')
def sum_of_two_nums(num1, num2):
    #return f'{num1} + {num2} = {num1 + num2}'
    return {"sum": num1 + num2}


@app.route('/hotels')
def get_hotels():
    return hotels

@app.route('/hotels/<int:id>')
def specific_hotel(id):
    # result =  [hotel for hotel in hotels if hotel['id'] == id]
    # try:
    #     return result.pop()
    # except IndexError:
    #     return {"error": "hotel not found"}
    for hotel in hotels:
        if id == hotel['id']:
            return hotel
    return {"error": "hotel not found"}

@app.route('/display')
def display_hotels():
    hotels_lis = ""
    
    for hotel in hotels:
        hotels_lis += f"<li>Hotel # {hotel['id']}: {hotel['name']}</li>"
    
    return f'<ul>{hotels_lis}</ul>'

if __name__ == "__main__":
    app.run(port=7777, debug=True)