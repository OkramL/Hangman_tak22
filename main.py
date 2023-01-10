from Controller import Controller


class Hangman:

    def __init__(self):
        Controller().main()


if __name__ == '__main__':
    # TODO read commandline db name
    # TODO Enter key as Send button
    # TODO if letter inputed second time read as error HOMEWORK
    Hangman()
