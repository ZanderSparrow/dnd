from django.db import models

# Races

# Classes

# Characters
class Character(models.Model):
    player = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Monsters
class Monster(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Items
class Item(models.Model):
    name = models.CharField(max_length=200)
    holder = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
