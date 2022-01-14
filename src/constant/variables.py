from datetime import datetime

# search
keyword_1 = 'Epic Games'
keyword_2 = 'Engineers'

search_query = 'site:linkedin.com/in/ AND "' + keyword_1 + '" AND "' + keyword_2 + '"'

# output
date = str(datetime.now().year) + '-' + str(datetime.now().month) + '-' + str(datetime.now().day)
file_name = keyword_1.replace(' ', '_') + '-' + keyword_2.replace(' ', '_') + 'results' + date + '.csv'

#linkedin ids
linkedin_username = 'axelcoudray@outlook.com'
linkedin_password = 'AX98yeti&'