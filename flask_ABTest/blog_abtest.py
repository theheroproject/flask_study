from flask import Flask, jsonify, request





app = Flask(__name__, static_url_path='/static')

CORS(app)
app.secret_key = 'dave_server1'


@login_manager.user_loader
def load_user(user_id):
    return User.gert(user_id)

@login_manager.unauthorized_handler
def unauthorized():
    return make_response(jsonify(success=False,401))

@app.before_request
def before_request():
    if 'client_id' not in session:
        session['client_id'] = request.environ.get(
            'HTTP_X_REAL_IP', request.remote_addr
        )

if __name__ == '__main__':
    app.run(host="0.0.0.0",port = "8080")