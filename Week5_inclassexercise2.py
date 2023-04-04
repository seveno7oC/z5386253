def word():
    with open() as file:
            counts = dict()
            for line in file:
                words = line.split()
                for word in words:
                    counts[word]