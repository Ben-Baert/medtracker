from datetime import datetime
from peewee import SqliteDatabase
from peewee import Model
from peewee import DateTimeField
from peewee import CharField
from peewee import TextField

class BaseModel(Model):
    database = SqliteDatabase('med.sqlite')


class Medicine(BaseModel):
    name = CharField()
    description = TextField()


class MedicinePrescription(BaseModel):
    medicine = ForeignKeyField(Medicine, related_name='prescriptions')
    start_dt = DateTimeField()
    stop_dt = DateTimeField(null=True)  # null: undetermined
    dosage_in_mg = IntegerField()
    frequency_per_24_hours = IntegerField()
    administration_method = CharField(choices=[('sci', 'Subcutaneous injection'), ('oral', 'Oral')])


class MedicineAdministration(BaseModel):
    medicine_prescription = ForeignKeyField(MedicinePrescription, related_name='administrations')
    dt = DateTimeField(default=datetime.now())
    specification = CharField()
