''' MAPEAMENTO '''


import collections

# Recebendo a entrada do usuário
results = input("Digite os resultados separados por vírgula: ").split(',')

# Convertendo os resultados para sequências de números
numbers = [result for result in results]

# Contando as ocorrências de cada número e unidade da milhar
counts = collections.Counter(''.join(numbers))
units = [collections.Counter(result[i] for result in results) for i in range(4)]

# Encontrando os números que mais e menos saíram
most_frequent = sorted(counts, key=counts.get, reverse=True)
least_frequent = sorted(counts, key=counts.get)

print("Números que mais saíram:", most_frequent)
print("Números que menos saíram:", least_frequent)

# Encontrando as unidades da milhar que mais e menos saíram
most_frequent_units = [sorted(unit, key=unit.get, reverse=True) for unit in units]
least_frequent_units = [sorted(unit, key=unit.get) for unit in units]

print("Unidades da milhar que mais saíram:", most_frequent_units)
print("Unidades da milhar que menos saíram:", least_frequent_units)

# Contando as ocorrências de sequências consecutivas de números
consecutives = collections.Counter()
for number in numbers:
  for i in range(len(number) - 2):
    consecutives[number[i:i+3]] += 1

# Encontrando as sequências consecutivas de números que mais e menos saíram
most_frequent_consecutives = sorted(consecutives, key=consecutives.get, reverse=True)
least_frequent_consecutives = sorted(consecutives, key=consecutives.get)

print("Sequências consecutivas de números que mais saíram:", most_frequent_consecutives)
print("Sequências consecutivas de números que menos saíram:", least_frequent_consecutives)
