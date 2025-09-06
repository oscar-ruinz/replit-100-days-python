import os

adminUser = os.environ['AdminUser']
adminPass = os.environ['AdminPass']

normalUser = os.environ['NormyUser']
normalUserPass = os.environ['NormyPass']

print("🌟Login System🌟\n")

username = input("Username > ")
print()
password = input("Password > ")
print()

if username == adminUser and password == adminPass:
  print("Hello admin.")
elif username == normalUser and password == normalUserPass:
  print(f"Hello {normalUser}.")
else:
  print("I don't know you.")