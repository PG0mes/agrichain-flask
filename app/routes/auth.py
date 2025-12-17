from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app.models import User

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Busca na lista simulada
        user = User.get_by_email(email)
        
        # Verificação simples de senha (sem hash para este teste)
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('main.index'))
        
        flash('Email ou senha inválidos.', 'error')
    return render_template('auth/login.html')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        
        if User.get_by_email(email):
            flash('Email já cadastrado.', 'error')
            return redirect(url_for('auth.register'))
            
        # Cria novo usuário na lista
        user = User.create(
            name=request.form.get('name'),
            email=email,
            password=request.form.get('password'),
            role=request.form.get('role')
        )
        
        login_user(user)
        flash('Conta criada com sucesso!', 'success')
        return redirect(url_for('main.index'))
        
    return render_template('auth/register.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))