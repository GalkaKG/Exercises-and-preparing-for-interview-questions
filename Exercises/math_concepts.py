import random


# Simple Monte Carlo simulation to estimate the probability of getting a 6 in a dice roll
def monte_carlo_simulation(num_trials):
    successes = 0
    for _ in range(num_trials):
        if random.randint(1, 6) == 6:
            successes += 1
    return successes / num_trials


# Run simulation with 100,000 trials
probability = monte_carlo_simulation(100_000)
print(f"Estimated probability of rolling a 6: {probability}")
