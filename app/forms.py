from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required, Length

class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)

class EditForm(Form):
    nickname = TextField('nickname', validators = [Required()])
    about_me = TextField('about_me', validators = [Length(min = 0, max = 140)])
