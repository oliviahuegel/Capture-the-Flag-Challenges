import requests
import html
import urllib.parse
import base64
from math import floor

#page1 = urllib.request.urlopen('http://challenges.ctfd.io:30107/calc/calc.php')

REQUEST_URL = 'http://challenges.ctfd.io:30107/calc/calc.php'

with requests.Session() as session:
    page1 = session.get(REQUEST_URL)
    print(page1.text)

    content = page1.text

    #will print the whole page
    #print(content)

    print("Here is the string that we need: ", content[253:317])
    first_number = content[253:257]
    first_sign = content[262:263]
    print(first_number)
    print(first_sign)

    second_number = content[268:272]
    second_sign = content[277:278]
    print(second_number)
    print(second_sign)

    third_number = content[283:287]
    third_sign = content[292:293]
    print(third_number)
    print(third_sign)

    fourth_number = content[298:302]
    fourth_sign = content[307:308]
    print(fourth_number)
    print(fourth_sign)

    fifth_number = content[313:317]
    print(fifth_number)

    total_string = (first_number + first_sign + 
                second_number + second_sign + 
                third_number + third_sign + 
                fourth_number + fourth_sign + 
                fifth_number)

    #this is the final equation
    print("Here is the final string: ", total_string)

    #this will calculate the answer to the equation
    #print ("Here is the evaluated string: ", eval(total_string))
    print(type(total_string))

    new_string = eval(total_string)
    new_string1 = floor(new_string)

    print(new_string1)
    payload = {
        'answer': new_string1
    }

    # #This URL will be the URL that your login form points to with the "action" tag.
    POST_URL = 'http://challenges.ctfd.io:30107/calc/calc.php'

    #this creates a session
    #with requests.Session() as session:
    post = session.post(POST_URL, data = payload)
    print(post.text)