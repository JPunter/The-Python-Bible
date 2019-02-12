#Email slicer project
#Get user email address
email = input("What is your email address?: ").strip()

#strip out name
name = email[:email.index("@")]

#strip out domain
domain = email[email.index("@") + 1:]

#print name and domain
output = "Your username is {} and your domain is {}!".format(name, domain)
print(output)
