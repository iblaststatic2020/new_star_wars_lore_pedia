from flask import Blueprint, request, jsonify, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user, login_required
from models import User, Article
from app import db
import os

main = Blueprint('main', __name__, static_folder='../frontend/build', static_url_path='/')

@main.route('/', defaults={'path': ''})
@main.route('/<path:path>')
def serve(path):
    requested_path = os.path.join(main.static_folder, path)
    if path and os.path.exists(requested_path):
        return send_from_directory(main.static_folder, path)
    return send_from_directory(main.static_folder, 'index.html')

@main.route('/register', methods=['POST'])
def register_user():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not all([username, email, password]):
        return jsonify({'message': 'Missing username, email, or password'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Username already exists'}), 400

    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

@main.route('/login', methods=['POST'])
def login_user_route():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    print(f"Received login request for username: {username}")

    user = User.query.filter_by(username=username).first()
    print(f"user value is: {check_password_hash(user.password, password)}")
    if user and check_password_hash(user.password, password):
        login_user(user)
        return jsonify({'message': 'Login successful'})
    
    return jsonify({'message': 'Invalid credentials'}), 401

@main.route('/logout', methods=['POST'])
@login_required
def logout_user_route():
    logout_user()
    return jsonify({'message': 'Logout successful'})

@main.route('/articles', methods=['GET'])
def get_articles():
    articles = Article.query.all()
    output = [{'id': article.id, 'title': article.title, 'content': article.content, 'author': article.author.username} for article in articles]
    return jsonify({'articles': output})

@main.route('/article/<int:id>', methods=['GET'])
def get_article(id):
    article = Article.query.get_or_404(id)
    return jsonify({'title': article.title, 'content': article.content, 'author': article.author.username})

@main.route('/article', methods=['POST'])
@login_required
def create_article():
    data = request.get_json()
    new_article = Article(title=data.get('title'), content=data.get('content'), author_id=current_user.id)
    db.session.add(new_article)
    db.session.commit()
    return jsonify({'message': 'Article created'})
