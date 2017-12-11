from datetime import datetime
from datetime import timedelta
from peewee import SqliteDatabase
from peewee import Model
from peewee import DateTimeField
from peewee import CharField
from peewee import TextField


class BaseModel(Model):
    database = SqliteDatabase('med.db')


class MedicineCategory(BaseModel):
    parent = ForeignKeyField('self', related_name='children', null=True)
    name = CharField()
    description = TextField()


class Medicine(BaseModel):
    category = ForeignKeyField(MedicineCategory, related_name='medicines')
    parent = ForeignKeyField('self', related_name='children', null=True)
    administration_method = ForeignKeyField(MedicineAdministrationMethod)
    name = CharField()
    description = TextField()


class MedicineAdministrationMethod(BaseModel):
    parent = ForeignKeyField('self', related_name='children', null=True)
    name = CharField()


class MedicinePrescription(BaseModel):
    medicine = ForeignKeyField(Medicine, related_name='prescriptions')
    start_dt = DateTimeField()
    stop_dt = DateTimeField(null=True)  # null: undetermined
    dosage_in_mg = IntegerField()
    frequency_per_24_hours = IntegerField()
    essential = BooleanField(default=False) 

class MedicineAdministration(BaseModel):
    medicine_prescription = ForeignKeyField(MedicinePrescription, related_name='administrations')
    dt_planned = DateTimeField()
    dt_done = DateTimeField(default=datetime.now())
    specification = CharField(null=True)  # e.g. left side

    def relevant(self):
        return self.overdue() or self.due_soon()

    def overdue(self):
        return not self.dt_done and self.dt_planned > datetime.now()

    def due_soon(self):
        return not self.dt_done and self.dt_planned > datetime.now() - timedelta(hours=24)
