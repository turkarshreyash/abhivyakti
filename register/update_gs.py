from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import os 



def update_google_sheets(range,*argv):
    SCOPES = 'https://www.googleapis.com/auth/drive'
    spreadsheet_id = '1yaYioBBVK7_QccId9UqQajNKXmW2mIlAAJcgkThpPxs'
    range_name = range
    dir_path = os.path.dirname(os.path.realpath(__file__))

    store = file.Storage(dir_path+'/google_auth/token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(dir_path+'/google_auth/credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

        # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheet_id ,
                                    range=range_name).execute()
    values = [argv,]
    body = {
        'values': values
    }
    result = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id, range=range_name,
        valueInputOption='RAW', body=body).execute()