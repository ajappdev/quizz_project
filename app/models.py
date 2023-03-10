# DJANGO DECLARATIONS
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum, Count, F, Max, Min


# DECLARING GLOBAL VARIABLES

QUESTION_TYPES = [
    ("Multiple Choices", "Multiple Choices"),
    ("True or False", "True or False"),
    ("Free Text", "Free Text")]


USER_ROLES = [
    ('Student', 'Student'),
    ('Administrator', 'Administrator')
]

# DECLARING CLASSES

class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='user_profile')
    username = models.CharField(
        max_length=200,
        blank=False,
        null=False)
    role = models.CharField(
        max_length=200,
        blank=False,
        null=False,
        choices=USER_ROLES)
    creation = models.DateTimeField(auto_now_add=True)
    modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Region(models.Model):
    """
    Here we store all regions of quizz questions
    """
    name = models.CharField(
        max_length=300, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    """
    Here we store all countries of quizz questions, and their associated
    regions
    """
    name = models.CharField(
        max_length=300, null=False, blank=False)
    region = models.ManyToManyField(Region)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    Here we store all categories of quizz questions
    """
    name = models.CharField(
        max_length=300, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    """
    Here we store all subcategories of quizz questions, and their associated
    categories
    """
    name = models.CharField(
        max_length=300, null=False, blank=False)
    category = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Question(models.Model):
    """
    Questions table.
    """
    question = models.TextField(
        null=False,
        blank=False)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    type = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        choices=QUESTION_TYPES)
    wikepdia_link = models.CharField(
        max_length=300, null=True, blank=True)
    maps_link = models.CharField(
        max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.question)

    def question_choices(self):
        if self.type == "Multiple Choices":
            return Choice.objects.filter(question=self)
        else:
            return None

    def right_answer(self):
        return Answer.objects.filter(question=self)[0]


class Choice(models.Model):
    """
    Here we store all the choices for questions that take multiple choices
    as answer
    """
    choice = models.CharField(
        max_length=300, null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.choice

class Answer(models.Model):
    """
    Here we store the right answers for questions
    """
    answer = models.CharField(
        max_length=300, null=True, blank=True)
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.answer