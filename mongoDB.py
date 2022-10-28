import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.trendyol.com/laventin/profesyonel-selulit-ve-catlak-karsiti-bolgesel-incelme-icin-soguk-lipoliz-jel-250-ml-p-208776930?boutiqueId=601988&merchantId=249592')
soup = BeautifulSoup(r.content, 'html.parser')
kupon = soup.findAll('div', {'class':'coupon-price-content'})
kupon2 = soup.findAll('div', {'class':'coupon-discount'})
print(kupon, kupon2)
for i in  kupon:
    print(i.get_text)