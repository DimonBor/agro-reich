import networkx as nx

island_map = nx.Graph()

nodes = {
    'bed_1': (154.590, 74.986),
    'bed_2': (144.968, 95.194),
    'bed_3': (144.791, 135.619),
    'bed_4': (114.983, 95.315),
    'bed_5': (105.026, 115.314),
    'bed_6': (175.092, 145.092),
    'bed_7': (195.049, 145.213),
    'bed_8': (194.614, 164.926),
    'bed_9': (214.654, 165.135),
    'bed_10': (224.736, 124.853),
    'bed_11': (224.756, 94.805),
    'bed_12': (204.592, 74.982),
    'bed_13': (274.953, 125.394),
    'bed_14': (264.769, 95.055),
    'bed_15': (294.769, 95.248),
    'bed_16': (184.840, 115.204),
    'isle_start': (181.148, 89.124),
    'corner_1': (225.083, 109.636),
    'corner_2': (264.746, 109.528),
    'travel': (180.233, 54.623)
}

island_map.add_nodes_from([
    'bed_1',
    'bed_2',
    'bed_3',
    'bed_4',
    'bed_5',
    'bed_6',
    'bed_7',
    'bed_8',
    'bed_9',
    'bed_10',
    'bed_11',
    'bed_12',
    'bed_13',
    'bed_14',
    'bed_15',
    'bed_16',
    'isle_start',
    'corner_1',
    'corner_2',
    'travel'
    ])

island_map.add_edge('isle_start', 'travel')
island_map.add_edge('isle_start', 'bed_1')
island_map.add_edge('bed_1', 'bed_2')
island_map.add_edge('bed_2', 'bed_3')
island_map.add_edge('bed_3', 'bed_4')
island_map.add_edge('bed_4', 'bed_5')
island_map.add_edge('bed_3', 'bed_6')
island_map.add_edge('bed_6', 'bed_16')
island_map.add_edge('bed_6', 'bed_7')
island_map.add_edge('bed_7', 'bed_8')
island_map.add_edge('bed_7', 'bed_10')
island_map.add_edge('bed_8', 'bed_9')
island_map.add_edge('bed_9', 'bed_10')
island_map.add_edge('bed_10', 'bed_11')
island_map.add_edge('bed_10', 'corner_1')
island_map.add_edge('corner_1', 'bed_11')
island_map.add_edge('corner_1', 'corner_2')
island_map.add_edge('corner_2', 'bed_13')
island_map.add_edge('corner_2', 'bed_14')
island_map.add_edge('bed_14', 'bed_15')
island_map.add_edge('bed_11', 'bed_12')
island_map.add_edge('bed_12', 'isle_start')

test_path = [
    (161, 92),
    (160, 141),
    (211, 144),
    (208, 92),
    (161, 92)
]


def find_path(start, finish):
    nodes_path = nx.shortest_path(
        island_map, source=start, target=finish
        )

    path = [nodes[node] for node in nodes_path]

    return path
