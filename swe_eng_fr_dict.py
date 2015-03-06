__author__ = 'Applegrain'

def search_dict(dictionary, key):
    val = "Word not found."
    if key in dictionary:
        val = se_eng_dict[key]
    print val

se_eng_fr_dict = {'School': ['Skola', 'Ecole'], 'Ball': ['Boll', 'Ballon']}
print se_eng_fr_dict

choose_language = raw_input("Type 'English', for English. Skriv 'svenska' fo:r svenska. Pour francais, ecrit 'francais'. ")

if choose_language == 'English':
    word = raw_input("Type in a word:")
    swe_word = se_eng_fr_dict[word][0]
    fra_word = se_eng_fr_dict[word][1]
    print word, ":", swe_word, "pa. svenska," , fra_word, "en francais."

elif choose_language == 'Svenska':
    word = raw_input("Vilket ord:")
    for key, value in se_eng_fr_dict.iteritems():
        if value == word:
            print key











