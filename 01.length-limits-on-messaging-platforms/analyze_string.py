from typing import TypedDict

COST_PER_SMS   = 11
COST_PER_TWEET = 7
COST_PER_BOTH  = 13

def calculate_cost(chars: int, bytes: int) -> int:
  if chars < 140:
    fits_in_tweet = True

  if bytes < 160:
    fits_in_sms = True

  if fits_in_tweet and fits_in_sms:
    return COST_PER_BOTH

  elif fits_in_sms:
    return COST_PER_SMS

  elif fits_in_tweet:
    return COST_PER_TWEET

  # It's too big, cap'n
  return 0


class Result(TypedDict):
  chars: int
  bytes: int
  cost: int


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
