import json


def get_data(time):
    input_str = input()
    if time == 1:
        full_input = json.loads(input_str)
        all_requests = full_input["requests"]
        curr_input = all_requests[-1]
        return curr_input
    else:
        return input_str

