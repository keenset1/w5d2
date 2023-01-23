from flask_wtf import flaskform
from wtforms import stringfield, passwordfield,submitfield
from wtforms.validators import data_required, email, length



class signupform(flaskform):
    first_name = stringfield('first_name',validators= [data_required()])

    last_name = stringfield('last_name',validators= [data_required()])

    email = stringfield