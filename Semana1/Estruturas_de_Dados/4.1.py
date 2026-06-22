frutas = {"banana", "laranja", "uva"}

print(frutas)
print(type(frutas))
frutas.add("melancia")
frutas.add("banana")

if "laranja" in frutas:
    print("True")
else:
    print("False")

frutas.remove("uva")
frutas.discard("abacaxi")
print(frutas)
print(f"Tamanho do set: {len(frutas)}")


