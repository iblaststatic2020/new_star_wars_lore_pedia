from flask import request, jsonify, send_from_directory, render_template
from app import app, db
from models import User, Article
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user, login_required

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], email=data['email'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'Registration successful'})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password, data['password']):
        login_user(user)
        return jsonify({'message': 'Login successful'})
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logout successful'})

@app.route('/articles', methods=['GET'])
def get_articles():
    articles = Article.query.all()
    output = []
    for article in articles:
        article_data = {'id': article.id, 'title': article.title, 'content': article.content, 'author': article.author.username}
        output.append(article_data)
    return jsonify({'articles': output})

@app.route('/article/<id>', methods=['GET'])
def get_article(id):
    article = Article.query.get_or_404(id)
    return jsonify({'title': article.title, 'content': article.content, 'author': article.author.username})

@app.route('/article', methods=['POST'])
@login_required
def create_article():
    data = request.get_json()
    new_article = Article(title=data['title'], content=data['content'], author_id=current_user.id)
    db.session.add(new_article)
    db.session.commit()
    return jsonify({'message': 'Article created'})
