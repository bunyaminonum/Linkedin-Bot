from LinkedinBot_search_item import Search
from getpass4 import getpass
def main():
    while True:
        try:
            email = input('enter e-mail: ')
            password = getpass('enter password: ')
            job_name = input('job name: ')
            num_page = int(input('name of page: '))

            print(f"avarage: {search.average}")
            break
        except:
            print('wrong input! try again...')
            continue
        search = Search(email, password, job_name, num_page)

if __name__ == '__main__':
    main()