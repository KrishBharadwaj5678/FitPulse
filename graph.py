import matplotlib.pyplot as plt

def showGraph(repNum,repSpeed):
    # Workout Graph
    plt.figure(figsize=(8,5))  # Creates a new graph window, Width=8, Height=5
    plt.plot(repNum,repSpeed,marker="o",linewidth=2)
    plt.title("FitPulse Analysis")
    plt.xlabel("Total Push-ups")
    plt.ylabel("Seconds per Push-up")
    plt.grid(True)

    # Save the graph
    plt.savefig("FitPulse.png",dpi=300,bbox_inches='tight')
    plt.show()