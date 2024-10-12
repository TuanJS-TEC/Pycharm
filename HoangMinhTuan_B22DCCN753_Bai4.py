import matplotlib.pyplot as plt

def word_frequency(text):

  words = text.lower().split()
  word_freq = {}
  for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1
  sorted_words = sorted(word_freq.items(), key=lambda item: item[1], reverse=True)
  return word_freq, sorted_words

def plot_histogram(sorted_words):

  top_words = dict(sorted_words[:10])
  plt.bar(top_words.keys(), top_words.values())
  plt.title("10 most frequent tokens in description")
  plt.xlabel("Words")
  plt.ylabel("Frequency")
  plt.show()


text = input("Nhập một đoạn văn bản: ")


word_freq, sorted_words = word_frequency(text)
plot_histogram(sorted_words)