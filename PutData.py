import json


def put_data(action, debug_str=""):
    print(json.dumps({
        "response": action,
        "debug": debug_str
    }))
    print("\n>>>BOTZONE_REQUEST_KEEP_RUNNING<<<\n")
