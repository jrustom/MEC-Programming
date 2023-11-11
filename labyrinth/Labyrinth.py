import networkx as nx
import matplotlib.pyplot as plt
import json
import heapq
import os

class Labyrinth:

    def __init__(self, filename):
        self.labyrinth = self.read_json(filename)

        self.graph, self.start, self.end = self.generate_graph()

    def generate_graph(self):
        '''
        This function uses the JSON object obtained from read_json, fetching the tiles, start position, and end position.
        It iterates over the tile data to create the graph.
        For each tile, it checks if it's a wall tile;
        If so, it moves on.
        Otherwise, it takes the a, r, c values and adds a node to the graph.

        https://en.wikipedia.org/wiki/Hexagonal_Efficient_Coordinate_System

        It generates the positions of the 6 potential neighboring nodes based on the coordinate information provided in the link:
        https://en.wikipedia.org/wiki/File:HECS_Nearest_Neighbors.png

        While iterating over the coordinates, it checks if any of the corresponding nodes already exist in the graph.
        If yes, it adds an edge between them; otherwise, it does nothing.

        Returns:
        G (networkx.Graph): Graph object representing the labyrinth.
        start_position (tuple): Tuple containing the (a, r, c) coordinates of the starting position.
        end_position (tuple): Tuple containing the (a, r, c) coordinates of the ending position.
        '''

        labyrinth_data = self.labyrinth["tiles"]
        start_position = (self.labyrinth["start"]["a"], self.labyrinth["start"]["r"], self.labyrinth["start"]["c"])
        end_position = (self.labyrinth["end"]["a"], self.labyrinth["end"]["r"], self.labyrinth["end"]["c"])

        G = nx.Graph()

        for tile_data in labyrinth_data:
            hex_tile = tile_data[0]
            tile_type = tile_data[1]["type"]


            a = hex_tile["a"]
            r = hex_tile["r"]
            c = hex_tile["c"]

            position = (a, r, c)


            if tile_type != "TileType.WALL":
                G.add_node(position)

                # Check neighbors and add edges
                neighbors = [
                    (1 - a, r - ( 1 - a), c - (1 - a)), # top left
                    (1 - a, r - ( 1 - a), c + a), # top right
                    (a, r, c - 1), # left
                    (a, r, c + 1), # right
                    (1 - a, r + a, c - ( 1 - a)), # bottom left
                    (1 - a, r + a, c + a), # bottom right
                ]

                for neighbor in neighbors:
                    if neighbor in G.nodes:
                        G.add_edge(position, neighbor)


        return G, start_position, end_position

    def read_json(self, filename):
        '''
        Basic function to read from JSON file at filename

        Returns:
        data: json python object of labyrinth
        '''
        with open(filename, 'r') as file:
            data = json.load(file)
        return data

    def dijkstra(self):
        '''
        Implements boiler plate Dijkstra's algorithm for finding the shortest path in a graph.
        This algorithm is modified for the specific use case of the labyrinth problem.
        Modifications include setting all weights to 0

        Taken and modified from here:
        https://brilliant.org/wiki/dijkstras-short-path-finder/

        Returns:
        path: List of node coordingates representing the shortest path from the start to the end.
        An empty list is returned if no path is found.
        '''

        # Initialize distances and predecessors
        distances = {node: float('inf') for node in self.graph.nodes}
        predecessors = {node: None for node in self.graph.nodes}
        distances[self.start] = 0

        # Priority queue to store nodes and their distances
        priority_queue = [(0, self.start)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_node == self.end:
                # Reconstruct the path
                path = []
                while current_node is not None:
                    path.insert(0, current_node)
                    current_node = predecessors[current_node]
                return path

            for neighbor in self.graph.neighbors(current_node):
                weight = 1  # Uniform weight graph due to use case
                new_distance = distances[current_node] + weight

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = current_node
                    heapq.heappush(priority_queue, (new_distance, neighbor))

        return []


def write(path, output_filename):
    '''
    Used for submission
    Writes the path of dijkstras to the output file
    '''

    with open(output_filename, 'w') as file:
        for node in path:
            file.write(f"{node}\n")

if __name__ == "__main__":

    showGraph = False # used for demo, when set to true will display graph and path

    # Generate a visual representation of graph for demo
    if showGraph:
        filename = 'Labyrinth/labyrinths/easy/labyrinth_00.json'
        test = Labyrinth(filename)

        path = test.dijkstra()

        layout = nx.spring_layout(test.graph)

        plt.figure(figsize=(10, 8))
        nx.draw(test.graph, pos=layout, with_labels=True, node_color=["green" if node == test.start else "red" if node == test.end else "lightblue" for node in test.graph.nodes], font_size=8, node_size=300, font_color="black")

        path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(test.graph, pos=layout, edgelist=path_edges, edge_color='blue', width=3)

        plt.title("Hexagonal Graph")
        plt.show()

    else:

        # iterate over difficulties for testing script
        difficulties = ["easy", "hard", "extreme"]

        for diff in difficulties:
            input_folder = f"Labyrinth/labyrinths/{diff}/"

            output_folder = f"Labyrinth/solutions/{diff}/"

            # iterate over all mazes
            for filename in os.listdir(input_folder):
                input_filepath = os.path.join(input_folder, filename)
                output_filepath = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.txt")

                test = Labyrinth(input_filepath)
                path = test.dijkstra()

                if path:
                    write(path, output_filepath)
                    print(f"Solution for {filename} written to {output_filepath}")
