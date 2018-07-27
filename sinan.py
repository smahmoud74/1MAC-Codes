def play_game(ml_string, parts_of_speech):
    replaced = []
    ml_string = ml_string.split()
    for word in ml_string:
        replacement = word_in_pos(word, parts_of_speech)
        if replacement != None:
            word = word.replace(replacement, "Corgi")
            replaced.append(word)
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    retuturn replaced
