from datetime import datetime

# search
keyword_1 = 'EA'
keyword_2 = 'Electronic Arts'
keyword_3 = 'Data'

#search_query = 'site:linkedin.com/in/ AND "' + keyword_1 + '" AND "' + keyword_2
search_query = 'site:linkedin.com/in/ AND "' + keyword_1 + '" OR "' + keyword_2 + '"' + '" AND "' + keyword_3

# output
date = str(datetime.now().year) + '-' + str(datetime.now().month) + '-' + str(datetime.now().day)
#file_name = keyword_1.replace(' ', '_') + '-' + keyword_2.replace(' ', '_') + '-' + 'results' + date + '.csv'
file_name = keyword_1.replace(' ', '_') + '-' + keyword_2.replace(' ', '_') + '-' + keyword_3.replace(' ', '_') + '-' + 'results' + date + '.csv'

#linkedin ids
linkedin_username = 'axelcoudray@outlook.com'
linkedin_password = 'AX98yeti&'