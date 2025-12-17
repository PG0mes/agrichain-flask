from flask_login import UserMixin
from datetime import datetime
import uuid

# --- SIMULAÇÃO DE BANCO DE DADOS EM MEMÓRIA ---
# Estas listas vão guardar os dados enquanto o servidor estiver rodando
users_db = []
products_db = []

def generate_uuid():
    return str(uuid.uuid4())

class User(UserMixin):
    def __init__(self, id, name, email, password, role='producer'):
        self.id = id
        self.name = name
        self.email = email
        self.password = password  # Em produção, use hash!
        self.role = role
        self.company_name = ""

    @staticmethod
    def get(user_id):
        # Busca usuário por ID na lista
        return next((u for u in users_db if u.id == user_id), None)

    @staticmethod
    def get_by_email(email):
        # Busca usuário por Email na lista
        return next((u for u in users_db if u.email == email), None)

    @staticmethod
    def create(name, email, password, role='producer'):
        new_user = User(generate_uuid(), name, email, password, role)
        users_db.append(new_user)
        return new_user

class Product:
    def __init__(self, product_id, name, category, producer_id, harvest_date, quantity, unit):
        self.id = generate_uuid()
        self.product_id = product_id
        self.name = name
        self.category = category
        self.producer_id = producer_id
        self.harvest_date = harvest_date
        self.quantity = quantity
        self.unit = unit
        self.status = 'harvested'
        self.created_at = datetime.utcnow()

    @staticmethod
    def get_all_by_producer(producer_id):
        return [p for p in products_db if p.producer_id == producer_id]

    @staticmethod
    def create(product_id, name, category, producer_id, harvest_date, quantity, unit):
        new_product = Product(product_id, name, category, producer_id, harvest_date, quantity, unit)
        products_db.append(new_product)
        return new_product