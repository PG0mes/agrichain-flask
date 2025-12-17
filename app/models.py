from flask_login import UserMixin
from datetime import datetime
import uuid

# --- SIMULAÇÃO DE BANCO DE DADOS EM MEMÓRIA ---
users_db = []
products_db = []

def generate_uuid():
    return str(uuid.uuid4())

class User(UserMixin):
    def __init__(self, id, name, email, password, role='producer'):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.role = role
        self.company_name = ""

    @staticmethod
    def get(user_id):
        return next((u for u in users_db if u.id == user_id), None)

    @staticmethod
    def get_by_email(email):
        return next((u for u in users_db if u.email == email), None)

    @staticmethod
    def create(name, email, password, role='producer'):
        new_user = User(generate_uuid(), name, email, password, role)
        users_db.append(new_user)
        return new_user


admin_user = User("admin-id", "Super Admin", "admin@agrichain.com", "admin123", "admin")
users_db.append(admin_user)

demo_producer = User("prod-1", "Produtor João", "produtor@agrichain.com", "123456", "producer")
demo_distributor = User("dist-1", "Logística Rápida", "distribuidor@agrichain.com", "123456", "distributor")
demo_retailer = User("ret-1", "Mercado Central", "varejista@agrichain.com", "123456", "retailer")
demo_consumer = User("cons-1", "Maria Consumidora", "consumidor@agrichain.com", "123456", "consumer")

users_db.extend([admin_user, demo_producer, demo_distributor, demo_retailer, demo_consumer])

class Product:
    def __init__(self, product_id, name, category, producer_id, producer_name, harvest_date, quantity, unit):
        self.id = generate_uuid()
        self.product_id = product_id
        self.name = name
        self.category = category
        self.producer_id = producer_id
        self.producer_name = producer_name
        self.harvest_date = harvest_date
        self.quantity = quantity
        self.unit = unit
        self.status = 'harvested'
        self.created_at = datetime.utcnow()

    @staticmethod
    def get_by_id(id):
        return next((p for p in products_db if p.id == id), None)

    @staticmethod
    def get_all():
        """Retorna TODOS os produtos do sistema (para o Admin)"""
        return products_db

    @staticmethod
    def get_all_by_producer(producer_id):
        return [p for p in products_db if p.producer_id == producer_id]

    @staticmethod
    def create(product_id, name, category, producer_id, producer_name, harvest_date, quantity, unit):
        new_product = Product(product_id, name, category, producer_id, producer_name, harvest_date, quantity, unit)
        products_db.append(new_product)
        return new_product