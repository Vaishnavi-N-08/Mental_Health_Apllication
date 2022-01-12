from django.db import models
#create your model here

class Feedback(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=150,null=False,blank=False)
    email = models.EmailField(null=False)
    number = models.DecimalField(max_digits=10, decimal_places=0)
    suggestion_p = models.CharField(max_length=500,null=False,blank=False)
   

#     eventdesc = models.TextField(max_length=300, null=True, blank=True)
#     eventlink = models.URLField(max_length=5000, null=True, blank=True)

    def _str_(self):
        return str(self.fullname)