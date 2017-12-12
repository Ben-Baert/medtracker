from click import command
from click import echo
from click import prompt


@command()
def add_medicine_category():
    name = echo.prompt("What is the name of the category you wish to add")
    if prompt("Do you wish to add a description?").lower().startswith("y"):
        prompt("Type your description: ")
    while prompt("Do you wish to add a parent category?").lower().startswith("y"):
        categories = MedicineCategory.select()
        for category in categories:
            echo("{}: {}".format(category.id, category.name))
        parent_category_id = prompt("Type the parent category id: ")
        try:
            MedicineCategory.get(MedicineCategory.id == int(parent_category_id))
        except ValueError:
            echo("Please provide a valid id (e.g. 1)")
        except DoesNotExist:
            echo("This category does not exist")
        else:
            break
