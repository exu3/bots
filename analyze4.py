import matplotlib.pyplot as plt


def load_history(filename):
    generations = []
    fitnesses = []

    with open(filename, "r") as f:
        for line in f:
            generation, fitness = line.strip().split()
            generations.append(int(generation))
            fitnesses.append(float(fitness))

    return generations, fitnesses


quad_g, quad_f = load_history("ffitness_history_quadruped.txt")
hex_g, hex_f = load_history("ffitness_history_hexapod.txt")

quad_distance = [-f for f in quad_f]
hex_distance = [-f for f in hex_f]

plt.plot(quad_g, quad_distance, marker="o", label="Quadruped")
plt.plot(hex_g, hex_distance, marker="o", label="Hexapod")

plt.xlabel("Generation")
plt.ylabel("Fitness level")
plt.title("Quadruped vs hexapod fitness over generations")
plt.legend()
plt.grid(True)
plt.show()
