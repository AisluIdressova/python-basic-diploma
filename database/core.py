from database.CRUD import CRUDInterface
from database.models import db, User

db.connect()
db.create_tables([User])

crud = CRUDInterface()

if __name__ == '__main__':
    crud()
