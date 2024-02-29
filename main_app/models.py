from django.db import models

SIZES = (
  ('S', 'Small'),
  ('M', 'Medium'),
  ('L', 'Large'),
)

class Stuff(models.Model):
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  size = models.CharField(
    max_length=1,
    choices=SIZES,
    default=SIZES[0][0]
  )
  age = models.IntegerField()

  def __str__(self):
    return self.name
