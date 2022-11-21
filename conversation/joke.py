
words = {
    "positive_words": ["good", "great", "nice", "hahaha", "haha"],
    "negative_words": ["not", "don't", "didn't"],
    "joke_words": ["joke", "crack", "other", "any", "know", "another"],
    "jokes": iter([
        'I am tired of the constant ups and downs in my life, so I got to stop using the stairs.',
        'What do you call an act of investing in Bill Gates’ business? To Investigate!',
        'What did east say to west? You mustn’t go north when things are going south!',
        'You can find ghost everywhere except the living room.',
        'A Japanese student: "Master Aykodo, why do Europeans think we look all the same?"-The master replied: "I am not master Aykodo."',
        'Can a kangaroo jump higher than a house? - Of course, a house doesn’t jump at all.'
    ])
}


def converse(reply, name):
    message = reply.split(" ")
    for msg in message:
        try:
            if msg in words["joke_words"]:
                return next(words["jokes"])
                break
        except StopIteration:
            return f"Sorry {name}, I don't have more jokes for you"

        if msg in words["positive_words"]:
            return "I am glad you like it. Anything else?"
            break
        if msg in words["negative_words"]:
            return "I am sorry you didn't like it. Anything else I can do for you?"
            break




