from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255))
    image_url = db.Column(db.String(255))
    likes = db.relationship('Like', backref='post', lazy=True)
    comments = db.relationship('Comment', backref='post', lazy=True)

class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

db.create_all()

@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@app.route('/create_post', methods=['POST'])
def create_post():
    text = request.form.get('text')
    image_url = request.form.get('image_url')

    new_post = Post(text=text, image_url=image_url)
    db.session.add(new_post)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/like_post/<int:post_id>', methods=['POST'])
def like_post(post_id):
    post = Post.query.get(post_id)
    new_like = Like()
    post.likes.append(new_like)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/comment_post/<int:post_id>', methods=['POST'])
def comment_post(post_id):
    post = Post.query.get(post_id)
    text = request.form.get('comment_text')

    new_comment = Comment(text=text)
    post.comments.append(new_comment)
    db.session.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
