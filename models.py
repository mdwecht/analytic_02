from django.db import models


class Job(models.Model):
    '''
    DSAE Fields Common to all Jobs:
    '''
    name = models.CharField(max_length=40)
    type = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    period = models.IntegerField(default=3600)
    last_ts = models.DateTimeField(auto_now_add=True)
    created_ts = models.DateTimeField(auto_now_add=True)
    updated_ts = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    '''
    DSAE Fields Specific to 'analytic_02' Job Type:
    '''
    script = models.CharField(max_length=20)
    parm_01 = models.IntegerField(default=10)
    parm_02 = models.IntegerField(default=20)

    def __str__(self):
        return self.name