def chocolate_maker(small, big, x):
  max_big = x // 5

  if big < max_big:
    big_used = big 
  else:
    big_used = max_big
  
  balance = x - big_used * 5
  return small >= balance

print (chocolate_maker(4,1,12))