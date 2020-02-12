create_user(username, email=None)

sender
User.objects.create_user('Yossi', 'yossi@yossi.com', 'password')

courier
User.objects.create_user('Shimon', 'shimon@shimon.com', 'password')
User.objects.create_user('Ariel', 'ariel@ariel.com', 'password')

>>> from app.models import *
>>> y = User.objects.get(username='Yossi')
>>> y
<User: Yossi>
>>> Sender.objects.create(user=y, company='Bar')
<Sender: Sender object (1)>
>>> s = User.objects.get(username='Shimon')
>>> Courier.objects.create(user=s, first_name='Shimon', last_name='Shimon', phone='050-3434343', vehicle_type='pickup')
<Courier: Courier object (1)>
>>> a = User.objects.get(username='Ariel')  
>>> a
<User: Ariel>
>>> Courier.objects.create(user=a, first_name='Ariel', last_name='Ariel', phone='050-3434344', vehicle_type='toyota')   
<Courier: Courier object (2)>