import sys
import json

import requests

# Use Like python githubber.py JASchilz
# (or another user name)

if __name__ == "__main__":
    username = sys.argv[1]

    # TODO:
    #
    # 1. Retrieve a list of "events" associated with the given user name
    # 2. Print out the time stamp associated with the first event in that list.
    response = requests.get("https://api.github.com/users/{}/events".format(username))
    events = json.loads(response.content)
    
    print(f"Number of events: {len(events)}")
    if len(events) != 0:
        print(f"First event time stamp:")
        print(events[0]['created_at'])

    # print("COMPLETE THE TODOs")
    


