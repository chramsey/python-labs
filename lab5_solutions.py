""" (1) STANFORD PREREQS """

type(a) # => <class 'lab5test.Course'>
isinstance(a, Course) # => True
isinstance(b, Course) # => True
type(a) == type(b) # => False
a == b # => False

# ADDITIONAL ATTRIBUTES
class Course:
	def __init__(self, department, number, title):
		self.department = department
		self.number = number
		self.title = title
		self.students_here = set()	

	def mark_attendance(self, *students):
		for s in students:
			self.students_here.add(s)

	def is_present(self, student):
		return student in self.students_here
	
# IMPLEMENTING PREREQUISITES
	def __gt__(self, other):
		if isinstance(other, Course):
			def stripLetters(num):
				return int(''.join(filter(lambda x: x.isdigit(), num)))
			return stripLetters(self.number) > stripLetters(other.number)
		
# INSTRUCTORS (CHALLENGE)

""" (2) SIMPLE GRAPH """

class Vertex:
	def __init__(self, name=""):
		self.name = name
		edges = set()

	def __repr__(self):
		return "Vertex({})".format(self.name)

class Edge:
	def __init__(self, start, end, cost=1, visited=False):
		self.start = start
		self.end = end
		self.cost = float(cost)
		self.visited = visited

	def __repr__(self):
		return "Edge(Start: {e_start}, End: {e_end}, Cost: {e_cost}, Visited: {e_visit}" \
			.format(e_start = self.start, e_end = self.end, e_cost = e.cost, e_visit = e.visited)

class SimpleGraph:
	def __init__(self):
		self.verts = []
		self.edges = []

	def add_vertex(self, v):
		if type(v) == Vertex:
			self.verts.append(v)

	# remember - edges are directed
	def add_edge(self, v_start, v_end):
		if type(v_start) == Vertex and type(v_end) == Vertex and v_start in self.verts and v_end in self.verts:
			e = Edge(v_start, v_end)
			self.edges.append(e)

	def contains_vertex(self, v):
		if type(v) == Vertex:
			return v in self.verts

	def contains_edge(self, v_start, v_end):
		if type(v_start) == Vertex and type(v_end) == Vertex:
			for e in self.edges:
				if e.start == v_start and e.end == v_end:
					return True
		return False

	def get_neighbors(v):
		if type(v) == Vertex:
			return [e.end for e in self.edges if e.start == v]
		return []

	def is_empty(self):
		return not self.edges

	def size(self):
		return len(edges)

	def remove_vertex(self, v):
		if type(v) == Vertex:
			# remove vertex from graph
			if v in self.verts:
				self.verts.remove(v)
			# remove any edges connected to v
			for e in self.edges:
				if e.start == v or e.end == v:
					self.edges.remove(e)

	def remove_edge(self, v_start, v_end):
		if type(v_start) == Vertex and type(v_end) == Vertex:
			for e in self.edges:
				if e.start == v_start and e.end == v_end:
					self.edges.remove(e)

	def is_neighbor(self, v_start, v_end):
		if type(v_start) == Vertex and type(v_end) == Vertex:
			return v_end in self.get_neighbors(v_start)
		return False

	# DFS search
	def is_reachable(self, v_1, v_2):
		stack = [v_1]
		visited = set()
		while stack:
			v_curr = stack.pop()
			if v_curr == v_2:
				return True
			if v_curr not in visited:
				visited.add(v_curr)
				stack += list(filter(lambda x: x not in visited, get_neighbors(v)))
		return False

	def clear_all():
		self.edges = []
		self.verts = []

	def __repr__(self):
		verts = ', '.join([v.name for v in self.verts])
		edges = ', '.join([(e.start, e.end, e.cost, e.visited) for e in self.edges])
		return "Vertices: [{verts}] \nEdges: [{edges}]".format(verts = verts, edges = edges)
		
		
## CHALLENGE: GRAPH ALGORITHMS	

## CHALLENGE: USING MAGIC METHODS
		
""" (3) TIMED KEY-VALUE STORE (CHALLENGE) """
		
		

