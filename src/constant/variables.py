from datetime import datetime

# search
keyword_1 = 'Art Pipeline'
keyword_2 = 'Epic Games'
keyword_3 = 'Epic Games'

nb_pages = 15
waiting_time = 10

search_query = 'site:linkedin.com/in/ AND "' + keyword_1 + '" AND "' + keyword_2
#search_query = 'site:linkedin.com/in/ AND "' + keyword_1 + '" OR "' + keyword_2 + '"' + '" AND "' + keyword_3
#search_query = 'site:linkedin.com/in/ AND "' + keyword_1 + '" AND "' + keyword_2 + '"' + '" AND "' + keyword_3

# output
date = str(datetime.now().year) + '-' + str(datetime.now().month) + '-' + str(datetime.now().day)
file_name = keyword_1.replace(' ', '_') + '-' + keyword_2.replace(' ', '_') + '_' + 'results' + '_' + date + '.csv'
# file_name = keyword_1.replace(' ', '_') + '-' + keyword_2.replace(' ', '_') + '-' + keyword_3.replace(' ', '_') + '_' + 'results' + '_' + date + '.csv'
