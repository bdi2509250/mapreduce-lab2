from src.core.job.reducer import Reducer


class WordCountReducer(Reducer):
    def reduce(self, key, values, emit):
        emit(key, sum(values))


class VowelConsonantStatsReducer(Reducer):
    def reduce(self, key, values, emit):
        total_vowels = 0
        total_consonants = 0
        total_words = 0

        for value in values:
            v, c, n = value
            total_vowels += v
            total_consonants += c
            total_words += n

        if total_words == 0:
            return

        total_letters = total_vowels + total_consonants
        if total_letters == 0:
            return

        avg_vowels_per_word = total_vowels / total_words
        avg_consonants_per_word = total_consonants / total_words

        vowels_pct = total_vowels / total_letters * 100.0
        consonants_pct = total_consonants / total_letters * 100.0

        emit(
            key,  
            {
                "avg_vowels_per_word": avg_vowels_per_word,
                "avg_consonants_per_word": avg_consonants_per_word,
                "vowels_pct": vowels_pct,
                "consonants_pct": consonants_pct,
            },
        )
