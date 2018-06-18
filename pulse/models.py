from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Pulse(models.Model):
    name=models.CharField(max_length=200)
    ctype=models.CharField(max_length=60, db_column='type')
    maximum_rabi_rate=models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)]
        )
    polar_angle=models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(1.0)]
        )

    # def __init__(self,  **kwargs):
    #     super(Pulse, self).__init__( **kwargs)
    #     print(kwargs)
    #     self.name=kwargs["name"]
    #     self.ctype=kwargs["ctype"]
    #     self.maximum_rabi_rate=kwargs["maximum_rabi_rate"]
    #     self.polar_angle=kwargs["polar_angle"]
    
