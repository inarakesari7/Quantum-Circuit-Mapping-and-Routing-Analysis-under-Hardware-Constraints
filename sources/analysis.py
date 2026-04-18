from qiskit import transpile

def analyze(qc, coupling, name):
    # Map the circuit to the given hardware topology
    tqc = transpile(qc, coupling_map=coupling, optimization_level=0)

    # Extract metrics
    depth = tqc.depth()
    gate_counts = tqc.count_ops()
    total_gates = sum(gate_counts.values())
    swap_count = gate_counts.get('swap', 0)

    return {
        "topology": name,
        "depth": depth,
        "total_gates": total_gates,
        "swaps": swap_count
    }