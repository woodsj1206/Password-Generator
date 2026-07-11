# Program Name: Password-Generator
# Author: woodsj1206 (https://github.com/woodsj1206)
# Description: A Python program that generates a password containing uppercase characters, lowercase characters, special characters, and digits.
# Date Created: 6/4/2026
# Last Modified: 7/11/2026

import random
import argparse

def parse_arguments():
  parser = argparse.ArgumentParser()
  
  parser.add_argument(
    "--num_upper_chars",
    type=int,
    default=2,
    help="The number of uppercase letters (A-Z) that will appear in the password."
  )
  
  parser.add_argument(
    "--num_lower_chars",
    type=int,
    default=3,
    help="The number of lowercase letters (a-z) that will appear in the password."
  )
  
  parser.add_argument(
    "--num_digits",
    type=int,
    default=2,
    help="The number of digits (0-9) that will appear in the password."
  )
  
  parser.add_argument(
    "--num_special_chars",
    type=int,
    default=1,
    help="The number of special characters that will appear in the password."
  )
  
  args = parser.parse_args()
  return args


def generate_password(num_upper_chars, num_lower_chars, num_digits, num_special_chars):
  capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  lowercase_letters = capital_letters.lower()
  digits = "0123456789"
  specials = "~!@#$%^&*()_+-=`{}|:\"<>?[]\\;',./"
  
  random_upper_chars = [random.choice(capital_letters) for i in range(num_upper_chars)]
  random_lower_chars = [random.choice(lowercase_letters) for i in range(num_lower_chars)]
  random_digits = [random.choice(digits) for i in range(num_digits)]
  random_special_chars = [random.choice(specials) for i in range(num_special_chars)]
  
  password = random_upper_chars + random_lower_chars + random_digits + random_special_chars
  shuffled_password = random.sample(password, len(password))

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