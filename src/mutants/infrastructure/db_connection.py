from src.mutants.domain.mutant import Mutant

class DBMuntant():
    COLLECTION = 'mutants'

    def __init__(self,database):
        self.database = database

    def insert_one(self, mutant: Mutant):
        dict_mutant = mutant.__dict__
        return self.database[self.COLLECTION].insert_one(dict_mutant)

    def find_one(self, id_):
        cursor = self.database[self.COLLECTION].find_one({'id_': id_})
        return cursor

    def count_documents(self, query: dict) -> int:
        documents = self.database[self.COLLECTION].count_documents(query)
        return documents
