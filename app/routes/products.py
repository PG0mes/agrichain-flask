from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import Product
import datetime
import random

bp = Blueprint('products', __name__, url_prefix='/products')

@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        product_code = f"AGRI-{random.randint(1000,9999)}"
        
        # Cria e salva na lista
        Product.create(
            product_id=product_code,
            name=request.form.get('name'),
            category=request.form.get('category'),
            producer_id=current_user.id,
            harvest_date=datetime.datetime.strptime(request.form.get('harvest_date'), '%Y-%m-%d'),
            quantity=float(request.form.get('quantity')),
            unit=request.form.get('unit')
        )
        
        flash('Produto registrado com sucesso (Memória)!', 'success')
        return redirect(url_for('main.index'))
        
    return render_template('products/create.html')