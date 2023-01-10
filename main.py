import time
import subprocess

last_read_line = 0

with open("flag.txt", "w") as f:
        f.truncate(0)

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

def print_hello_if_called(last_read_line):
    with open("flag.txt", "r") as f:
        current_last_line = len(f.readlines())
        # print('previous number of lines: {}'.format(previous_number_of_lines))
        print('Last read line: {}'.format(last_read_line))

        if last_read_line == current_last_line:
            return current_last_line

        lines_to_read = current_last_line - last_read_line
        print('lines to read: {}'.format(lines_to_read))

        
        last_lines = read_last_lines("flag.txt", lines_to_read)
        if "a" in last_lines:
            print("a")
        if "b" in last_lines:
            print("b")
        if "c" in last_lines:
            print("c")
        
        return current_last_line

while True:
    time.sleep(5)
    # print('Inside while loop; numbe of lines: {}'.format(previous_number_of_lines))
    last_read_line = print_hello_if_called(last_read_line)