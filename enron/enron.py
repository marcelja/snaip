import os
from validate_email import validate_email


class Inbox():
    def __init__(self, name, directory):
        self.name = name
        self.directory = directory
        self.folders = folder_names(self.path())

    def __str__(self):
        return self.name

    def path(self):
        return self.directory + self.name


class Enron():
    def __init__(self, directory):
        self.directory = directory
        self.inbox_names = folder_names(directory)
        print(self.inbox_names)
        print('number of inboxes:', len(self.inbox_names))
        self.inboxes = []

        self.connections = {}
        self.high_connections = []

    def create_inboxes(self):
        for inbox_name in self.inbox_names:
            self.inboxes.append(Inbox(inbox_name, self.directory))
            print(self.inboxes[-1])
            self.scan_inbox(self.inboxes[-1])

    def highest_connections(self):
        print('Find high connections.')
        for key, value in self.connections.items():
            if value >= 50:
                self.high_connections.append((key, value))
        print('Sort high connections.')
        self.high_connections.sort(key=lambda x: x[1], reverse=True)

    def scan_inbox(self, inbox):
        for folder in inbox.folders:
            self.scan_folder(inbox.path() + '/' + folder)

    def scan_folder(self, folder_path):
        files = file_names(folder_path)
        for file in files:
            file_path = folder_path + '/' + file
            with open(file_path, 'r') as f:
                try:
                    head = [next(f) for x in range(4)]
                    date = head[1]
                    from_address = self.parse_address(head[2], file_path)
                    to_address = self.parse_address(head[3], file_path)
                    if from_address and to_address:
                        self.save_or_update_in_dict(from_address, to_address,
                                                    date)
                except:
                    pass

        for folder in folder_names(folder_path):
            self.scan_folder(folder_path + '/' + folder)

    def save_or_update_in_dict(self, from_address, to_address, date):
        sorted_from_to = sorted([from_address, to_address])
        identifier = sorted_from_to[0] + ';' + sorted_from_to[1]
        if identifier in self.connections:
            self.connections[identifier] += 1
        else:
            self.connections[identifier] = 1

    @staticmethod
    def parse_address(address_field, file_path):
        address_field = address_field.replace('To:', '').replace('From:', '')
        address_field = address_field.strip()
        if '<' in address_field or ',' in address_field:
            return False
        if not validate_email(address_field):
            return False
        return address_field


def folder_names(directory):
    files = sorted(next(os.walk(directory))[1])
    return [x for x in files if x[0] != '.']


def file_names(directory):
    files = sorted(next(os.walk(directory))[2])
    return [x for x in files if x[0] != '.']


def main():
    enron = Enron('../maildir/')
    enron.create_inboxes()
    enron.highest_connections()
    import pdb;pdb.set_trace()


if __name__ == '__main__':
    main()
