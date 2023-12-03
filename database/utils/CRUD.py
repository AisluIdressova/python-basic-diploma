from typing import Dict, List, TypeVar
from database.common.models import ModelBase, db
from peewee import ModelSelect

T = TypeVar('T')

def _store_data(db: db, model: T, *data: List[Dict]) -> None:
    with db.atomic():
        model.insert_many(*data).execute()


def _retrieve_all_data(db: db, model: T) -> str:
    new_str = ''
    with db.atomic():
        response = model.select()
        response = [[str(item.id), str(item.message), str(item.date)] for item in response]
        for item in response:
            new_str += '{} | {} |  {}\n'.format(item[0], item[1], item[2])

    return new_str

class CRUDInterface:
    @staticmethod
    def create():
        return _store_data

    @staticmethod
    def retrieve():
        return _retrieve_all_data


if __name__ == '__main__':
    _store_data()
    _retrieve_all_data()
    CRUDInterface()

