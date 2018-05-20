from django.db import models
import bcrypt
import re
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



class LogUsersManager(models.Manager):
    def basic_registration(self, postData):
        result = {
            'status': False,
            'errors':[]
        }
        if len(postData['first'])<2 and len(postData['last'])< 2:
            result['errors'].append('First and Last name needs to be greater than 2 charaters.')
            print('yup errors')
        if len (postData['username']) == LogUsers.objects.filter(user_name = postData['username']):
            result['errors'].append('Username exist already.')
        if postData['password'] != postData['confirmation_password']:
            result['errors'].append('Passwords do not match')
        if len(postData['password']) <7:
            result['errors'].append('Password has to be more than 7 charaters.')
        if len(postData['username'])<3:
            result['errors'].append('Username is too short, has to be atleast 3 characters.')
        # if not EMAIL_REGEX.match(postData['email']):
        #     result['errors'].append('Invalid Email')
        if len(result['errors'])<1:
            result['status'] = True
            result['user_id']= LogUsers.objects.create(
                    first_name=postData['first'],
                    last_name= postData['last'],
                    user_name=postData['username'],
                    password=bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()).decode('utf-8')
                    ).id
        return result

    def basic_login(self,postData):
        result  = {
            'status': False,
            'errors': []
        }

        existing_users = LogUsers.objects.filter(user_name= postData['username'])
        # if not EMAIL_REGEX.match(postData['email']):
        #     result['errors'].append('Invalid email or password did not matach.')
        if  len(existing_users) == 0:
            result['errors'].append('Invalid Username or password did not matach.')
        else:
            if  bcrypt.hashpw(postData['password'].encode(),existing_users[0].password.encode()):
                result['status'] = True
                result ['user_id'] = existing_users[0].id
        print(result)
        return result
        
        
class LogUsers(models.Model):
    # full_name = models.CharField(max_length = 30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length= 30)
    email_address = models.CharField(max_length=30)
    password = models.CharField(max_length= 30)
    age = models.AutoField
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    objects = LogUsersManager()
    def __repr__(self):
        return "<users object:{} {} {} {}  >".format(self.first_name, self.last_name, self.email_address, self.user_name)

class BookManager(models.Manager):
    def add_book(self,postData,user_id):
        result  = {
            'status': False,
            'errors': []
        }
        if len(postData['title']) == Book.objects.filter(title = postData['title']):
            result['errors'].append('Title already exist.')
        if len(result['errors'])<1:
            result['status'] = True
            result['uploader'] = Book.objects.create(
                title = postData['title'],
                desc = postData['desc'],
                uploader = LogUsers.objects.get(id = user_id))
        
        
        
        return result


class Book(models.Model):
    title = models.CharField(max_length = 30)
    desc = models.CharField(max_length = 30)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    uploader = models.ForeignKey(LogUsers, related_name = 'uploaded_books',on_delete=models.CASCADE)
    liked_users = models.ManyToManyField(LogUsers,related_name = 'liked_books')
    objects = BookManager()
    def __repr__(self):
        return "<books object:{} {} >".format(self.title, self.desc)





# Create your models here.
