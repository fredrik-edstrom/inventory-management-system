from abc import ABC


class Result(list):
    def first(self):
        return self[0] if len(self) > 0 else None

    def last(self):
        return self[-1] if len(self) > 0 else None


class Document(dict, ABC):
    collection = None

    def __init__(self, data):
        super().__init__()

        if '_id' not in data:
            self._id = None
        self.__dict__.update(data)

    def __repr__(self):
        return '\n'.join(f'{k} = {v}' for k, v in self.__dict__.items())

    def save(self):
        if not self._id:
            del self.__dict__['_id']
            self.collection.insert_one(self.__dict__)
        else:
            self.collection.replace_one({'_id': self._id}, self.__dict__)

    def delete_column(self, column: str):
        self.collection.update_one({'_id': self._id}, {'$unset': {column: ''}})

    @classmethod
    def get_all(cls):
        return [cls(item) for item in cls.collection.find()]

    @classmethod
    def find(cls, **kwargs):
        return Result(cls(item) for item in cls.collection.find(kwargs))

    @classmethod
    def delete(cls, **kwargs):
        cls.collection.delete_many(kwargs)

    @classmethod
    def order_by(cls, column):
        return sorted([item.__dict__ for item in cls.get_all()], key=lambda j: j[column])

    @classmethod
    def get_object_id(cls, **kwargs):
        return Result(item.__dict__['_id'] for item in cls.find(**kwargs))
