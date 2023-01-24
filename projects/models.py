from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name = models.CharField( max_length=122)
    email = models.CharField( max_length=122)
    phone = models.CharField( max_length=122)
    desc =models.TextField()
    date =models.DateField()

    def __str__(self):
        return self.name



class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=122)
    content = models.TextField()
    author = models.CharField( max_length=122)
    timeStamp = models.DateTimeField(blank = True)

    def __str__(self):
        return self.title + 'by' + self.author


class postjob(models.Model):
    sno = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    title = models.CharField( max_length=122)
    companyname = models.CharField( max_length=122)
    describtion = models.TextField()
    experience = models.CharField( max_length=122)
    salary = models.CharField( max_length=122)


    def __str__(self):
        return self.title  
    
class feedback(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    jobno = models.ForeignKey(postjob,null=True,on_delete=models.CASCADE)
    title = models.CharField( max_length=122)
    feedback = models.CharField( max_length=122)

    def __str__(self):
        return self.title

class company(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    contact = models.CharField(max_length=200, null=True)

    def __str__(self):
	    return self.contact

class candidate(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	contact = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.user.username



class applyforjob1(models.Model):
    candidate = models.ForeignKey(User, on_delete=models.CASCADE)
    jobno = models.ForeignKey(postjob, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.PositiveIntegerField()
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=50)
    image = models.ImageField(upload_to='profileimg', blank=True)
    ifile = models.FileField(upload_to='doc', blank=True)
     

    def __str__(self):
        return self.name

