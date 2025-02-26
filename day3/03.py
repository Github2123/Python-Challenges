text='hello world'
text_unique={char.lower() for char in text if char.isalpha()}
print(text_unique)