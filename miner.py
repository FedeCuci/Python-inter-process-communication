import string
import random
import time
import multiprocessing
import subprocess

# Read only the last lines that have been added since last opening flag.txt
def read_last_lines(filename, num_lines):
    # Use the tail command to retrieve the last x lines of the file
    last_lines = subprocess.run(["tail", "-n", str(num_lines), filename], capture_output=True).stdout
    # Decode the output from bytes to a string
    last_lines = last_lines.decode("utf-8")
    # Split the output into a list of lines
    last_lines = last_lines.split("\n")
    # Remove the empty string at the end of the list
    last_lines = last_lines[:-1]

    return last_lines

def scan_blockchain():
    last_read_line = 0
    current_last_line = 0
    while True:
        time.sleep(2)
        print('scanning blockchain')
        with open("flag.txt", "r") as f:
            current_last_line = len(f.readlines())
            print(last_read_line)
            print(current_last_line)

        # If no changes have been made, return without doing anything
        if last_read_line == current_last_line:
            continue

        # Amount of lines to be read at the end of the file since last change
        lines_to_read = current_last_line - last_read_line

        # Read the last added lines
        last_lines = read_last_lines("flag.txt", lines_to_read)

        for i in last_lines:
            print(i)

        last_read_line = current_last_line

def mine_block():
    all_chars = string.ascii_letters + string.digits
    while True:
        time.sleep(2)
        
        # Store currently computed hash
        computed_hash = ''.join(random.choice(all_chars) for i in range(8))

        # If computed hash end with letter 'a' (nonce)
        if computed_hash[-1] == 'a':
            with open("flag.txt", "a") as f:
                f.write('Miner1 ' + computed_hash)

        # Think about how to adjust difficulty

# last_read_line = multiprocessing.Queue()
if __name__ == '__main__':
    try:
        p1 = multiprocessing.Process(target=scan_blockchain)
        p1.start()

        p2 = multiprocessing.Process(target=mine_block)
        p2.start()

        p2.join()
        p1.join()
    except KeyboardInterrupt:
        p1.terminate()
        p2.terminate()
