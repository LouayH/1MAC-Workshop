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

	def delete(self, id):
		member = self.get_by_id(id)
		if member is not None:
			self.members.remove(member)

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
		return result

	def delete(self, id):
		post = self.get_by_id(id)
		if post is not None:
			self.posts.remove(post)