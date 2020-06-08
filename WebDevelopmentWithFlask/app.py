# This is basic example of web development with Flask. There are other complex Python web development frameworks like Django
# Flask has other features like User management (Login/logout) with session management. Need to explore more on Flask

from flask import Flask, render_template, request, redirect, url_for

# Create a Flask app with an unique name (__name__ will be always unique for an application)
# __name__ will be __main__ for a running script and all other scripts will have different names
app = Flask(__name__)

# posts is dict of dict
posts = {
    0: {
        'title': 'Hello, world',
        'content': 'This is my first blog post!'
    }
}


# Decorator for path of home page - First Flask endpoint
@app.route('/')
def home():
    # return 'Hello World!' # Displays a string on home page
    return render_template('home.jinja2', posts=posts)


@app.route('/post/<int:post_id>')  # /post/0
def post(post_id):   # post_id = 0
    post = posts.get(post_id)
    if not post:
        return render_template('404.jinja2', message=f'A post with id {post_id} was not found.')
    return render_template('post.jinja2', post=post)  # post is a dict
    # return render_template('post.html', post=post)  # passing params to plain html is also possible


@app.route('/post/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        post_id = len(posts)
        posts[post_id] = {'id': post_id, 'title': title, 'content': content}
        return redirect(url_for('post', post_id=post_id)) # Redirect to post page in case of POST
    return render_template('create.jinja2') # submit to same page in case of GET


if __name__ == '__main__':
    app.run(debug=True) # Run the application with debug mode as True (only during development)
