from django.db import models


class Owner(models.Model):
    """Dueño de una casa"""

    # - relational
    # houses <-m2o-> House
    # - own
    user = models.OneToOneField("users.User", on_delete=models.CASCADE,)

    def __str__(self):
        return f"{self.__class__.__name__}[{self.id}] <{self.first_name} {self.last_name}>"  # pylint: disable=no-member


class Visitor(models.Model):
    # - relational
    # plates <-m2o-> Plate
    # - own
    user = models.OneToOneField("users.User", on_delete=models.CASCADE,)

    def __str__(self):
        return f"{self.__class__.__name__}[{self.id}] <{self.first_name} {self.last_name}>"  # pylint: disable=no-member


class Address(models.Model):
    """Address model"""

    # - relational
    # house <-o2o-> House
    # - own
    ext_number = models.PositiveSmallIntegerField()
    street = models.CharField(max_length=50)
    # optional:
    int_number = models.PositiveSmallIntegerField(blank=True, null=True)
    suburb = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.PositiveIntegerField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(default="Mexico", max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.__class__.__name__}[{self.id}] <{self.ext_number} {self.street}>"  # pylint: disable=no-member


class House(models.Model):
    """Una propiedad del fraccionamiento"""

    # - relational
    owner = models.OneToOneField(
        Owner, on_delete=models.SET_NULL, null=True, related_name="house"
    )
    # - own
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.__class__.__name__}[{self.id}] <{self.owner}, {self.address.ext_number} {self.address.street}>"


class Plate(models.Model):
    # - relational
    visitor = models.ForeignKey(
        Visitor, on_delete=models.CASCADE, related_name="plates"
    )
    # - own
    number = models.CharField(max_length=20)


class Checkin(models.Model):
    # - relational
    house = models.ForeignKey(House, on_delete=models.PROTECT)
    visitor = models.OneToOneField(Visitor, on_delete=models.SET_NULL, null=True)
    # - own
    time_created = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)
    time_verified = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.__class__.__name__}[{self.id}] <{self.visitor}>"  # pylint: disable=no-member
