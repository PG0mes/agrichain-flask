from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models import Product

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    # Se não estiver logado, mostra a Home Page Pública (aquela verde bonita)
    if not current_user.is_authenticated:
        return render_template('index.html')

    # Lógica de Redirecionamento por Perfil
    if current_user.role == 'producer':
        products = Product.get_all_by_producer(current_user.id)
        return render_template('dashboards/producer.html', products=products)
    
    elif current_user.role == 'distributor':
        # Em um sistema real, filtraria produtos "em trânsito"
        shipments = Product.get_all() 
        return render_template('dashboards/distributor.html', shipments=shipments)
    
    elif current_user.role == 'retailer':
        inventory = Product.get_all()
        return render_template('dashboards/retailer.html', products=inventory)
    
    elif current_user.role == 'consumer':
        featured = Product.get_all()[:3] # Pega os 3 primeiros como destaque
        return render_template('dashboards/consumer.html', featured=featured)
    
    elif current_user.role == 'admin':
        products = Product.get_all()
        return render_template('dashboard.html', products=products, page_title="Visão Geral (Admin)")
    
    # Fallback
    return render_template('dashboard.html', products=[], page_title="Dashboard")

@bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html')