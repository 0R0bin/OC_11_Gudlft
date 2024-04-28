import json
from flask import Flask,render_template,request,redirect,flash,url_for


def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


def initPointsPerComp(clubs, competitions):
    obj_to_return = {}

    for club in clubs:
        list_to_add = {}
        for competition in competitions:
            list_to_add[competition['name']] = {'places': 0}

        obj_to_return[club['name']] = list_to_add

    return obj_to_return

app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()
count_places = initPointsPerComp(clubs, competitions)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSummary',methods=['POST'])
def showSummary():
    club = [club for club in clubs if club['email'] == request.form['email']][0]
    return render_template('welcome.html',club=club,competitions=competitions)


@app.route('/book/<competition>/<club>')
def book(competition,club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    # Vérif > 12
    places_already_booked = count_places[club['name']][competition['name']]['places']

    if placesRequired > 12 or (12 - places_already_booked - placesRequired) < 0:
        flash('You can\'t take more than 12 places by competition.')
        return render_template('booking.html', club=club, competition=competition), 400
    else:
        count_places[club['name']][competition['name']]['places'] = places_already_booked + placesRequired
    
    competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired

    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))