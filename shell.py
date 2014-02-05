import os
from flask import *
from flask1 import *

db.create_all()
db.session.commit()

mike = nipples('mike')

db.session.add(mike)
db.session.commit()

