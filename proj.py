import re


def getInput(sentence):
    sentence = sentence.lower()
    # print sentence
    sentence_length = len(sentence)
    ###
    # return a empty list when no of characters more than 200
    ###
    if sentence_length > 200:
        return []
    ### split the sentence using regular expresssion
    words_array = re.compile("[,\.!\?&;\:'\" ]").split(sentence)
    ### remove the zero character strings from the list
    words_array_cleaned = [x for x in words_array if x is not ""]
    return words_array_cleaned


def detectSpellErrors(words):
    # initialize no of error to zero
    no_of_errors = 0

    # initialize the set which will hold all the correct words
    set_of_correctwords = set()

    # open the file that conatains the correct words
    spell_file = open("ALL WORDS.txt", "r")

    # read each line from file and add it to the set
    for line in spell_file:
        set_of_correctwords.add(line.rstrip("\n"))
    for word in words:
        ########################################################
        # check if the word is not in the set of correct words #
        # if yes increment the no of errors                    #
        ########################################################
        if word.upper() not in set_of_correctwords:  # convert to upper
            no_of_errors += 1
    return no_of_errors


def removeDuplicates(words):
    new_words = []
    for i in range(len(words) - 1):
    # debugging
    # print i
    # print words[i]
    # print words[i+1]
        if words[i] == words[i + 1]:
            # print "coming inside if"
            words[i] = ''
    new_words = [x for x in words if x != '']
    return new_words


def removeStopWords(words):
    new_words = []
    stop_file = open("STOP WORDS.txt", "r")
    stop_words_array = []
    for line in stop_file:
        ##########################################
        # Strip any new line from each stop word #
        # append the stopword to stopword array  #
        ##########################################
        stop_words_array.append(line.rstrip('\n'))
    # prints all the stop words
    # print stop_words_array
    for word in words:
        if word not in stop_words_array:
            new_words.append(word)
    return new_words


def main_algo(answer):
    words = getInput(answer)
    no_of_spell_errors = detectSpellErrors(words)
    words_dup_removed = removeDuplicates(words)
    words_dup_stop_removd = removeStopWords(words_dup_removed)
    # print "No of spelling errors detected: " + str(no_of_spell_errors)
    # print words_dup_stop_removd
    return (no_of_spell_errors, words_dup_stop_removd)


def main(answer):
    words = getInput(answer)
    no_of_spell_errors = detectSpellErrors(words)
    words_dup_removed = removeDuplicates(words)
    words_dup_stop_removd = removeStopWords(words_dup_removed)
    print "No of spelling errors detected: " + str(no_of_spell_errors)
    print words_dup_stop_removd

main("Hi there how are you  am deva.  am test sample.")
