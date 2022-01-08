paragraph = """  The titled track “Heart Attack” does not interpret the 
    feelings of being in love in a serious way, 
    but with Chuu’s own adorable emoticon like ways. The music video has 
    references to historical and fictional 
    figures such as the artist Rene Magritte!!....  """

for r in ((",", ""), ("!", ""), (".", ""), ("  ", "")):
    paragraph = paragraph.replace(*r)

paragraph_list = paragraph.split()


def count_words(word, word_list):

    word_count = 0
    for i in range(len(word_list)):
        if word_list[i] == word:
            word_count += 1
    return word_count

def unique(word):
    result = []
    for f in word:
        if f not in result:
            result.append(f)
    return result
unique_list = unique(paragraph_list)