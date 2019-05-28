from bonjour import bonjour
from flask import request,render_template
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
import requests, json, bleach

@bonjour.route("/")

@bonjour.route('/get_keywords')
def keyword():
	motcle1 = request.args.get('keyword1')
	motcle2 = request.args.get('keyword2')
	motcle3 = request.args.get('keyword3')
	return render_template("forumlairespotify.html", lemotcle1 = motcle1, lemotcle2 = motcle2, lemotcle3 = motcle3)

def show_keywords():
	motcle1 = request.form['keyword1']
	motcle2 = request.form['keyword2']
	motcle3 = request.form['keyword3']
	return render_template("affichemotcle.html", lemotcle1=motcle1, lemotcle2=motcle2, lemotcle3=motcle3)

@bonjour.route('/show_list', methods = ['POST'])
def request_spotify():
	motcle1 = request.form['keyword1']
	motcle2 = request.form['keyword2']
	motcle3 = request.form['keyword3']
	authurl = "https://accounts.spotify.com/api/token"
	clientID = "2752a9464abd490590d6e9a9fb7e8505"
	clientSecret = "1a97de1ae6e2462d8811c43294e7c330"
	postdata = {"grant_type" : "client_credentials"}

	client = BackendApplicationClient(client_id=clientID)
	oauth = OAuth2Session(client=client)
	token = oauth.fetch_token(token_url=authurl, client_id=clientID, client_secret=clientSecret)

	head = {"Authorization" : "Bearer " + token["access_token"]}
	baseurl = "https://api.spotify.com/v1"
	endpoint = "/search"
	types = "track"
	payload = {"q":motcle1+' '+motcle2+' '+motcle3,"type":types}
	r = requests.get(baseurl + endpoint, headers=head, params = payload)

	data = json.loads(r.text)

	track_name = []
	url_link = []

	for i in data["tracks"]["items"]:
		track = (i['name'])
		url = (i['external_urls'])
		url2 = (url.get("spotify",""))
		t = track
		u = url2
		track_name.append(t)
		url_link.append(u)

	return render_template("affichemotcle.html", len = len(track_name), track_name = track_name, len2 = len(url_link), url_link = url_link)
