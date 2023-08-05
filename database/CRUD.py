from typing import List, Dict, TypeVar

from peewee import ModelSelect

from database.models import db, ModelBase, Anecdotes

T = TypeVar("T")


def _store_data(db: db, model: T, *data: Dict) -> None:
    """Запись данный в БД из списка."""
    with db.atomic():
        model.insert_many(*data).execute()


def _retrieve_all_data(db: db, model: T, *columns: ModelBase) -> ModelSelect:
    """Чтение данных из БД."""
    with db.atomic():
        response = model.select(*columns)

    return response


def _delete_all_data(db: db, model: T):
    with db.atomic():
        model.delete().execute()


def _delete_by_id(db: db, model: T, pk):
    with db.atomic():
        model.delete_by_id(pk)


class CRUDInterface():
    """Интерфейс вызова функций чтения/записи БД."""

    @staticmethod
    def create():
        return _store_data

    @staticmethod
    def retrieve():
        return _retrieve_all_data

    @staticmethod
    def clear():
        return _delete_all_data

    @staticmethod
    def delete_by_id():
        return _delete_by_id
