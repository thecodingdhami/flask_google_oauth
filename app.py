from flask import Flask, redirect, url_for, session, render_template
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = "my_super_secret_key_123"

# OAuth setup with correct OIDC metadata
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id="588043608380-flofi75vgoitra3ocu0qqm05h312npa3.apps.googleusercontent.com",
    client_secret="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",
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid email profile'}
)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    redirect_uri = url_for('auth', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/auth')
def auth():
    token = google.authorize_access_token()
    user_info = token.get('userinfo')  # Authlib now fetches user info automatically
    session['user'] = user_info
    return redirect('/profile')

@app.route('/profile')
def profile():
    user = session.get('user')
    if user:
        return render_template('profile.html', user=user)
    return redirect('/')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
