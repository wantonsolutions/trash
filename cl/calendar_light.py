from __future__ import print_function
from datetime import datetime, timedelta
import os.path
import pytz
from dateutil import parser
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


utc=pytz.UTC
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.utcnow() #.isoformat() + 'Z' # 'Z' indicates UTC time
    earlier = timedelta(hours=3, minutes=0)
    before = now - earlier
    beforeString = before.isoformat() + 'Z'
    print(now)
    #print('Getting the upcoming 10 events')

    calendar_list_result = service.calendarList().list().execute()

    #print(calendar_list_result['items'])

    #collect the list of all the calendar items
    for item in calendar_list_result['items']:
        print(item['id'])

        events_result = service.events().list(calendarId=item['id'], timeMin=beforeString,
                                            maxResults=10, singleEvents=True,
                                            orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            end = event['end'].get('dateTime', event['end'].get('date'))
            if 'summary' in event:
                #print(start, end ,event['summary'])
                now=datetime.now()
                startTime = parser.parse(start)
                endTime = parser.parse(end)
                startTime=startTime.replace(tzinfo=utc)
                endTime=endTime.replace(tzinfo=utc)
                now=now.replace(tzinfo=utc)

                if startTime < now and endTime > now:
                    print("IN MEETING!!")


if __name__ == '__main__':
    main()