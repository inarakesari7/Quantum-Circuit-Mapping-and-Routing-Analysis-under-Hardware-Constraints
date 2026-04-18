from circuit import create_circuit
from topologies import get_topologies
from analysis import analyze
from plot import plot_results

def main():
    # Step 1: Create base circuit
    qc = create_circuit()

    print("Base Circuit:\n")
    print(qc)
    print("\n--- Running Analysis ---\n")

    # Step 2: Get hardware topologies
    topologies = get_topologies()

    results = []

    # Step 3: Analyze circuit under each topology
    for name, topo in topologies.items():
        res = analyze(qc, topo, name)
        results.append(res)
        print(res)

    # Step 4: Plot results
    plot_results(results)

if __name__ == "__main__":
    main()