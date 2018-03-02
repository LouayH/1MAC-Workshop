import models, stores

def create_members():
	member1 = models.Member("Manar", 23)
	member2 = models.Member("Nour", 21)
	member3 = models.Member("Zein", 21)
	member4 = models.Member("Rayan", 21)

	return member1, member2, member3, member4

def store_members(store, members):
	for member in members:
		store.add(member)

def update_member(store, member):
    copy = models.Member(member.name, member.age)
    copy.id = member.id

    copy.name = "Manar"
    store.update(copy)

def search_members_by_name(store, name):
    results = store.get_by_name("Manar")
    for member in results:
        print(member)

def create_posts():
    post1 = models.Post("First Post", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
    post2 = models.Post("Second Post", "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")
    post3 = models.Post("Third Post", "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.")

    return post1, post2, post3

def store_posts(posts, store):
	for post in posts:
		store.add(post)

members = create_members()
member_store = stores.MemberStore()
store_members (member_store, members)
update_member(member_store, members[3])
search_members_by_name(member_store, "Manar")

posts = create_posts()
post_store = stores.PostStore()
store_posts (posts, post_store)