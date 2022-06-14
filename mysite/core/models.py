from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField("file",upload_to='media/')

    # def save(self,name, *args, **kwargs):
    #     print(name)
    #     self.pdf.name = name
    #     super(Book, self).save(*args, **kwargs)


    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs)
