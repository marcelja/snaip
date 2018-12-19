import os
import json
from validate_email import validate_email
from textblob import TextBlob
from graph import Graph


EMAIL_TOKENS = ['subject', 're', 'fw', 'fwd', 'enron']
HIGH_CONNECTION_THRESHOLD = 50


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
        self.persons = set()

    def scan_inboxes(self):
        for inbox_name in self.inbox_names:
            self.inboxes.append(Inbox(inbox_name, self.directory))
            print(self.inboxes[-1])
            self._scan_inbox(self.inboxes[-1])

    def highest_connections(self, max_high_connections):
        return self.high_connections[:max_high_connections]

    def sort_high_connections(self):
        print('Find high connections.')
        for key, value in self.connections.items():
            if value[0] >= HIGH_CONNECTION_THRESHOLD:
                topic = ''
                if len(value[1]) > 0:
                    topic = max(value[1], key=lambda key: value[1][key])
                self.high_connections.append((key, value[0], topic))
        print('Sort high connections.')
        self.high_connections.sort(key=lambda x: x[1], reverse=True)

    def unique_persons(self, max_high_connections):
        for connection in self.high_connections[:max_high_connections]:
            email_addresses = connection[0].split(';')
            self.persons.add(email_addresses[0])
            self.persons.add(email_addresses[1])
        return self.persons

    def _scan_inbox(self, inbox):
        for folder in inbox.folders:
            self._scan_folder(inbox.path() + '/' + folder)

    def _scan_folder(self, folder_path):
        files = file_names(folder_path)
        for file in files:
            file_path = folder_path + '/' + file
            with open(file_path, 'r') as f:
                from_address, to_address, subject = None, None, None
                try:
                    head = [next(f) for x in range(5)]
                    # date = head[1]
                    from_address = self.parse_address(head[2], file_path)
                    to_address = self.parse_address(head[3], file_path)
                    subject = head[4]
                except:
                    pass

                if from_address and to_address and subject:
                    nouns = self._find_nouns_in_subject(subject)
                    self._save_or_update_in_dict(from_address, to_address,
                                                 nouns)

        for folder in folder_names(folder_path):
            self._scan_folder(folder_path + '/' + folder)

    @staticmethod
    def _find_nouns_in_subject(subject):
        blob = TextBlob(subject)
        return [noun for noun in blob.noun_phrases if noun not in EMAIL_TOKENS]

    def _save_or_update_in_dict(self, from_address, to_address, nouns):
        sorted_from_to = sorted([from_address, to_address])
        identifier = sorted_from_to[0] + ';' + sorted_from_to[1]
        if identifier in self.connections:
            self.connections[identifier][0] += 1
        else:
            self.connections[identifier] = [1, {}]
        self._add_nouns_to_dict(nouns, self.connections[identifier][1])

    def _add_nouns_to_dict(self, nouns, nouns_dict):
        for noun in nouns:
            if noun in nouns_dict:
                nouns_dict[noun] += 1
            else:
                nouns_dict[noun] = 1

    def store_connections_json(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.connections, f)

    def load_connections_json(self, filename):
        with open(filename, 'r') as f:
            self.connections = json.load(f)

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
    # enron.scan_inboxes()
    # enron.store_connections_json('./enron/connections_nouns.json')
    enron.load_connections_json('./enron/connections_nouns.json')
    enron.sort_high_connections()

    number_connections = [35, 50, 100, 200, 500]
    # number_connections = [35, 50]
    for number in number_connections:
        persons = enron.unique_persons(number)
        connections = enron.highest_connections(number)
        # print(persons, connections)

        graph = Graph(persons, connections)
        graph.draw_graph()


if __name__ == '__main__':
    main()
