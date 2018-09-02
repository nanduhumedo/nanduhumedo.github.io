from flask import Flask
import chain_reaction
app = Flask(__name__)

@app.route('/')
def hello_world():
	chain = chain_reaction.get_chain()
	return chain
