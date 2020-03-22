from app import app
'''
NOTES/ISSUES
 - use the virtualenv with `source venv/bin/activate`
 - manifest.json icons won't load, it's in /app/static/manifest.json
 - authentication is jank, replace with oauth
 - using google maps embedded
 - kinda jank that we intialize firebase twice

 TODO:
 - database structure:
    - users
        - name
        - email
        - friends (later)
    - sessions
        - email_of_student
        - latitude
        - longitude
        - location_description (later)
        - start_time (later)
        - duration (later)
 - add blue dot at current location, allow user to move it elsewhere
 - when user starts a session, add it to database
 - all other users take snapshot of change and have red marker on their screen
 - marker should have a popup that fills screen with info abt session
 - do we rlly need firebase auth anymore? just using oauth2 and RealtimeDB
'''
