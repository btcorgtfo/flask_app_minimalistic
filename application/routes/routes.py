# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
import os
from application.routes.models import Song
user_interface = Blueprint('user_interface', __name__)

@user_interface.route('/', methods=['GET'])
def home():
    return "Hello world!"


@user_interface.route('/songs', methods=['GET'])
def songs():
    # here should be a function to generate the data for the html page
    # have a look at the library to access mp3 info
    # https://stackoverflow.com/questions/8948/accessing-mp3-metadata-with-python

    data_backend = list()

    a_song = Song(artist='REM',
                  title='Losing my Religion',
                  length=220)
    data_backend.append(a_song)

    another_song = Song(artist='Die Fantastischen Vier',
                        title='Sie ist weg',
                        length=180)
    data_backend.append(another_song)

    # in html via jinja2, you can access the data_frontend variable with its methods
    return render_template('index.html',
                           data_frontend=data_backend)
