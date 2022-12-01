import sys

def find_max_sum(input_str: str) -> int:
  # Split the input string into a list of lines
  lines = input_str.strip().split('\n')

  # Initialize the maximum sum to be 0
  max_sum = 0

  # Initialize the current sum to be 0
  cur_sum = 0

  # Initialize a list to store the sums of the groups of integers
  sums = []

  # Loop through the lines of the input
  for line in lines:
    # If the current line is an empty string, that means we have reached
    # the end of a group. So we add the current sum to the list of sums
    # and then reset the current sum to 0.
    if line == '':
      sums.append(cur_sum)
      cur_sum = 0
    else:
      # If the current line is not an empty string, then we add the integer
      # in the line to the current sum.
      cur_sum += int(line)

  # Sort the list of sums in descending order
  sums = sorted(sums, reverse=True)

  # Return the sum of the top three sums
  return sum(sums[:3])

# Read the input from the command line
input_str = sys.stdin.read()

# Print the sum of the top three sums
print(find_max_sum(input_str))