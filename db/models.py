from datetime import datetime

from peewee import *

db = PostgresqlDatabase('suma')
db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class Ingest(BaseModel):
    id = PrimaryKeyField()
    content = TextField()
    url = TextField()
    created_at = DateTimeField(default=datetime.now())