languages = ['Python', 'Java', 'JavaScript']

enumerate_prime = enumerate(languages)

# converte um objeto enumerate em uma lista
print(f'{list(enumerate_prime)}\n')

# Saída: [(0, 'Python'), (1, 'Java'), (2, 'JavaScript')]

# Unpacking:
for index, language in enumerate(languages):
    print(f'{index} - {language}')
    
    
# Other Examples:
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(f'\n{list(enumerate(seasons))}')
# [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
print(list(enumerate(seasons, start=1)))
# [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
