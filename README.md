# slack_coding_challenge
Slack bot Designed to daily send a link to a coding challenge.
![image](img/logo.jpeg)

## Functionalities
This bot will automatically send a message to your slack channel. 
It is able to fetch a random link of a coding challenge from a file, or, from a mysql database (which I am currently using).

The structure of my challenges table is the following
![database]](img/db.png)

## Bot Message structure
![challenge screenshot](img/challenge.png)

## System requirements
* Python3
* slacklist ```pip install slackclient```
* Mysql ```pip install MySQL-python```

## How to avoid to get this script running h24

HEI DJ, SPIN THAT CRON JOB;
![image](img/dj.png)


[Guide to crontab job set-up](https://www.digitalocean.com/community/tutorials/how-to-use-cron-to-automate-tasks-ubuntu-1804)

## Note
* At the root folder of the bot, make sure to add create a log folder; 
* This bot has been made during a boring thursday night, any feedback is welcome. 
