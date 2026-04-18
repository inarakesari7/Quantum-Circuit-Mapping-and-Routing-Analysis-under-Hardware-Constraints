from qiskit.transpiler import CouplingMap

def get_topologies():
    # Line topology: 0 - 1 - 2 - 3 - 4
    line = CouplingMap([
        [0, 1], [1, 2], [2, 3], [3, 4]
    ])

    # Ring topology: 0 - 1 - 2 - 3 - 4 - 0
    ring = CouplingMap([
        [0, 1], [1, 2], [2, 3], [3, 4], [4, 0]
    ])

    # Grid topology (approximate 2D connectivity)
    grid = CouplingMap([
        [0, 1], [1, 2],
        [0, 3], [1, 4], [2, 5],
        [3, 4], [4, 5]
    ])

    return {
        "Line": line,
        "Ring": ring,
        "Grid": grid
    }