#This is an example project, showing a program that analyzes a sample file to find what percentage of the text each character occupies.
# This section shows how a file could be open and read.

def count_char(text, char):
  count = 0
  for c in text:
    if c == char:
      count += 1
  return count

filename = "text_file1.txt"

with open(filename) as f:
   text = f.read()



for char in "abcdefghijklmnopqrstuvwxyz":
  perc = 100 * count_char(text, char) / len(text)
  print("{0} - {1}%".format(char, round(perc, 2)))
  # a - 4.11 %
  # b - 2.57 %
  # c - 3.08 %
  # d - 0.0 %
  # e - 4.11 %
  # f - 6.43 %
  # g - 10.28 %
  # h - 3.08 %
  # i - 0.26 %
  # j - 0.0 %
  # k - 0.51 %
  # l - 1.8 %
  # m - 0.0 %
  # n - 5.91 %
  # o - 2.31 %
  # p - 3.34 %
  # q - 1.54 %
  # r - 10.8 %
  # s - 1.03 %
  # t - 1.29 %
  # u - 3.08 %
  # v - 6.94 %
  # w - 0.0 %
  # x - 0.26 %
  # y - 5.14 %
  # z - 1.29 %