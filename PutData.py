import json
import sys


def put_data(action, debug_str=""):
    print(json.dumps({
        "response": action,
        "debug": debug_str
    }))
    print(">>>BOTZONE_REQUEST_KEEP_RUNNING<<<")
    sys.stdout.flush()
