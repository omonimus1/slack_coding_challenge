
import slack
import random 
import sys


def send_challenge(challenge_to_solve):
    try:
        client = slack.WebClient(token='')
        client.chat_postMessage(channel='coding_challenges', text=challenge_to_solve)
    except:
        print('error sending challenge via slack')


# Fetch random challenge from a file; I will use a database instead
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
    # connection = mysql_connection.connect()
    # rand_challenge = mysql_connection.fetch_challenge_from_database(connection)
    challenge = fetch_random_challenge()
    # connection.close()
    send_challenge(challenge)


