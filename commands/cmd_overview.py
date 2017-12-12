from models import MedicineAdministration
from click import command
from click import echo
from click import prompt


@command()
def overview():
    # show  medication
    # show overdue meds in red
    # show shortly_due meds in orange
    # shows meds in order in green


@command()
def list():
    administrations = MedicineAdministration.select().order_by(MedicineAdministration.dt.desc()).limit(10)
    for administration in administrations:
        echo(administration.dt.strftime("%d/%m/%y %H:%M"))


if __name__ == '__main__':
    list()
