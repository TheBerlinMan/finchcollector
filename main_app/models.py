from django.db import models
from django.urls import reverse

SIZES = (
  ('S', 'Small'),
  ('M', 'Medium'),
  ('L', 'Large')
)

class Things(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
      return self.name
  
  def get_absolute_url(self):
      return reverse("thing-detail", kwargs={"pk": self.id})

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
  things = models.ManyToManyField(Things)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
      return reverse("stuff-detail", kwargs={"stuff_id": self.id})
  
class Walking(models.Model):
  date = models.DateField()
  length = models.IntegerField()
  stuff = models.ForeignKey(Stuff, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.stuff.name} walked on {self.date} for {self.length} minutes"
  class Meta:
    ordering = ['-date']
       


  
  