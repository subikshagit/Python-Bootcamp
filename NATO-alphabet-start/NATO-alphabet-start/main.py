
#TODO 1. Create a dictionary in this format 
import pandas as pd

data = pd.read_csv('nato.csv')
print(data)
d = {key:value for (key, value) in zip(data.letter, data.code)}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
output = [d[letter] for letter in word if letter in d]
print(output)
