import peewee as pw

db = pw.SqliteDatabase('anecdotes.db')


class ModelBase(pw.Model):
    class Meta:
        database = db


class Anecdotes(ModelBase):
    """Дочерний класс Anecdote. Описывает свойства атрибутов для БД."""
    anecdote = pw.TextField()
    anecdote_rate = pw.IntegerField()
    publication = pw.BooleanField()