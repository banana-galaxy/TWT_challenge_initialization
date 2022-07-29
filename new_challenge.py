import os, sys, shutil
from pprint import pprint


def create_challenge(name):
    os.mkdir(name)
    with open(f"{name}/solution.py", 'w') as f:
        f.write('''T = int(input())

for _ in range(T):
    pass
''')
    with open(f"{name}/get_tester.py", 'w') as f:
        f.write(r'''import requests, os

BASE_URL = "https://raw.githubusercontent.com/Pomroka/TWT_Challenges_Tester/main/Challenge_"

CHALLENGE_NUMBER = ''

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

files = [f"test_challenge_{CHALLENGE_NUMBER}.py", 'test_cases.json.gz', 'test_cases_b.json.gz']
found_files = []
for i in files:
    if os.path.exists(i):
        found_files.append(i)

if len(found_files) > 0:
    do_it = input(f"The following files have been found that WILL be overwritten: {[i for i in found_files]}\nDo you wish to continue? [Y/n] ")
    if do_it in ['n', 'N']:
        quit()

print("Looking for python file...")
tester_content = requests.get(f'{BASE_URL+CHALLENGE_NUMBER}/test_challenge_{CHALLENGE_NUMBER}.py').content.decode('utf-8')

if tester_content == "404: Not Found":
    quit(f'Challenge {CHALLENGE_NUMBER} tester not yet published, please try again later.')

print("Writing python file...")
with open(f'test_challenge_{CHALLENGE_NUMBER}.py', 'w') as f:
    f.write(tester_content)

print("Writing test cases file...")
with open(f'test_cases.json.gz', 'wb') as f:
    f.write(requests.get(f'{BASE_URL+CHALLENGE_NUMBER}/test_cases.json.gz').content)

print("Looking for big test cases file...")
big_cases = 'test_cases_b.json.gz'
big_cases_content = requests.get(f'{BASE_URL+CHALLENGE_NUMBER}/{big_cases}').content

try:
    big_cases_content.decode('utf-8')
    print("No big test cases available.")
except UnicodeDecodeError:
    print("Writing big test cases file...")
    with open(big_cases, 'wb') as f:
        f.write(big_cases_content)
''')


def main():
    if len(sys.argv) == 1:
        dirs = []
        for item in os.listdir('.'):
            if os.path.isdir(item) and "challenge" in item:
                dirs.append(int(float(item.split('e')[2].split('(')[0])))

        dirs.sort(reverse=True)
        create_challenge(f"challenge{dirs[0]+1}")
        print(f"challenge{dirs[0]+1} created")
    else:
        chname = sys.argv[1]
        if len(sys.argv) > 2:
            chname = ''.join(sys.argv[1:])

        if os.path.exists(chname):
            print(f"The {chname} directory already exists, and has the following contents:")
            pprint(os.listdir(chname))
            overwrite = input("Do you want to overwrite it? [y/N] ")
            if overwrite in ['', 'n', 'N']:
                quit()
            else:
                shutil.rmtree(chname)
        create_challenge(chname)
        print(f"{chname} created")


if __name__ == "__main__":
    main()
