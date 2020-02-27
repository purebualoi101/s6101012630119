from django.db import models

# Create your models he
class ResultHis(models.Model):
    num_x = models.TextField(max_length=200, blank=True)
    num_y = models.TextField(max_length=200, blank=True)
    operation = models.TextField(max_length=200, blank=True)
    num_result = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return str(self.num_x + self.operation + self.num_y + "=" + self.num_result)
