# A divide and conquer algorithm
# Will be compared with naive search that scans all elements in the list 

import random
import time

def naive_search(l, target):
  for i in range(len(l)):
    if l[i] == target:
      return i
  return -1

def binary_search(l, target, low=None, high=None):
  if low is None:
    low = 0
  if high is None:
    high = len(l) - 1
  if high < low:
    return -1

  midpoint = (low + high) // 2 

  if l[midpoint] == target:
    return midpoint
  elif target < l[midpoint]:
    return binary_search(l, target, low, midpoint-1)
  else:
    return binary_search(l, target, midpoint+1, high)

def search():
  lenght = int(input('Choose the lenght of the list to compare the search time: '))
  
  sorted_list = set()
  while len(sorted_list) < lenght:
    sorted_list.add(random.randint(-3*lenght, 3*lenght))
  sorted_list = sorted(list(sorted_list))

  start = time.time()
  for target in sorted_list:
    naive_search(sorted_list, target)
  end = time.time()
  print("  Naive Search Time: ", (end - start)/lenght, "seconds")

  start = time.time()
  for target in sorted_list:
    binary_search(sorted_list, target)
  end = time.time()
  print("  Binary Search Time: ", (end - start)/lenght, "seconds")

if __name__ == '__main__': # good practice
  search()