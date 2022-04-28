from django.db import models
from accounts.models import MainProfile
from django.utils import timezone


class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)


class SoftDeleteModel(models.Model):
    deleted_at = models.DateTimeField(blank=True, null=True)
    objects = SoftDeleteManager()
    all_objects = models.Manager()

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

    class Meta:
        abstract = True


class CarBrand(SoftDeleteModel):
    name = models.CharField(max_length=50, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)


class CarModel(SoftDeleteModel):
    car_brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name='car_models')
    name = models.CharField(max_length=50, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


class UserCar(SoftDeleteModel):
    user = models.ForeignKey(MainProfile, on_delete=models.CASCADE, related_name='user_cars')
    car_brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name='user_brands')
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='user_models')
    first_reg = models.DateField(blank=True, null=True)
    odometer = models.IntegerField(blank=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.car_brand.name, self.car_model.name)
