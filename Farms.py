from peewee import *
from db import db, UUIDFieldProper
from playhouse.csv_loader import load_csv

class Farms(Model):
    uuid = UUIDFieldProper(primary_key=True)
    category = CharField()
    description = CharField()
    quantity = DoubleField()
    order_number = UUIDField()

    class Meta:
        database = db
        db_table = 'FARMS'
        auto_increment = False
