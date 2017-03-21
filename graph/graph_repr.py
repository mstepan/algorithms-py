
class Graph:

    def __init__(self, undirected=True):
        self.undirected = undirected
        self.vertexes = {}

    def add_vertex(self, ver):
        if ver not in self.vertexes:
            self.vertexes[ver] = {}

    def add_edge(self, src, dest, weight=1):

        if src not in self.vertexes:
            self.vertexes[src] = {}

        if dest not in self.vertexes:
            self.vertexes[dest] = {}

        if dest not in self.vertexes[src]:
            self.vertexes[src][dest] = weight

        if self.undirected and src not in self.vertexes[dest]:
            self.vertexes[dest][src] = weight

    def adj_vertexes(self, ver):
        if ver not in self.vertexes:
            return {}
        return self.vertexes[ver]

    def dfs(self, initial_ver, pre_callback, post_callback):
        self.__dfs(initial_ver, set(), set(), {initial_ver: None}, pre_callback, post_callback)

    def __dfs(self, ver, visited, marked, parents, pre_callback, post_callback):

        pre_callback(ver)
        marked.add(ver)

        for adj_ver in self.vertexes[ver].keys():

            if adj_ver in marked and adj_ver not in visited and parents[ver] != adj_ver:
                print("back: %s->%s" % (ver, adj_ver))

            elif adj_ver in visited and parents[ver] != adj_ver:
                print("forward: %s->%s" % (ver, adj_ver))

            elif adj_ver not in visited and adj_ver not in marked:
                print("tree: %s->%s" % (ver, adj_ver))
                parents[adj_ver] = ver
                self.__dfs(adj_ver, visited, marked, parents, pre_callback, post_callback)

        visited.add(ver)
        post_callback(ver)



    def bfs(self):
        pass

    def __str__(self):

        buf = ""

        for ver, edges in self.vertexes.items():
            buf += ver + " -> "

            for dest, weight in edges.items():
                buf += "(%s, %s), " % (dest, weight)

            buf += "\n"

        return buf

    def __repr__(self):
        return "Graph()"
