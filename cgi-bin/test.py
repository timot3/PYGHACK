#! /usr/bin/env python3

print("Content-Type: application/json")
print()

print('{"hello": "world"}')

file = open("copy.txt", "w")
file.write("Your text goes here")
file.close()
