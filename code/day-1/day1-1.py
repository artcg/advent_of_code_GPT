import sys

def find_max_sum(input_str: str) -> int:
  # Split the input string into a list of lines
  lines = input_str.strip().split('\n')

  # Initialize the maximum sum to be 0
  max_sum = 0

  # Initialize the current sum to be 0
  cur_sum = 0

  # Loop through the lines of the input
  for line in lines:
    # If the current line is an empty string, that means we have reached
    # the end of a group. So we update the maximum sum if the current sum
    # is greater than the maximum sum, and then reset the current sum to 0.
    if line == '':
      max_sum = max(max_sum, cur_sum)
      cur_sum = 0
    else:
      # If the current line is not an empty string, then we add the integer
      # in the line to the current sum.
      cur_sum += int(line)

  # Return the maximum sum
  return max_sum

# Read the input from the command line
input_str = sys.stdin.read()

# Print the maximum sum
print(find_max_sum(input_str))
