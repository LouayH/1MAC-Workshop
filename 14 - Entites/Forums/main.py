import models

member1 = models.Member("Manar", 23)
member2 = models.Member("Nour", 21)

post1 = models.Post("First Post", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
post2 = models.Post("Second Post", "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")
post3 = models.Post("Third Post", "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.")

print (member1)
print (member2)

print (post1)
print (post2)
print (post3)