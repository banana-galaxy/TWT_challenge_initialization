import requests, os
from bs4 import BeautifulSoup as BS
from tqdm import tqdm

CHALLENGE_NUMBER = ''

BASE_DOWNLOAD_URL = "https://raw.githubusercontent.com/Pomroka/TWT_Challenges_Tester/main/Challenge_"
BASE_CHECK_URL = "https://github.com/Pomroka/TWT_Challenges_Tester/tree/main/Challenge_"

if CHALLENGE_NUMBER == '':
    num_found = False
    for char in os.path.dirname(os.path.abspath(__file__))[::-1]:
        if not num_found:
            if char.isdigit():
                num_found = True
                CHALLENGE_NUMBER += char
        else:
            if char.isdigit():
                CHALLENGE_NUMBER += char
            else:
                break
    CHALLENGE_NUMBER = CHALLENGE_NUMBER[::-1]


def download(ffile):
    with open(ffile, 'wb') as f:
        f.write(requests.get(BASE_DOWNLOAD_URL+CHALLENGE_NUMBER+"/"+ffile).content)


def main():
    files = BS(requests.get(BASE_CHECK_URL+CHALLENGE_NUMBER).content.decode('utf-8'), 'html.parser')
    files = [i.text for i in files.find_all("a", class_="js-navigation-open Link--primary")]
    if len(files) == 0:
        quit(f"Challenge {CHALLENGE_NUMBER} has not been published yet. Please try again later.")

    found_files = []
    for i in files:
        if os.path.exists(i):
            found_files.append(i)

    if len(found_files) > 0:
        do_it = input(f"The following files have been found that WILL be overwritten: {[i for i in found_files]}\nDo you wish to continue? [Y/n] ")
        if do_it in ['n', 'N']:
            quit()

    print("\nDownloading files")
    for i in tqdm(files):
        download(i)


if __name__ == "__main__":
    main()
