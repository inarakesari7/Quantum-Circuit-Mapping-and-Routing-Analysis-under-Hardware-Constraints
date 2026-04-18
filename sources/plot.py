import matplotlib.pyplot as plt

def plot_results(results):
    topologies = [r["topology"] for r in results]
    swaps = [r["swaps"] for r in results]
    depths = [r["depth"] for r in results]

    # Plot 1: SWAP count vs topology
    plt.figure()
    plt.bar(topologies, swaps)
    plt.title("SWAP Count vs Topology")
    plt.xlabel("Topology")
    plt.ylabel("Number of SWAP Gates")
    plt.savefig("results/swap_count.png")

    # Plot 2: Depth vs topology
    plt.figure()
    plt.bar(topologies, depths)
    plt.title("Circuit Depth vs Topology")
    plt.xlabel("Topology")
    plt.ylabel("Depth")
    plt.savefig("results/depth.png")

    plt.show()