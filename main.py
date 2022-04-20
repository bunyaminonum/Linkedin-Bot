from LinkedinBot_search_item import Search
def main():
    while True:
        try:
            email = input('enter e-mail: ')
            password = input('password: ')
            job_name = input('job name: ')
            num_page = int(input('name of page: '))
            search = Search(email, password, job_name, num_page)
            print(f"avarage: {search.average}")

            break
        except:
            print('wrong input! try again...')
            continue

if __name__ == '__main__':
    main()
