import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read().lower()
                    content = content.translate(str.maketrans('', '', string.punctuation.replace('-', '')))
                    words = content.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
            except Exception as e:
                print(f"Ошибка при чтении файла {file_name}: {e}")
        return all_words

    def find(self, word):
        results = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            if word in words:
                results[name] = words.index(word)
        return results

    def count(self, word):
        results = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            results[name] = words.count(word)
        return results

# Создаем объект класса с именем файла
finder = WordsFinder('test_file.txt')

# Получаем все слова из файла
all_words = finder.get_all_words()
print("Все слова из файла:", all_words)

# Поиск слова
word_to_find = 'text'
position = finder.find(word_to_find)
print(f"Позиция слова '{word_to_find}':", position)

# Подсчет слова
word_count = finder.count(word_to_find)
print(f"Количество слов '{word_to_find}':", word_count)