# Python-inter-process-communication between multiple scripts

# How to use

Run main.py in a terminal tab and open as many other tabs equal to the amount of user scripts that you have. User scripts can be programmed to add custom 'commands' to the flag.txt file. main.py will then read the added commands from the users in the flag.txt file and can act upon them depending on what you need.

The reason for having created this script was to find a command-line friendly way to demo how a blockchain works. Different user scripts represent users using the blockchain. flag.txt is the file which keeps a record of all the commands run by all users.

The reason for having done it like this is because a user trying to understand how the blockchain functions can simply watch the output given by main.py in real time. user scripts can be automated to perform transactions by using the time and random module. 

