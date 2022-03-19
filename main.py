from LinkedinBot import LinkedinBot
while True:
    job = input('Write the name of the profession you want to search: ')
    page_num = int(input('enter number of page: '))

    if page_num % 25 == 0:
        bot = LinkedinBot(job, page_num)
        print(bot.avarage)
        break
    else:
        print('yeniden dene')
        continue