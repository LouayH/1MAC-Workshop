class MemberStore():
	"""This class provides a way to Manage Members Information"""

	members = []
	last_id = 1

	def get_all(self):
		return MemberStore.members

	def add(self, member):
		member.id = self.last_id
		self.members.append(member)
		self.last_id += 1

class PostStore():
	"""This class provides a way to Manage Posts Information"""

	posts = []
	last_id = 1

	def get_all(self):
		return self.posts

	def add(self, post):
		post.id = self.last_id
		self.posts.append(post)
		self.last_id += 1