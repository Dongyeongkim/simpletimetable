from datetime import datetime

TimetableList = [
    {'Network Programming': '7863685919',
     'Industrial Mathematics(kim)': 'google-meet',
     'Business English': '4700404365',
     'Classical Literature': '3300965795',
     'Database Programming': '9785689787',
     'Homeroom time': 'google-meet'},
    {'Business English': '4700404365',
     'Industrial Mathematics(Lee)': '7987833794',
     'English II': '7385237525',
     'Classical Literature': '3300965795',
     'BigData Analysis': '4679526373',
     'General Engineering': '5363759347',
     'My FUTURE': '3650046422'
     },
    {'Computer Security': '3335559622',
     'Database Programming': '9785689787',
     'Calculus': 'google-meet',
     'General Engineering': '5363759347',
     'CA': 'NONE'
     },
    {'General Engineering': '5363759347',
     'Database Programming': '9785689787',
     'English II': '7385237525',
     'BigData Analysis': '4679526373',
     'Computer Security': '3335559622'
     },
    {'My FUTURE': '3650046422',
     'Network Programming': '7863685919',
     'BigData Analysis': '4679526373',
     'Database Programming': '9785689787',
     'Industrial Mathematics(Lee)': '7987833794'
     }
]


def zoom_link_generator(day):
    for i in TimetableList[day]:
        if i == 'BigData Analysis':
            print(i + ':https://zoom.us/j/' + TimetableList[day][i])
        elif i in ['Calculus', 'Homeroom time', 'Industrial Mathematics(kim)']:
            print(i + 'google-meet')
        elif i == 'CA':
            print(i + ': NONE')
        else:
            print(i + ':https://zoom.us/j/' + TimetableList[day][i])


zoom_link_generator(datetime.today().weekday())
