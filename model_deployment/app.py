import flask
import numpy as np
import pickle

app = flask.Flask(__name__, template_folder='templates')

@app.route('/')
def main():
    return(flask.render_template('main.html'))

@app.route('/prediction', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in flask.request.form.values()]
    final_features = [np.array(int_features)]
    model = pickle.load(open('model/model_classifier.pkl', 'rb'))
    prediction = model.predict(final_features)

    output = {0: 'Sorry, you are deceased', 1: 'Congrats! You survived'}

    return flask.render_template('main.html', prediction_text='{}'.format(output[prediction[0]]))

if __name__ == '__main__':
    app.run()