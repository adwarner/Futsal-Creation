# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 16:14:29 2016

@author: adamwarner
"""

import peewee
from peewee import *
import MySQLdb 

db = MySQLDatabase('test', user='root', host = "localhost") 

class futsalData(peewee.Model):
    Buzz = peewee.CharField()
    Charlie = peewee.CharField()
    Dez = peewee.CharField()
    Henrik = peewee.CharField()
    Jose = peewee.CharField()
    Kevin = peewee.CharField()
    Matt = peewee.CharField()
    Mitch = peewee.CharField()
    Nate = peewee.CharField()
    Reid = peewee.CharField()
    Rico = peewee.CharField()
    Scud = peewee.CharField()
    Snider = peewee.CharField()
    Tanner = peewee.CharField()
    Tim = peewee.CharField()
    Toby = peewee.CharField()
    Tyler = peewee.CharField()
    Will = peewee.CharField()
    Zo = peewee.CharField()




    class Meta:
        database = db

futsalData.create_table()

db.close()

