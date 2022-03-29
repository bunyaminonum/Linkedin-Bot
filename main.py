import warnings
from LinkedinBot_search_item import Search
warnings.filterwarnings("ignore")
while True:
    try:
        email = input('enter e-mail: ')
        password = input('enter password: ')
        job_name = input('job name')
        num_page = int(input('name of page'))
        a = Search(email, password, job_name, num_page)
        print(a.avarage)
        break
    except:
        print('wrong input! try again...')
        continue