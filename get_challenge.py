
import slack
import random 
import logging
import traceback
import sys
import mysql_connection


# Configure Basic Logging
logging.basicConfig(filename='log/error.log',
                            filemode='a',
                            format='%(asctime)s - %(message)s',
                            datefmt='%d-%b-%y %H:%M:%S',
                            level=logging.ERROR)


logging.basicConfig(filename='log/info.log',
                            filemode='a',
                            format='%(asctime)s - %(message)s',
                            datefmt='%d-%b-%y %H:%M:%S',
                            level=logging.INFO)


def send_challenge(challenge_to_solve):
    try:
        client = slack.WebClient(token='')
        client.chat_postMessage(channel='coding_challenges', text=challenge_to_solve)
    except Exception as error:
        logging.error("--Impossible to communicate with slack--")
        logging.exception(error)



def fetch_random_challenge():
    path_to_file = "challenges.txt"
    file = open(path_to_file)
    # Fetch all lines from the file
    lines = open(path_to_file).readlines()
    # calculate number of challenges available
    number_of_challenges = len(lines)
    logging.info("Almost got a challenge")
    # Pick a random challenge from line [0](first line) to N-1
    send_challenge(lines[random.randint(0,number_of_challenges-1)])
    logging.info("Challenge sent")



if __name__ == '__main__':
    connection = mysql_connection.connect()
    print('ottenende ca')
    rand_challenge = mysql_connection.fetch_challenge_from_database(connection)
    # fetch_random_challenge()
    connection.close()
    send_challenge(rand_challenge)


