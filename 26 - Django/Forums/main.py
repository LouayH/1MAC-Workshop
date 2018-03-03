import models, stores
from time import sleep

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
    post1 = models.Post("1st Post", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",1)
    sleep(0.1)
    post2 = models.Post("2nd Post", "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.", 3)
    sleep(0.1)
    post3 = models.Post("3rd Post", "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.", 2)
    sleep(0.1)
    post4 = models.Post("4th Post", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", 4)
    sleep(0.1)
    post5 = models.Post("5th Post", "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.", 1)
    sleep(0.1)
    post6 = models.Post("6th Post", "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.", 3)
    sleep(0.1)
    post7 = models.Post("7th Post", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", 1)
    sleep(0.1)
    post8 = models.Post("8th Post", "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.", 3)
    sleep(0.1)
    post9 = models.Post("9th Post", "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.", 1)

    return post1, post2, post3, post4, post5, post6, post7, post8, post9

def store_posts(posts, store):
	for post in posts:
		store.add(post)

def view_members_with_posts(store, posts):
    members_with_posts = store.get_members_with_posts(posts)
    for member in members_with_posts:
        print("{0} has posts".format(member.name))
        for post in member.posts:
            print("\t{0}".format(post.title))

def view_top_members_with_posts(store):
    print ("** Top Members with Posts **")
    top_members_with_posts = store.get_top_members_with_posts()
    for member in top_members_with_posts:
        print("{0} has {1} posts".format(member.name, len(member.posts)))

def view_posts_by_date(store):
    posts_by_date = store.get_posts_by_date()
    for post in posts_by_date:
        print("{0} created at {1}".format(post.title, post.date))

members = create_members()
member_store = stores.MemberStore()
store_members (member_store, members)
#update_member(member_store, members[3])
#search_members_by_name(member_store, "Manar")

posts = create_posts()
post_store = stores.PostStore()
store_posts (posts, post_store)

#view_members_with_posts(member_store, post_store.posts)
#view_top_members_with_posts(member_store)

view_posts_by_date(post_store)