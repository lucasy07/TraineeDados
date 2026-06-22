A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
C = {7, 8, 9, 10}

print(f"União: {A.union(B)}")
print(f"União: {A | B}")

print(f"Intersecção: {A.intersection(B)}")
print(f"Intersecção: {A & B}")

print(f"Diferença: {A.difference(B)}")
print(f"Diferença: {A - B}")

print(f"Diferença simétrica: {A.symmetric_difference(B)}")

print(f"Intersecção entre B e C: {B & C}")

print(f"União entre A, B e C: {A | B | C}")
