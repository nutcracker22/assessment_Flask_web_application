import os
import threading
from wsgiref import simple_server
from wsgiref.simple_server import WSGIRequestHandler
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from sites import app
import time

options = FirefoxOptions()


def before_all(context):
    context.server = simple_server.WSGIServer(("", 5000), WSGIRequestHandler)
    context.server.set_app(app)
    context.pa_app = threading.Thread(target=context.server.serve_forever)
    context.pa_app.start()

    context.browser = webdriver.Firefox(options=options)
    context.browser.set_page_load_timeout(time_to_wait=200)


def after_all(context):
    time.sleep(3)
    context.browser.quit()
    context.server.shutdown()
    context.pa_app.join()

