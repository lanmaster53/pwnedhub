from flask import Blueprint, request, render_template
from common.models import Config
from pwnedconfig import db

core = Blueprint('core', __name__)

@core.route('/', methods=['GET', 'POST'])
def config():
    if request.method == 'POST':
        Config.get_by_name('CSRF_PROTECT').value = request.form.get('csrf_protect') == 'on' or False
        Config.get_by_name('BEARER_AUTH_ENABLE').value = request.form.get('bearer_enable') == 'on' or False
        Config.get_by_name('CORS_RESTRICT').value = request.form.get('cors_restrict') == 'on' or False
        Config.get_by_name('OIDC_ENABLE').value = request.form.get('oidc_enable') == 'on' or False
        db.session.commit()
    return render_template('config.html')
