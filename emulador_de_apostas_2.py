import collections

# Recebendo a entrada do usuário
results = input("Digite os resultados separados por vírgula: ").split(',')

# Convertendo os resultados para sequências de números
numbers = [int(result) for result in results]

# Contando as ocorrências de cada número
counts = collections.Counter(numbers)

# Encontrando os números que mais e menos saíram
most_frequent = sorted(counts, key=counts.get, reverse=True)
least_frequent = sorted(counts, key=counts.get)

print("Números que mais saíram:")
for number in most_frequent:
  print(f"{number}: {counts[number]}")

print("Números que menos saíram:")
for number in least_frequent:
  print(f"{number}: {counts[number]}")

# Contando as ocorrências de sequências consecutivas de números
consecutives = collections.Counter()
for i in range(len(numbers) - 2):
  consecutives[tuple(numbers[i:i+3])] += 1

# Encontrando as sequências consecutivas de números que mais e menos saíram
most_frequent_consecutives = sorted(consecutives, key=consecutives.get, reverse=True)
least_frequent_consecutives = sorted(consecutives, key=consecutives.get)

print("Sequências consecutivas de números que mais saíram:")
for seq in most_frequent_consecutives:
  print(f"{seq}: {consecutives[seq]}")

print("Sequências consecutivas de números que menos saíram:")
for seq in least_frequent_consecutives:
  print(f"{seq}: {consecutives[seq]}")
