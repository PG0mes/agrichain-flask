from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models import Product

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    if current_user.is_authenticated:
        # Lógica do Super Usuário
        if current_user.role == 'admin':
            # Admin vê TUDO
            products = Product.get_all()
            page_title = "Visão Geral do Sistema (Admin)"
        else:
            # Usuários comuns veem apenas seus produtos
            products = Product.get_all_by_producer(current_user.id)
            page_title = "Meus Produtos"
            
        return render_template('dashboard.html', products=products, page_title=page_title)
        
    return render_template('index.html')