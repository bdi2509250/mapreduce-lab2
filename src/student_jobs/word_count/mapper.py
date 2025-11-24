import re
from src.core.job.mapper import Mapper


class WordCountMapper(Mapper):
    def map(self, record, emit):
        for token in str(record).split():
            emit(token.lower(), 1)


class CleanWordCountMapper(Mapper):
    PUNCTUATION_REGEX = re.compile(r"[^\w']+", re.UNICODE)

    def map(self, record, emit):
        text = str(record).lower()
        text = self.PUNCTUATION_REGEX.sub(" ", text)
        for token in text.split():
            emit(token, 1)


class LongWordCountMapper(Mapper):
    PUNCTUATION_REGEX = re.compile(r"[^\w']+", re.UNICODE)
    MIN_LENGTH = 6  

    def map(self, record, emit):
        text = str(record).lower()
        text = self.PUNCTUATION_REGEX.sub(" ", text)
        for token in text.split():
            if len(token) >= self.MIN_LENGTH:
                emit(token, 1)


class VowelConsonantStatsMapper(Mapper):
    PUNCTUATION_REGEX = re.compile(r"[^\w']+", re.UNICODE)
    VOWELS = set("aeiouyаеєиіїоуюяыэ")

    def map(self, record, emit):
        text = str(record).lower()
        text = self.PUNCTUATION_REGEX.sub(" ", text)

        for token in text.split():
            word = token
            length = len(word)
            if length == 0:
                continue

            vowels = 0
            consonants = 0

            for ch in word:
                if not ch.isalpha():
                    continue
                if ch in self.VOWELS:
                    vowels += 1
                else:
                    consonants += 1
            emit(length, (vowels, consonants, 1))
