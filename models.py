from __future__ import unicode_literals
from django.db import models
from django.contrib import messages

class UserManager(models.Manager):
    def validate_new(self, request):       
        if request.method == "POST":
            valid = True
            for key in request.POST:
                if request.POST[key] == "":
                    valid = False
                    messages.error(request,"{} needs to be filled in".format(key))
            if valid == True:
                self.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'],email=request.POST['email'])
                messages.success(request, "Created User")

    def validate_edit(self, request, id):
        if request.method == "POST":
            valid = True
        for key in request.POST:
            if request.POST[key] == "":
                valid = False
                messages.error(request,"{} needs to be filled in".format(key))
            if valid == True:
                u = self.filter(id=id)
                if len(u) > 0:
                    u = u[0]
                u.first_name=request.POST['first_name']
                u.last_name=request.POST['last_name']
                u.email=request.POST['email']
                u.save()
                messages.success(request, "Updated User")
    
    def delete(self, request, id):
        u = User.objects.filter(id=id)
        if len(u) > 0:
            u = u[0]
        u.delete()
        messages.success(request, "Deleted User")

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    objects = UserManager()

    def __repr__(self):
        return "<Users object: {} {}, {}, {}>".format(self.first_name, self.last_name, self.email, self.created_at)