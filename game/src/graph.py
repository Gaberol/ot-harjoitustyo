class Graph:
    def __init__(self, board_map) -> None:
        self.board = []
        for i in range(len(board_map)):
            self.board.append([(j,i) for j in range(len(board_map[0])) if board_map[i][j][0] > 0])
        self.board_height = len(self.board)
        self.board_width = len(self.board[0])
        self.board_size = self.board_height * self.board_width
        self.adj_lists = {}

        self._construct_adj_lists()


    def _construct_adj_lists(self):
        for i in range(self.board_height):
            for j in range(self.board_width):
                not_a_tile = True
                for k in self.board:
                    if (j,i) in k:
                        print((j,i))
                        not_a_tile = False
                if not_a_tile: 
                    print("disqualified") 
                    continue
                self.adj_lists[(j,i)] = []
                if i%2 == 0:
                    cases = [(j+1,i), (j,i+1), (j-1,i+1), (j-1,i), (j,i-1), (j-1,i-1)]
                else:
                    cases = [(j+1,i), (j,i+1), (j+1,i-1), (j-1,i), (j,i-1), (j+1,i+1)]
                for case in cases:
                    for k in self.board:
                        if case in k:
                            self.adj_lists[(j,i)].append(case)

    def _dfs(self, node, visited):
        if visited[node]:
            return
        visited[node] = True
        for edge in self.adj_lists[node]:
            self._dfs(edge, visited)

    def is_connected(self):
        visited = {}
        for i in self.adj_lists.keys():
            visited[i] = False
        print(self.board)
        print(self.adj_lists)
        print(visited)
        self._dfs(self.board[0][0], visited)

if __name__ == "__main__":
    board_map = [[(0,0), (2,0), (2,0), (2,0), (0,0), (0,0), (3,0), (3,0)],
                [(0,0), (0,0), (2,1), (2,0), (0,0), (0,0), (3,0), (3,0)],
                [(1,0), (1,0), (2,0), (0,0), (2,0), (3,0), (3,1), (0,0)],
                [(1,0), (1,0), (1,0), (0,0), (2,0), (3,0), (3,0), (4,0)],
                [(0,0), (1,0), (0,0), (1,0), (4,0), (4,1), (4,0), (4,0)],
                [(0,0), (0,0), (1,0), (1,0), (0,0), (0,0), (4,0), (4,0)],
                [(0,0), (1,0), (1,1), (0,0), (0,0), (4,0), (4,0), (0,0)],
                [(0,0), (1,0), (1,0), (4,0), (4,0), (4,0), (4,0), (0,0)]]

    goo = Graph(board_map)
    goo.is_connected()