from datetime import datetime

# search
keyword_1 = 'Analyst'
keyword_2 = 'Wargaming'
keyword_3 = 'Data'

nb_pages = 6
waiting_time = 10

search_query = 'site:linkedin.com/in/ AND "' + keyword_1 + '" AND "' + keyword_2
#search_query = 'site:linkedin.com/in/ AND "' + keyword_1 + '" OR "' + keyword_2 + '"' + '" AND "' + keyword_3

# output
date = str(datetime.now().year) + '-' + str(datetime.now().month) + '-' + str(datetime.now().day)
file_name = keyword_1.replace(' ', '_') + '-' + keyword_2.replace(' ', '_') + '_' + 'results' + '_' + date + '.csv'
#file_name = keyword_1.replace(' ', '_') + '-' + keyword_2.replace(' ', '_') + '-' + keyword_3.replace(' ', '_') + '_' + 'results' + '_' + date + '.csv'

#linkedin ids
linkedin_username = 'axelcoudray@outlook.com'
linkedin_password = 'AX98yeti&'