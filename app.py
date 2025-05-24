from flask import *
import airedirect
app = Flask(__name__)

api_key='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'
model="google/gemini-2.0-flash-001"


urls_disc={
    "home":"contains basic information about the company",
    "about":"This is the about page",
    "services":"This is the services page",
    "products":"This is the products page",
    "blog":"This is the blog page",
    "contact":"contains ceo's contact information",
    'create_account':'contains information about creating an account and resetting password',
    "not_found":"if no pages found"
}


@app.route('/<query>')
def index(query):
    path_to_redirect = airedirect.ask_ai(query, api_key, model, urls_disc)
    path_to_redirect = path_to_redirect.strip().replace('\n', '')
    print(path_to_redirect)
    return redirect(path_to_redirect)

#Example
@app.route('/contact')
def contact():
    return 'This is the contact page'

@app.route('/about')
def about():
    return 'This is the about page'

@app.route('/')
def home():
    return 'Hello world bro this is the home page'

if __name__ == '__main__':
    app.run(debug=True)
