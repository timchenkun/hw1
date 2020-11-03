import numpy as np

# Задача 1
print('Задача 1')

corpus = [
    'Crock Pot Pasta Never boil pasta again',
    'Pasta Pomodoro Fresh ingredients Parmesan to taste',
]


class CountVectorizer:
    def __init__(self):
        self.words = []

    """Преобразует текста в вектор"""

    def fit_transform(self, new_texts: list) -> np:
        split_text = [text.lower().split() for text in new_texts]
        # new_words = list(set([word for text in split_text for word in text]))
        new_words = [word for text in split_text for word in text]
        new_words = [new_words[k] for k in range(len(new_words))
                     if k == new_words.index(new_words[k])]
        self.words = new_words
        return np.array([[text.count(word) for word in self.words] for text in split_text])

    """Возвращает все уникальные значения"""

    def get_feature_names(self) -> list:
        return self.words


vectorizer = CountVectorizer()
count_matrix = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names(), '\n')
print(count_matrix, '\n')


# Задача 2
print('Задача 2')


def tf_transform(matrix: np) -> np:
    return count_matrix / np.sum(matrix, axis=1).reshape(2, 1)


tf_matrix = tf_transform(count_matrix)
print(tf_matrix, '\n')


# Задача 3
print('Задача 3')


def idf_transform(matrix: np) -> np:
    return np.log((np.full(matrix.shape[1], matrix.shape[0]) + 1) / (np.sum(matrix.transpose() > 0, axis=1) + 1)) + 1


idf_matrix = idf_transform(count_matrix)
print(idf_matrix, '\n')


# Задача 4
print('Задача 4')


class TfidfTransformer:
    def __init__(self):
        self.count_matrix = np.array([])

    """Нормализирует вектора"""
    @staticmethod
    def fit_transform_new(matrix: np) -> np:
        tf_m = tf_transform(matrix)
        idf_m = idf_transform(matrix)
        return tf_m * idf_m


transformer = TfidfTransformer()
tfidf_matrix = transformer.fit_transform_new(count_matrix)
print(tfidf_matrix, '\n')


# Задача 5
print('Задача 5')


class TfidfVectorizer:
    def __init__(self):
        self.count_matrix = []
        self.words = []

    """Нормализирует вектора"""

    def fit_transform(self, corp: np) -> np:
        vectorizer_ = CountVectorizer()
        count_m = vectorizer_.fit_transform(corp)
        self.words = vectorizer_.get_feature_names()
        transform = TfidfTransformer()
        tfidf_m = transform.fit_transform_new(count_m)
        return tfidf_m

    def get_feature_names(self) -> list:
        return self.words


vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names(), '\n')
print(tfidf_matrix, '\n')
