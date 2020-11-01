# -*- coding: utf-8 -*-
from flask import Blueprint

user_interface = Blueprint('user_interface', __name__)

@user_interface.route('/', methods=['GET'])
def dashboard():
    return "Hello world!"
