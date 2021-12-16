from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Game(models.Model):
    """A Game a user can loan"""
    name = models.CharField(max_length=200)
    
    summary = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    

    LOAN_STATUS = (
        ('a', 'Available'),
        ('o', 'On loan'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='a',
        help_text='Game availability',
    )

    def __str__(self):
        """This will return the title of the Book"""
        return f"{self.name[:50]}..."



"""A Loan event for a game"""
class Loan(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    LOAN_ACTION = (
        ('r', 'Reserve'),
        ('l', 'Loan Out'),
        ('r', 'Return'),
    )

    action = models.CharField(
        max_length=1,
        choices=LOAN_ACTION,
        blank=True,
        default='r',
        help_text='Loan action',
    )

    date_added = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now_add = True)

   
            
    def __str__(self):
        """Return a string of the loan"""
        return f"{self.action}"