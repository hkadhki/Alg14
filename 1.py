import numpy as np

supply = [100, 200]
demand = [50, 100, 75, 75]
costs = [
    [4, 3, 5, 6],
    [8, 2, 4, 7],
]

x = np.zeros((len(supply), len(demand)), dtype=int)

remaining_supply = supply.copy()
remaining_demand = demand.copy()

while any(remaining_supply) and any(remaining_demand):
    min_cost = float('inf')
    min_i, min_j = -1, -1
    for i in range(len(supply)):
        for j in range(len(demand)):
            if remaining_supply[i] > 0 and remaining_demand[j] > 0 and costs[i][j] < min_cost:
                min_cost = costs[i][j]
                min_i, min_j = i, j

    quantity = min(remaining_supply[min_i], remaining_demand[min_j])
    x[min_i][min_j] = quantity
    remaining_supply[min_i] -= quantity
    remaining_demand[min_j] -= quantity

total_cost = sum(x[i][j] * costs[i][j] for i in range(len(supply)) for j in range(len(demand)))

print("Минимальная стоимость перевозок:", total_cost)
print("План перевозок:")
for i in range(len(supply)):
    for j in range(len(demand)):
        if x[i][j] > 0:
            print(f"Склад {i + 1} -> Магазин {j + 1}: {x[i][j]} единиц")