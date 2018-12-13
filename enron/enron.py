import os


class Inbox():
    def __init__(self, name, directory):
        self.name = name
        self.directory = directory
        self.folders = file_names(self.path())
        print(self.folders)

    def __str__(self):
        return self.name

    def path(self):
        return self.directory + self.name


class Enron():
    def __init__(self, directory):
        self.directory = directory
        self.inbox_names = file_names(directory)
        print(self.inbox_names)
        print('number of inboxes:', len(self.inbox_names))
        self.inboxes = []

        self.connections = {}

    def create_inboxes(self):
        for inbox_name in self.inbox_names:
            self.inboxes.append(Inbox(inbox_name, self.directory))
            print(self.inboxes[-1])
            self.scan_inbox(self.inboxes[-1])
            break

    def scan_inbox(self, inbox):
        for folder in inbox.folders:
            # print(folder)
            self.scan_folder(inbox.path() + '/' + folder)

    def scan_folder(self, folder_path):
        # print(folder_path)
        files = file_names(folder_path)
        # print(files)
        for file in files:
            print(file)
            with open(folder_path + '/' + file, 'r') as f:
                head = [next(f) for x in range(4)]
                date = head[1]
                from_address = self.parse_address(head[2])
                to_address = self.parse_address(head[3])
                # print(from_address)

    @staticmethod
    def parse_address(address_field):
        # print(address_field)
        print(address_field.strip())




def file_names(directory):
    files = sorted(os.listdir(directory))
    return [x for x in files if x[0] != '.']


def main():
    enron = Enron('../maildir/')
    enron.create_inboxes()


if __name__ == '__main__':
    main()
