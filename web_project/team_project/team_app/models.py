from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

#유저 테이블
class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='customer')
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    phone_num = models.CharField(max_length=20)


#흥미 테이블
class Domain(models.Model):
    foreignkey = models.ForeignKey(
        Customer, related_name='domain', on_delete=models.SET_NULL, null=True
    )
    health = models.IntegerField()
    economy = models.IntegerField()
    culture_art = models.IntegerField()
    education = models.IntegerField()
    society = models.IntegerField()
    technology = models.IntegerField()

#프로필(점수) 테이블
class Score(models.Model):
    foreignkey = models.ForeignKey(
        Customer, related_name='score', on_delete=models.SET_NULL, null=True
    )
    web = models.IntegerField()
    design = models.IntegerField()
    machine_learning = models.IntegerField() 
    statistics = models.IntegerField()
    deep_learning = models.IntegerField()
    algorithm = models.IntegerField()
    nlp = models.IntegerField()
    data_score = models.IntegerField()
    modeling_score = models.IntegerField()

#선호역할 테이블
class Role(models.Model):
    foreignkey = models.ForeignKey(
        Customer, related_name='role', on_delete=models.SET_NULL, null=True
    )
    analysis_hearts = models.IntegerField()
    web_hearts = models.IntegerField()
    design_hearts = models.IntegerField()
    modeling_hearts = models.IntegerField()

#알리미
class Message(models.Model):
    sender = models.CharField(max_length=20) #보낸사람
    recipient = models.CharField(max_length=20) #받을사람
    sentAt = models.DateTimeField(auto_now_add=True) #쪽지를보낸시간

    def save(self, **kwargs):
        if not self.id:
            self.sentAt = timezone.now()
        super(Message, self).save(**kwargs)