from flask import Flask
import chain_reaction
app = Flask(__name__)

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/get_chain')
def hello_world():
	chain = chain_reaction.get_chain()
	return chain
