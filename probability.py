from tqdm import tqdm


def checkProbability(texts):
    with open('englishDictionary.txt') as word_file:
        valid_words = list(word_file.read().split())
    hitSentence = 0
    for text in tqdm(texts):
        splitedText = list(text.split())
        hitWord = 0
        for i in range(len(splitedText)):
            splitedText[i] = splitedText[i].lower()
            temp = [char for char in splitedText[i] if char.isalnum()]
            temp = "".join(temp)
            for word in valid_words:
                if word == temp or temp.isnumeric():
                    hitWord += 1
                    break
        if hitWord == len(splitedText):
            hitSentence += 1
    return hitSentence
