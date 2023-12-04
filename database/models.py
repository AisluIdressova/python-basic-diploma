from peewee import SqliteDatabase, Model, PrimaryKeyField, TextField, DateField

db = SqliteDatabase('hhhh.db')


class ModelBase(Model):

    class Meta:
        database = db


class User(ModelBase):
    id = PrimaryKeyField()
    message = TextField()
    date = DateField()
