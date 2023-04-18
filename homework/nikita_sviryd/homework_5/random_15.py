import random

randoms = [random.random() for i in range(15)]

print(f" Максимум {max(randoms)}")
print(f"Минимум {min(randoms)}")
print(f"Сумма {sum(randoms)}")
print(f"Среднее {sum(randoms) / len(randoms)}")
