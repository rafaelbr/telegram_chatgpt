import json
import os
import re


def get_var_from_file(var):
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, '../config/{}.json'.format(var))
    with open(abs_file_path) as f:
        json_string = json.dumps(json.load(f))
    return json_string


def append_json_data_on_message(message):
    #get {var} on string
    file_vars = re.findall(r'{(.*?)}', message)
    for var in file_vars:
        #get the value of the var on the file
        message = message.replace('{'+var+'}', get_var_from_file(var))
    return message