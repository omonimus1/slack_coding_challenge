
#!/usr/bin/python
import json
import sys
import random
import requests


def send_challenge(challenge_to_solve):
    url = ""
    message = challenge_to_solve
    title = (f"New Challenge available :zap:")
    slack_data = {
        "username": "ChallengeBot",
        "icon_emoji": ":satellite:",
        "channel" : "test",
        "attachments": [
            {
                "color": "#9733EE",
                "fields": [
                    {
                        "title": title,
                        "value": message,
                        "short": "false",
                    }
                ]
            }
        ]
    }
    byte_length = str(sys.getsizeof(slack_data))
    headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
    response = requests.post(url, data=json.dumps(slack_data), headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)

# Fetch random challenge from
# 
#  a file; I will use a database instead
def fetch_random_challenge():
    path_to_file = "challenges.txt"
    file = open(path_to_file)
    # Fetch all lines from the file
    lines = open(path_to_file).readlines()
    # calculate number of challenges available
    number_of_challenges = len(lines)
    # Pick a random challenge from line [0](first line) to N-1
    return lines[random.randint(0,number_of_challenges-1)]



if __name__ == '__main__':
    challenge = fetch_random_challenge()
    send_challenge(challenge)


