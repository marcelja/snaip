import os


class Inbox():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Enron():
    def __init__(self, directory):
        self.directory = directory
        self.inbox_names = file_names(directory)
        print(self.inbox_names)
        print('number of inboxes:', len(self.inbox_names))


def file_names(directory):
    files = sorted(os.listdir(directory))
    return [x for x in files if x[0] != '.']


def main():
    enron = Enron('../maildir/')
    inbox = Inbox(enron.inbox_names[0])
    print(inbox)


if __name__ == '__main__':
    main()
