from flask import Blueprint, render_template
from flask_login import current_user
from app.models import Product

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    if current_user.is_authenticated:
        # Busca na lista em memória
        my_products = Product.get_all_by_producer(current_user.id)
        return render_template('dashboard.html', products=my_products)
    return render_template('index.html')