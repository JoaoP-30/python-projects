# Mad Libs Game

# Este programa é um jogo de Mad Libs que permite ao usuário criar 
# uma história engraçada preenchendo espaços em branco com palavras 
# fornecidas pelo usuário. O programa solicita ao usuário que insira adjetivos, 
# substantivos e verbos, e depois gera uma história completa usando essas palavras.

adjective1 = input("Enter an adjective (description of something): ")
noun1 = input("Enter a noun (person, place, or thing): ")
adjective2 = input("Enter another adjective (description of something): ")
verb1 = input("Enter a verb ending in -ing: ")
adjective3 = input("Enter one more adjective (description of something): ")

print(f"\nToday I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw a {noun1}") 
print(f"{noun1} was {adjective2} and {verb1}.")
print(f"I was {adjective3}!\n")