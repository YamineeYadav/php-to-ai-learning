email = input("Enter Your Email: ").strip()
# email.split()
breakmail  = email.split('@')
username= breakmail[0]
userdomain= breakmail[1]
print("user name is",  username )
print("user domain is",  userdomain )