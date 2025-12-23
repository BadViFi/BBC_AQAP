import os
from decouple import config

class Data():
    SIGNIN = config("SIGNIN")
    PASSWORD = config("PASSWORD")