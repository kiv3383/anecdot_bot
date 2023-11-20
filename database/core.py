from database.CRUD import CRUDInterface
from database.models import db, Anecdotes

db.connect()
db.create_tables([Anecdotes])

crud = CRUDInterface()


if __name__ == '__main__':
    crud()
