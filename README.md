# Quantum-Circuit-Mapping-and-Routing-Analysis-under-Hardware-Constraints
# Overview
This project analyzes how quantum hardware connectivity impacts circuit execution. A fixed quantum circuit is mapped onto different qubit topologies (line, ring, grid) to study routing overhead introduced during transpilation.

# Objective
To quantify the effect of limited qubit connectivity on:
Circuit depth
Gate count
SWAP insertion (routing overhead)

# Methodology
Designed a 5-qubit circuit with non-local interactions
Defined three hardware topologies: line, ring, and grid
Used Qiskit to transpile the circuit under each constraint
Measured depth, total gates, and SWAP count for comparison

# Results
Increasing connectivity reduced SWAP insertion and overall gate count
Grid topology showed the lowest routing overhead and best execution efficiency
Circuit depth did not strictly correlate with SWAP count due to scheduling effects

# Key Insight
Hardware connectivity significantly influences quantum circuit efficiency, but improvements in connectivity do not always translate linearly to reduced execution depth due to transpiler-driven gate scheduling.

# Tech Stack
Python
Qiskit
Matplotlib
