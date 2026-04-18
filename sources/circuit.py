from qiskit import QuantumCircuit

def create_circuit():
    qc = QuantumCircuit(5)

    qc.h(0)
    qc.cx(0, 3)
    qc.cx(1, 4)
    qc.cx(2, 3)
    qc.cx(0, 2)
    qc.h(4)

    return qc