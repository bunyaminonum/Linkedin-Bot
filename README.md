
# Linkedin Bot
https://user-images.githubusercontent.com/59376910/169173303-1a7f6be2-6f13-4c94-9b64-3f7afc6491bd.mp4
 ## Description
This bot searches for a job posting you specify on LinkedIn and adds the number of employees of the company that posted that job posting to a list and averages it.

## Points To Be Considered!
Your LinkedIn account must be a previously logged in account on the same device, otherwise the bot will not work properly.





## Required Modules
* time
* requests
* beautifulsoup4
* webdriver-manager


## Required Browsers

* Firefox

  
## Run Your Computer

### Install Modules

#### webdriver manager
```bash
  pip install webdriver-manager
```

#### requests

```bash
  pip install requests
```

#### beautifulsoup4

```bash
  pip install beautifulsoup4
```


  
## Usage/Examples
* Turkey ID is given to the default geoID. If you wish, you can use the geoID of the region you are in by manually searching on LinkedIn.

```python
from LinkedinBot_search_item import Search
def main():
    search = Search('enter_your_email', 'enter_your_password', 'enter_your_job_name', 'enter_num_page', geoID = 102105699)
    print(f"avarage: {search.average}")

if __name__ == '__main__':
    main()
```

  
