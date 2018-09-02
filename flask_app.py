from flask import Flask
import chain_reaction
app = Flask(__name__, static_url_path="/static", static_folder='/home/nfrancque/chain_reaction/static')

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/get_chain')
def hello_world():
	chain = chain_reaction.get_chain()
	return chain
