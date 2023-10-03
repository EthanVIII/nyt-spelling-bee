def spelling_bee(optional_letters, mandatory_letters, english_dict):
    word_list = []
    clue_letters = optional_letters + mandatory_letters
    for i in english_dict:
        word_letters = list(i)
        flag = True
        for letter in word_letters:
            if letter not in clue_letters:
                flag = False
        for mand_letter in mandatory_letters:
            if mand_letter not in word_letters:
                flag = False
        if flag and len(word_letters) >= 4:
            word_list.append(i)

    return word_list

if __name__ == "__main__":
    import numpy as np
    optional_letters = list(input("Input Optional Letters: "))
    mandatory_letters = list(input("Input Mandatory Letters: "))
    english_dict = np.loadtxt("words_alpha.txt",dtype="str")
    word_list = spelling_bee(optional_letters, mandatory_letters, english_dict)
    print(word_list)

