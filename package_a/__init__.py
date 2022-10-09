import datetime as dt


class Person:
    """A person class"""

    def __init__(self, name: str, height: float, weight: float, date_of_birth: dt.date):
        """Initialize a person.

        Args:
            name: The name of the person.
            height: The height of the person.
            weight: The weight of the person.
            date_of_birth: The date of birth of the person.
        """
        self.name = name
        self.height = height
        self.weight = weight
        self.date_of_birth = date_of_birth

    def get_bmi(self) -> float:
        """Get the BMI of the person.

        Returns:
            The BMI of the person.
        """
        return self.weight / (self.height**2)

    def get_age(self) -> int:
        """Get the age of the person.

        Returns:
            The age of the person.
        """
        return dt.date.today().year - self.date_of_birth.year
