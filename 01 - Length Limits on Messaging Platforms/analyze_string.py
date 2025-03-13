from calculate_cost import calculate_cost
from result_type import Result

def analyze_string(text: str) -> Result:
  """ 
  Analyze a string and return the utf-8 byte length (bytes) and 
  character count (chars), and the cost required to send the 
  message on the most possible networks that can support it in a 
  single message

  (e.g., messages exceeding 160bytes and 140 characters will cost 0)

  >>> analyze_string("Hello")
  {'chars': 5, 'bytes': 5, 'cost': 13}

  >>> analyze_string("With emojis 👍")
  {'chars': 13, 'bytes': 16, 'cost': 13}

  >>> analyze_string(" Ã«, Ã, Ã¬, Ã¹, Ã")
  {'chars': 17, 'bytes': 25, 'cost': 13}
  """ 

  string_length = len(text)
  bit_length = len(text.encode('utf-8'))
  cost = calculate_cost(string_length, bit_length)

  return {
    'chars': string_length,
    'bytes': bit_length,
    'cost': cost
  }


if __name__ == "__main__":
  import doctest
  doctest.testmod(verbose=True)
