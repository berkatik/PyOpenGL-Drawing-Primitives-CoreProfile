'''
	An object set. We can have different scenes for different views.
	We can have multiple scenes for different cameras.
	We can have multiple scenes for mirrors - can be low res than main scene.

	Here we can create different scenes like reflections with reference.
'''

class Scene:
	def __init__(self):
		self.nodes = []

	def add(self, node):
		self.nodes.append(node)

