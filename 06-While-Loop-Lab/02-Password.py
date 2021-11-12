username = input()
correct_password = input()
attempt_password = input()

while attempt_password != correct_password:
   attempt_password = input()

print(f"Welcome {username}!")
