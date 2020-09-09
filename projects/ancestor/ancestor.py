#will be given a dataset which is a list of ancestors like so: [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    #(parent, child)
#also given a starting node
# result will be the ancestor node that is fartest away from the start
# if there is more than one 'farthest path' the smallest ID will be returned
# if starting node has no parents, return -1

#Planning:
# ancestors need to be loaded into a graph. 
    # the tuples are edges
    # probably need to check all the numbers in the tuples and eliminate the duplicates to add vertices 
#DFS----modify it to keep track of the longest path and replace if necessary
    #edge case: if there is more than 1 longest path
    #base case: if there are no parents

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()
    
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    #add vertices to the graph
    for pair in ancestors:
        #check the parent
        if pair[0] not in graph.vertices:
            graph.add_vertex(pair[0])
        #check the child
        if pair[1] not in graph.vertices:
            graph.add_vertex(pair[1])
    
    #add edges >>> I switched the order so child points to parent 
    for pair in ancestors:
        graph.add_edge(pair[1], pair[0])

    ### Begin DFS ###
    s = Stack()
    visited = set()
    s.push([starting_node])
    
    #add variable to store longest path
    longest_path = []

    while s.size() > 0:
        current_path = s.pop()
        last_node = current_path[-1]

        #check if size of path is bigger
        if len(current_path) > len(longest_path):
            longest_path = current_path
        
        #check if size of path is equal ???not sure if this section is needed 
        if len(current_path) == len(longest_path):
            #check for the smaller last_node
            if current_path[-1] < longest_path[-1]: 
                longest_path = current_path

        if last_node not in visited:
            visited.add(last_node)

            parents = graph.get_neighbors(last_node)

            for parent in parents:
                new_path = [*current_path, parent]
                s.push(new_path)
    
    #check for base case of no parents
    if starting_node == longest_path[-1]:
        return -1
    else:
        return longest_path[-1]
    
a = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

b = a = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (11, 5), (11, 8), (8, 9), (4, 8), (10, 1)]
print(earliest_ancestor(b, 9))