from sys import argv
script, filename = argv

txt = open(filename)
print(f"Here's your file {filename}")
print(txt.read())
print("-"*20)

print("Type the filename in again: ")
file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())

txt.close()
txt_again.close()
