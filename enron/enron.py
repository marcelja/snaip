import os


class Inbox():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Enron():
    def __init__(self, directory):
        self.directory = directory
        self.inbox_names = os.listdir(directory)
        print('number of inboxes:', len(self.inbox_names))


def main():
    enron = Enron('../maildir/')
    inbox = Inbox(enron.inbox_names[0])
    print(inbox)


if __name__ == '__main__':
    main()
