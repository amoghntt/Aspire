# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import  reverse

# Create your models here.


class pk(models.Model):
        Release = models.IntegerField(max_length=250)
        name=models.CharField(max_length=200)
        def __str__(self):
                return self.name
class adaptive(models.Model):

        Release= models.ForeignKey(pk, on_delete=models.CASCADE)
        DD = models.IntegerField(max_length=200)
        DefectLeakage= models.IntegerField(max_length=200)
        DefectRejection= models.IntegerField(max_length=200)

        TestCaseCount= models.IntegerField(max_length=200)
        ApplicationComplexity= models.IntegerField(max_length=200)
        DomainKnowledge= models.IntegerField(max_length=200)
        TechnicalSkills= models.IntegerField(max_length=200)
        ReqQueryCount=models.IntegerField(max_length=200)
        CodeReviewComments= models.IntegerField(max_length=200)
        DesignReviewComments=models.IntegerField(max_length=200)
        NoofResources=models.IntegerField(max_length=200)
        BudgetinUse= models.IntegerField(max_length=200)
        ETA=models.IntegerField(max_length=200)
        CostofResource= models.IntegerField(max_length=200)
        Efficiency=models.IntegerField(max_length=200)
        ProjectStatus = models.IntegerField(max_length=200)
        AvailabilityofBudget= models.IntegerField(max_length=200)
        is_clicked = models.BooleanField(default=False)


class pk1(models.Model):
        Release = models.IntegerField(max_length=250)
        name = models.CharField(max_length=200)

        def __str__(self):
                return self.name
class adaptive1(models.Model):
        Release = models.ForeignKey(pk1, on_delete=models.CASCADE)
        DD = models.IntegerField(max_length=200)
        DefectLeakage = models.IntegerField(max_length=200)
        DefectRejection = models.IntegerField(max_length=200)

        TestCaseCount = models.IntegerField(max_length=200)
        ApplicationComplexity = models.IntegerField(max_length=200)
        DomainKnowledge = models.IntegerField(max_length=200)
        TechnicalSkills = models.IntegerField(max_length=200)
        ReqQueryCount = models.IntegerField(max_length=200)
        CodeReviewComments = models.IntegerField(max_length=200)
        DesignReviewComments = models.IntegerField(max_length=200)
        NoofResources = models.IntegerField(max_length=200)
        BudgetinUse = models.IntegerField(max_length=200)
        ETA = models.IntegerField(max_length=200)
        CostofResource = models.IntegerField(max_length=200)
        Efficiency = models.IntegerField(max_length=200)
        ProjectStatus = models.IntegerField(max_length=200)
        AvailabilityofBudget = models.IntegerField(max_length=200)
