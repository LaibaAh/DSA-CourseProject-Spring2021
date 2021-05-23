from flask import Flask, render_template, request,redirect
from flask import url_for
import os
from flask.globals import session 
from flask_sqlalchemy import SQLAlchemy
import sqlite3