# Lab 2 — MapReduce

## Implemented tasks

### Clean Word Count
Counts all words after removing punctuation.

Output stored in:  
- data/output/task1_clean_wordcount/part-00000.txt


### Words Length Count (≥ 6 characters)
Counts only words with length ≥ 6.

Output stored in:  
- data/output/task2_long_words/part-00000.txt


### Vowel / Consonant Statistics
For each word length calculates:  
average vowels per word, average consonants per word, as well as vowel % and consonant % among all letters.

Output stored in:  
- data/output/task3_vowels_consonants/part-00000.txt


## Source code
All mappers and reducers for this lab:

- src/student_jobs/word_count/mapper.py  
- src/student_jobs/word_count/reducer.py


## How to run

### Task 1
```bash
python -m src.cli.main run --workers 2 --reducers 2 \
  --input data/input --output data/output/task1_clean_wordcount \
  --job src.student_jobs.word_count.mapper:CleanWordCountMapper,src.student_jobs.word_count.reducer:WordCountReducer
```
### Task 2
```bash
python -m src.cli.main run --workers 2 --reducers 2 \
  --input data/input --output data/output/task2_long_words \
  --job src.student_jobs.word_count.mapper:LongWordCountMapper,src.student_jobs.word_count.reducer:WordCountReducer
```
### Task 3
```bash
python -m src.cli.main run --workers 2 --reducers 2 \
  --input data/input --output data/output/task3_vowels_consonants \
  --job src.student_jobs.word_count.mapper:VowelConsonantStatsMapper,src.student_jobs.word_count.reducer:VowelConsonantStatsReducer
```

Author

Dmytro Boichenko
