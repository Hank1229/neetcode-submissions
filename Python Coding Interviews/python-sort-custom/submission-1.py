from typing import List

def wordCount(word):
        return len(word)

def sort_words(words: List[str]) -> List[str]:
    words.sort(key=wordCount, reverse=True)
    return words

def abs_num(num):
    return abs(num)

def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(key=abs_num)
    return numbers


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
