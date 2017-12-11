from click import command
from click import argument 
from click import Choice
from click import option
from click import echo
from models import MedicineAdministration


@command()
@argument('side', type=Choice(['left', 'right']))
@option('--dt', default=None)
def add(side, dt):
    MedicineAdministration.create(side=side)
    echo('Created')


if __name__ == '__main__':
    add()

