def mmm(array):
  total1 = 0
  total2 = 0
  
  for x in array:
    total1 += x
    total2 += x ** 2

  return total1, total2

data = [((n % 10) + (n // 10)) for n in range(0,98)]
(total1, total2) = mmm(data)
print("Sum1 = %d, Sum2 = %d" % (total1, total2))
# Check md5sum: 0ea8229d50fea40748cb5cde952d1afe

