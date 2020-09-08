"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        #create a queue to hold nodes to visit
        to_visit = Queue()

        #create a set to hold visited nodes
        visited = set()

        #Initialize: add teh starting node to the queue
        to_visit.enqueue(starting_vertex)

        #While queue not empty:
        while to_visit.size() > 0:

            #dequeue first entry
            current_node = to_visit.dequeue()
            #if not visited:
            if current_node not in visited:
                #Visit the node ( print it out)
                print(current_node)
                #add it to the visited set
                visited.add(current_node)
                #enqueue all its neighbors
                for node in self.get_neighbors(current_node):
                    to_visit.enqueue(node)
                

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #see bft pseudocode: Stack=Queue pop=dequeue push=enqueue
        to_visit = Stack()

        visited = set ()

        to_visit.push(starting_vertex)

        while to_visit.size() > 0:
            current_node = to_visit.pop()

            if current_node not in visited:
                print(current_node)
                visited.add(current_node)

                for node in self.get_neighbors(current_node):
                    to_visit.push(node)

    def dft_recursive(self, starting_vertex,  visited = set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
       
        #mark current node as visited

        visited.add(starting_vertex)
        print(starting_vertex)
        #save current node neighbors to a variable
        neighbors = self.get_neighbors(starting_vertex)

        #While current node has neighbors:
        while len(neighbors) > 0:
            #for each neighbor 
            for node in neighbors:
                #neighbor has not been visited
                if node not in visited:
                    #recurse making the neighbor the current node
                    self.dft_recursive(node, visited)
                #neighbor has been visited
                else:
                    return

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        to_search = Queue()

        to_search.enqueue([starting_vertex])

        # Create a Set to store visited vertices
        visited = set()

        # While the queue is not empty...
        while to_search.size() > 0:

            # Dequeue the first PATH
            current_path = to_search.dequeue()

            # Grab the last vertex from the PATH
            last_node = current_path[-1]

            # If that vertex has not been visited...
            if last_node not in visited:

                # CHECK IF IT'S THE TARGET
                if last_node == destination_vertex:

                    # IF SO, RETURN PATH
                    return current_path

                #if it's not the target
                else:
                    # Mark it as visited...
                    visited.add(last_node)

                    # Then add A PATH TO its neighbors to the back of the queue
                    for node in self.get_neighbors(last_node):
                        # COPY THE PATH
                        copy = current_path[:]

                        # APPEND THE NEIGHOR TO THE BACK
                        copy.append(node)

                        #add copy to the queue
                        to_search.enqueue(copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        to_search = Stack()
        to_search.push([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while to_search.size() > 0:
            # Dequeue the first PATH
            current_path = to_search.pop() 
            # Grab the last vertex from the PATH
            last_node = current_path[-1]
            # If that vertex has not been visited...
            if last_node not in visited:
                # CHECK IF IT'S THE TARGET
                if last_node == destination_vertex:
                    # IF SO, RETURN PATH
                    return current_path
                else:
                    # Mark it as visited...
                    visited.add(last_node)
                    # Then add A PATH TO its neighbors to the back of the queue
                    for node in self.get_neighbors(last_node):
                        # COPY THE PATH
                        copy = current_path[:]
                        # APPEND THE NEIGHOR TO THE BACK
                        copy.append(node)
                        to_search.push(copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, path = [], visited = set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """

        
        #add node to visited
        visited.add(starting_vertex)

        #make current path equal to previous path + node
        current_path = [*path, starting_vertex]
        
        #get last vertex of the path
        last_node  = current_path[-1]

        #check if its the target
        if last_node == destination_vertex:
            return current_path
        
        for neighbor in self.get_neighbors(starting_vertex):

            #check if each neighbor is in visited
            if neighbor not in visited:
                #repeat the steps above
                neighbor_path = self.dfs_recursive(neighbor, destination_vertex, current_path, visited)

                #unsure on this part but need it bc error was getting thrown
                if neighbor_path is not None:
                    return neighbor_path



if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
