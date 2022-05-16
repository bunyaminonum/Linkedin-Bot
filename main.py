from LinkedinBot_search_item import Search
def main():
    search = Search('enter_your_email', 'enter_your_password', 'enter_your_job_name', 'enter_num_page')
    print(f"avarage: {search.average}")

if __name__ == '__main__':
    main()
