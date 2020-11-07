from django.db import models


class TodoTable(models.Model):
    todo_msg = models.CharField(max_length=256)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.todo_msg} | is_done? {self.is_done}'
