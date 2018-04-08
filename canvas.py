import json
#iron.io
#token UldP2WNEb7KRwOg0OmgH
#proj id 5ac90bddf8ec9c000b09db31
#
#twilio
#+12016769712

import pandas
import requests
import datetime
from twilio.rest import Client

#Call API to get JSON file
url = "http://utexas.instructure.com/api/v1/courses/1217790/assignments"

querystring = {"bucket":"upcoming"}

headers = {
    'Authorization': "Bearer 1017~G0aXMhrXuND2mxLsBZ9vIN2R7oHJpwS8QMurHtEz2SAalcMtaFmwLGGBZHM6aXzw",
    'Cache-Control': "no-cache",
    'Postman-Token': "3b253fe1-9819-4f18-8611-1e21b941990b"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
json_data = json.loads(response.text)

#Take only Name & Date of assignments
assignments=[]
due_dates=[]
submission=[]
i = 0

for i in json_data:
    assignments.append(i['name'])
    due_dates.append(i['due_at'])
    submission.append(i['has_submitted_submissions'])
    
print("Your upcoming assignments are:")
print(''.join(assignments))
print("Your upcoming due dates are:")
print(''.join(due_dates))

account = "AC84869c6273365b25abc7f71947391674"
token = "523fde5645063b82470cdcaaf48cf97f"
client = Client(account, token)

for i in due_dates:
    due_time = ''.join(due_dates)
    due_time_date = pandas.to_datetime(due_time)

worker = IronWorker()
i=0
while i < len(assignments):
    if submission[i] == False:
        task = Task(code_name="SendText")
        task.start_at = due_time_date - timedelta(hours=3)
        task.scheduled = True
        response = worker.queue(task)
    i+=1
