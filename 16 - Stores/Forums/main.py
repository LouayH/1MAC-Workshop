import models, stores

member1 = models.Member("Manar", 23)
member2 = models.Member("Nour", 21)

post1 = models.Post("First Post", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
post2 = models.Post("Second Post", "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")
post3 = models.Post("Third Post", "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.")

member_store = stores.MemberStore()
member_store.add(member1)
member_store.add(member2)

post_store = stores.PostStore()
post_store.add(post1)
post_store.add(post2)
post_store.add(post3)

print (member_store.get_all())
print (post_store.get_all())