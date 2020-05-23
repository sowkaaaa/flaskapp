# -*- coding: utf-8 -*-
# quiz/quiz.py

from flask import Flask
from flask import render_template
from flask import request, redirect, url_for, flash

app = Flask(__name__)

# konfiguracja aplikacji
app.config.update(dict(
	SECRET_KEY='bardzosekretnysekret',
))

# lista pytań
DANE = [{
  'pytanie': 'Stolica Hiszpani, to:', 
  'odpowiedzi': ['Madryt', 'Warszawa', 'Barcelona'],  
  'odpok': 'Madryt'}, 
  {
  'pytanie': 'Objętość sześcianu o boku 6 cm, wynosi:',
  'odpowiedzi': ['36', '216', '18'],
  'odpok': '216'},
  {
  'pytanie': 'Symbol pierwiastka Helu, to:',
  'odpowiedzi': ['Fe', 'H', 'He'],
  'odpok': 'He'},
  {
  'pytanie': 'Potoczna nazwa Kanczyla Srebrnogrzbietego, to:',
  'odpowiedzi': ['Sarna', 'Świnia rzeczna', 'Myszojeleń'],
  'odpok': 'Myszojeleń'},
   {
  'pytanie': 'Co to są liczby parzyste:',
  'odpowiedzi': ['To te liczby, które mają parę.', 'Liczby podzielne przez dwa.', 'Ktoś bez pary.'],
  'odpok': 'Liczby podzielne przez dwa.'},
]

@app.route('/', methods=['GET', 'POST'])
def index():
    
    # return 'Cześć, tu Python!'
    return render_template('index.html', pytania=DANE)

@app.route('/odp', methods=['GET', 'POST'])
def odp():

    if request.method == 'POST':
        punkty = 0
        odpowiedzi = request.form

        for pnr, odp in odpowiedzi.items():
            if odp == DANE[int(pnr)]['odpok']:
                punkty += 1

        flash('Liczba poprawnych odpowiedzi, to: {0}'.format(punkty))
        return redirect(url_for('odp'))

    # return 'Cześć, tu Python!'
    return render_template('odp.html', pytania=DANE)

if __name__ == '__main__':
    app.run(debug=True)