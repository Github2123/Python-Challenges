#Given a sentence, use a dictionary comprehension to count the frequency of each word in
#the sentence.
sentence="the quick brown fox jumps over the lazy dog"
s=sentence.split()
words_count={a:s.count(a) for a in s}
print(words_count)