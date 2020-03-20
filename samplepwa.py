from app import app
'''
NOTES/ISSUES
 - use the virtualenv with `source venv/bin/activate`
 - manifest.json icons won't load, it's in /app/static/manifest.json
 - authentication is jank, replace with oauth
 - using google maps embedded
 - kinda jank that we intialize firebase twice

 TODO:
 - use location to center map and add blue dot if not there already
 - push location to database and pull all other data with red markers
 - can't use auth.currentUser, need to listen to onAuthStateChanged 
'''
