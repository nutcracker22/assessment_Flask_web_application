import os
from flask import Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for
from sites.database import connect_to_db
from sites.test import create_app

my_app = create_app()