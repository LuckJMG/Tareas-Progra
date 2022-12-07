# Input
from operator import index


QUEUE = input()
ID = input()

# Constants
VALID_ID = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

# Variables
queue_length = 1
start_index = 0
end_index = 0

# Check position of the id in the queue
for char in QUEUE:
    if char not in VALID_ID:
        # Check if current id is equal to user id
        if QUEUE[start_index:end_index] == ID:
            break

        queue_length += 1
        start_index = end_index + 1

    end_index += 1

# Output
if QUEUE[start_index:end_index] == ID:
    print(queue_length)
else:
    print(queue_length + 1)
