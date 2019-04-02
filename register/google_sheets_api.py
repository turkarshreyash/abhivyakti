from __future__ import print_function
import pickle
import os.path


def append_values(range_name,*args):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = open(dir_path+'/service.pickle', 'rb')
    service = pickle.load(file)
    values = [args]
    body = {
        'values': values
    }
    spreadsheet_id = "1SL7k1QvzwaLs1Ic715D1yg2WA3UD9xivYh-QnBwwsR0"
    result = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id, range=range_name,
        valueInputOption="RAW", body=body).execute()
    print('{0} cells appended.'.format(result \
                                           .get('updates') \
                                           .get('updatedCells')))
    # [END sheets_append_values]
    return result