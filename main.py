# Program Name: Password-Generator
# Author: woodsj1206 (https://github.com/woodsj1206)
# Description: A Python program that generates a password containing uppercase characters, lowercase characters, special characters, and digits.
# Date Created: 6/4/2026
# Last Modified: 7/11/2026

import secrets
import argparse

def parse_arguments():
  parser = argparse.ArgumentParser()
  
  parser.add_argument(
    "--num_upper_chars",
    type=int,
    default=2,
    help="The number of uppercase letters (A-Z) that will appear in the password. Default is 2."
  )
  
  parser.add_argument(
    "--num_lower_chars",
    type=int,
    default=3,
    help="The number of lowercase letters (a-z) that will appear in the password. Default is 3."
  )
  
  parser.add_argument(
    "--num_digits",
    type=int,
    default=2,
    help="The number of digits (0-9) that will appear in the password. Default is 2."
  )
  
  parser.add_argument(
    "--num_special_chars",
    type=int,
    default=1,
    help="The number of special characters that will appear in the password. Default is 1."
  )
  
  args = parser.parse_args()
  return args


def sample(sequence, n):
  if n > len(sequence) or n < 0:
    raise ValueError("Sample larger than length of sequence or is negative")
  if n == 0:
    return []

  res = []
  indices = [i for i in range(len(sequence))]

  for i in range(n):
    index = secrets.choice(indices)
    res.append(sequence[index])
    indices.remove(index)
  
  return res


def generate_password(num_upper_chars, num_lower_chars, num_digits, num_special_chars):
  capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  lowercase_letters = capital_letters.lower()
  digits = "0123456789"
  specials = "~!@#$%^&*()_+-=`{}|:\"<>?[]\\;',./"
  
  random_upper_chars = [secrets.choice(capital_letters) for i in range(num_upper_chars)]
  random_lower_chars = [secrets.choice(lowercase_letters) for i in range(num_lower_chars)]
  random_digits = [secrets.choice(digits) for i in range(num_digits)]
  random_special_chars = [secrets.choice(specials) for i in range(num_special_chars)]
  
  password = random_upper_chars + random_lower_chars + random_digits + random_special_chars
  shuffled_password = sample(password, len(password))

  return "".join(shuffled_password)


def main(args):
  num_upper_chars = args.num_upper_chars
  num_lower_chars = args.num_lower_chars
  num_digits = args.num_digits
  num_special_chars = args.num_special_chars

  password = generate_password(num_upper_chars, num_lower_chars, num_digits, num_special_chars)
  print("Password:", password)

if __name__ == "__main__":
  args = parse_arguments()
  main(args)