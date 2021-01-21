import logging
from flask import redirect, Blueprint, render_template
from server.controller import visualization
from smm_workflow import workflow_most_common_emojis

"""
    Routes for outputs for front-end are set in this module
"""


bp = Blueprint('pages', __name__)
logger = logging.getLogger()


@bp.route('/')
def view_base():
    return "Home"


@bp.route('/smm')
def execute_smm():
    workflow_most_common_emojis('Chester Twitter')
    return "Executando workflow"


@bp.route('/visual1')
def render_app1():
    visualization.create_histogram1()
    return redirect('/histogram1/')


@bp.route('/visual2')
def render_app2():
    visualization.create_histogram2()
    return redirect('/histogram2/')


@bp.route('/my_page')
def render_my_page():
    visualization.create_histogram1()
    visualization.create_histogram2()
    return render_template('my_template.html')

