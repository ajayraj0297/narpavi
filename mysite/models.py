from django.db import models


# Create your models here.

class enquiry(models.Model):
    name = models.CharField(max_length=500, null=True)
    number = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    message = models.CharField(max_length=500,null=True)

    def __str__(self):
        return self.name


TYPE = (("yes", "yes"), ("no", "no"))


class courses(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)
    image_url = models.CharField(max_length=1000)
    duration = models.CharField(max_length=1000)
    fees = models.IntegerField(null=True)
    tool = models.CharField(max_length=1000, null=True)
    abt = models.CharField(max_length=10000, null=True)
    obj = models.CharField(max_length=10000, null=True)
    trend=models.CharField(
        max_length=20,
        choices=TYPE,
        default="no"
    )

    def __str__(self):
        return self.title


class section(models.Model):
    title = models.CharField(max_length=500)
    course = models.ForeignKey(courses, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class lessons(models.Model):
    title = models.CharField(max_length=500)
    section = models.ForeignKey(section, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(courses, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
