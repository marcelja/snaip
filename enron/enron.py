import os


class Inbox():
    def __init__(self, name, directory):
        self.name = name
        self.directory = directory
        self.folders = file_names(directory + name)
        print(self.folders)

    def __str__(self):
        return self.name


class Enron():
    def __init__(self, directory):
        self.directory = directory
        self.inbox_names = file_names(directory)
        print(self.inbox_names)
        print('number of inboxes:', len(self.inbox_names))
        self.inboxes = []

    def create_inboxes(self):
        for inbox_name in self.inbox_names:
            self.inboxes.append(Inbox(inbox_name, self.directory))
            print(self.inboxes[-1])
            break


def file_names(directory):
    files = sorted(os.listdir(directory))
    return [x for x in files if x[0] != '.']


def main():
    enron = Enron('../maildir/')
    enron.create_inboxes()


if __name__ == '__main__':
    main()
