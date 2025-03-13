COST_PER_SMS   = 11
COST_PER_TWEET = 7
COST_PER_BOTH  = 13

def calculate_cost(chars: int, bytes: int) -> int:
  fits_in_tweet = False
  fits_in_sms = False

  if chars <= 140:
    fits_in_tweet = True

  if bytes <= 160:
    fits_in_sms = True

  if fits_in_tweet and fits_in_sms:
    return COST_PER_BOTH

  elif fits_in_sms:
    return COST_PER_SMS

  elif fits_in_tweet:
    return COST_PER_TWEET

  # It's too big, cap'n
  return 0

if __name__ == "__main__":
  import doctest
  doctest.testmod(verbose=True)

