# TWT challenge initialization

This tiny project aims to simplify the process of organizing your twt weekly challenges directory and downloading Yantovis' test files.
___
## How to use

*This "how to" assumes your twt weekly challenge directory structure to be similar to this:*
```
- TWT_challenges
    - challenge50
        - solution.py
    - challenge51
        - solution.py
```

Download `new_challenge.py` and put it in the root folder of your TWT weekly challenges directory. In the above example we would put it in the `TWT_challenges` directory so it would end up looking like this:
```
- TWT_challenges
    - challenge50
        - solution.py
    - challenge51
        - solution.py
    - new_challenge.py
```
You can now run `new_challenge.py` from within `TWT-challenges` which will try to determine the last challenge you did by looking at the existing folders and create a folder for the next challenge.

If you haven't done challenges in a while or this is your first time doing them, you can specify what to call the new folder when running the command: `python3 new_challenge.py challenge52`

You'll end up with a new folder which will look like this: 
```
- TWT_challenges
    - challenge50
        - solution.py
    - challenge51
        - solution.py
    - challenge52
        - solution.py
        - get_tester.py
    - new_challenge.py
```
`solution.py` will contain a python template for the challenge, and `get_tester.py` can be run to download Yantovis' tester for the challenge.

---

## What if my organization system is different?
You can still download `get_tester.py`, put it into the current challenge folder, run it, and it'll download the tester for you.

## What about other languages?
Currently `new_challenge.py` can only make a python template. I might add an option for other language templates in the future.