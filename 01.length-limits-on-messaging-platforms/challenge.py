from analyze_string import analyze_string
from result_type import Result

def read_inputs(file_path='./data/input.txt'):
  try:
    with open(file_path, 'r', encoding='utf-8') as file:
      return file.read().splitlines()
  except FileNotFoundError:
    print(f"Error: The file at {file_path} was not found.")
    raise
  except IOError as e:
    print(f"Error reading the file: {e}")
    raise

  return []


def main(): 
  """ 
  Reads in messages from `./data/input.txt` and then calculates the cost of them all
  """

  messages = read_inputs()
  cost = 0

  for message in messages: 
    result: Result = analyze_string(message)
    cost = cost + result['cost']

  print(cost)

if __name__ == "__main__":
  main()