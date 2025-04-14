from pymongo import MongoClient
from bson.json_util import dumps
# Harrielle Monestime

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, host='localhost', port=27017, db='AAC'):
        """
        Initialize the connection to the MongoDB database.
        Assumes a local MongoDB server with no authentication.
        """
        self.client = MongoClient(host, int(port))
        self.database = self.client[db]

    def create(self, data):
        """Insert a document into the collection"""
        if data is not None:
            try:
                insert = self.database.animals.insert_one(data)
                return True if insert.inserted_id else False
            except Exception as e:
                print(f"An error occurred while inserting the document: {e}")
                return False
        else:
            raise ValueError("Data parameter cannot be empty")

    def read(self, criteria=None):
        """Query for documents in the collection"""
        try:
            data = self.database.animals.find(criteria, {"_id": False}) if criteria else self.database.animals.find({}, {"_id": False})
            return list(data)
        except Exception as e:
            print(f"An error occurred while querying the documents: {e}")
            return []

    def update(self, initial, change):
        """Update document(s) in the collection"""
        if initial is not None and change is not None:
            try:
                update_result = self.database.animals.update_many(initial, {"$set": change})
                return update_result.modified_count
            except Exception as e:
                print(f"An error occurred while updating the document(s): {e}")
                return 0
        else:
            raise ValueError("Initial and change parameters cannot be empty")

    def delete(self, remove):
        """Delete document(s) from the collection"""
        if remove is not None:
            try:
                delete_result = self.database.animals.delete_many(remove)
                return delete_result.deleted_count
            except Exception as e:
                print(f"An error occurred while deleting the document(s): {e}")
                return 0
        else:
            raise ValueError("Remove parameter cannot be empty")
