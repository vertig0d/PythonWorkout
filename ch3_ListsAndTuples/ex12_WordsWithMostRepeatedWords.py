'''Write a function, most_repeating_word, that takes a sequence of strings as input. 
The function should return the string that contains the greatest number of repeated letters. In other words
For each word, find the letter that appears the most times.
Find the word whose most-repeated letter appears more than any other.'''

from collections import Counter

def get_counter_val(words):
    wrd = ''
    max_wrd_cnt = 0
    for item in words:      
        dic_item = dict(Counter(item))
        max_letter = dic_item[max(dic_item, key= lambda x:dic_item[x])]        
        if max_letter > max_wrd_cnt:
            wrd = item
            max_wrd_cnt = max_letter
    return wrd

# words = ['this', 'is', 'an', 'elementary', 'test', 'example', 'aabbcccc']
# print(get_counter_val(words))