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


quad_g, quad_f = load_history("fitness_history_quadruped.txt")
hex_g, hex_f = load_history("fitness_history_hexapod.txt")

plt.plot(quad_g, quad_f, marker="o", label="Quadruped")
plt.plot(hex_g, hex_f, marker="o", label="Hexapod")

plt.xlabel("Generation")
plt.ylabel("Best Fitness")
plt.title("Quadruped vs Hexapod Fitness Over Generations")
plt.legend()
plt.grid(True)
plt.show()
