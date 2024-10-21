from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

refresh_token = ''

scopes = ['https://www.googleapis.com/auth/display-video']

credentials = Credentials(
    None,
    refresh_token=refresh_token,
    token_uri='https://oauth2.googleapis.com/token',
    client_id='',
    client_secret=''
)
# test
# Create DV360 API instance
dv360 = build('displayvideo', 'v1', credentials=credentials)

# Report body
report_body = {
    'params': {
        'type': 'TYPE_GENERAL',
        'groupBy': [
            'FILTER_DATE',
            'FILTER_ADVERTISER'
        ],
        'metrics': [
            'METRIC_REACH',
            'METRIC_CLICKS',
            'METRIC_IMPRESSIONS'
        ],
        'filters': [
            {
                'type': 'FILTER_ADVERTISER',
                'value': '1445418696'
            }
        ],
        'dateRange': {
            'startDate': {'year': 2024, 'month': 1, 'day': 1},
            'endDate': {'year': 2024, 'month': 1, 'day': 31}
        }
    },
    'metadata': {
        'title': 'My DV360 Report',
        'dataRange': 'CUSTOM_DATES',
        'format': 'CSV'
    },
    'schedule': {
        'frequency': 'ONE_TIME'
    }
}

try:
    # Create report query
    dv360_request = dv360.queries().create(body=report_body)
    created_query = dv360_request.execute()
    print(f"Report query created: {created_query['queryId']}")

    # Run the created report
    query_id = created_query['queryId']
    dv360_request = dv360.queries().run(queryId=query_id, body={})
    dv360_request.execute()
    print("Report executed")

except Exception as e:
    print(e)
