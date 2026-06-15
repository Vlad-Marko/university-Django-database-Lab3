from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone
import datetime

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField("date published")

#     def __str__(self):
#         return self.question_text

class Question(models.Model):

    QUESTION_TYPES = [
        ('Controversial', 'Controversial'),
        ('Popular', 'Popular'),
        ('Regular', 'Regular'),
    ]

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    question_type = models.CharField(
        max_length=20,
        choices=QUESTION_TYPES,
        default='Regular'
    )  

    def __str__(self):
        return self.question_text
        
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
#
    # def popularity(self):
        
    #     total_votes = sum(choice.votes for choice in self.choice_set.all())
    #     if total_votes >= 20:
    #         return "Highly Popular"
    #     elif total_votes >= 10:
    #         return "Popular"
    #     else:
    #         return "Regular"
#

    def countAbsoluteVotes(self):
        return sum(choice.votes for choice in self.choice_set.all())
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    is_correct = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text
