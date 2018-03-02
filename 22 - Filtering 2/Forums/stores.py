import itertools

class MemberStore():
	"""This class provides a way to Manage Members Information"""

	members = []
	last_id = 1

	def get_all(self):
		return MemberStore.members

	def get_by_id(self, id):
		for member in self.members:
			if member.id == id:
				return member

	def get_by_name(self, name):
		return (member for member in self.get_all() if member.name == name)

	def add(self, member):
		member.id = self.last_id
		self.members.append(member)
		self.last_id += 1

	def entity_exists(self, member):
		result = False
		if member is not None:
			if member is self.get_by_id(member.id):
				result = True
		return result

	def update (self, updated_member):
		members = self.get_all()
		for index, member in enumerate(members):
			if member.id == updated_member.id:
				members[index] = updated_member

	def delete(self, id):
		member = self.get_by_id(id)
		if member is not None:
			self.members.remove(member)

	def get_members_with_posts(self, posts):
		members = self.get_all()
		for member, post in itertools.product(members, posts):
			if post.member_id == member.id:
				member.posts.append(post)
		return members

	def get_top_members_with_posts(self):
		members = self.get_all()
		members.sort(key=lambda member: len(member.posts), reverse=True)
		return members[:2]

class PostStore():
	"""This class provides a way to Manage Posts Information"""

	posts = []
	last_id = 1

	def get_all(self):
		return self.posts

	def get_by_id(self, id):
		for post in self.posts:
			if post.id == id:
				return post

	def add(self, post):
		post.id = self.last_id
		self.posts.append(post)
		self.last_id += 1

	def entity_exists(self, post):
		result = False
		if post is not None:
			if post is self.get_by_id(post.id):
				result = True
		return

	def update (self, updated_post):
		posts = self.get_all()
		for index, post in enumerate(posts):
			if post.id == updated_post.id:
				posts[index] = updated_post

	def delete(self, id):
		post = self.get_by_id(id)
		if post is not None:
			self.posts.remove(post)