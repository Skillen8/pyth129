# basic funcitonailty of json objects

import json

# create a data structure which will encode/serialize into json spec friendly text

course_films = {}
course_films['Jack Goes Boating'] = 'Java: Might we be friends project'
course_films['War Games'] = 'Password Strength checking: Tip-dont make passwords dictionary words'
course_films['Dark Waters'] = 'Python 2: Processing of toxic Realise Inventory data'
# demo boolean literals and real numbers
course_films["Python Holy Grail Clips?"] = False
course_films["Film Length"] = 4.568
course_films['film count'] = 7
# nested dict
course_films["Dictionary dictionary"] = {'A':1, "b":2,}
# JSON encoding lists
course_films['Books'] = ['Intro to python by Deitel' ,( 'The C++ Programming Language', "Intro to C++")]
# pass our native python object to the json.dumps i.e. dump string and see its structure
print(json.dumps(course_films))

# json is most useful when the string makes it into a file for actual data exchange
# creates a file with the conventional .json ending, and the use our write method
# to ship out the returned JSON-encoded string by json.dumps
with open('course_films.json', 'w') as film_file:
    film_file.write(json.dumps(course_films))
