""" Web application that accepts a string and returns a new string comprised every third character """

from flask import Flask, request, jsonify, make_response
from helpers import cut_string

app = Flask(__name__)


@app.route('/test', methods=["POST"])
def return_cut_string():
    """ 
    POST a JSON object and return a JSON object
    req: {'string_to_cut': 'somestring'}
    res: {'return_string': 'mtn'}
    """

    output = {}

    # Ensure there is a key called 'string_to_cut', else respond with error.
    try:
        string_to_cut = request.json['string_to_cut']
    
    except:
        return make_response(jsonify({'error':'Please use the key: string_to_cut.'}), 400)

    # If value is a valid string pass into the cut_string function to create response value,
    # else respond with error.
    if isinstance(string_to_cut, str):
        output['return_string'] = cut_string(string_input=string_to_cut,
                                             string_length=len(string_to_cut))
    else:
        return make_response(jsonify({'error':'Please submit a string as the value.'}), 400)

    # If valid key and value, respond with the output object.
    return jsonify(output)