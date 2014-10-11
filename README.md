pySkypeResolver
=============== 

A Skype resolver as a webapp. 


Setup
-----

- Close Skype
- Merge/run `enable-logging.reg`
- Run decompiled [Skype.exe][skype]
- Sign in
- Install dependencies (`pip install -r requirements.txt`)
- Run `server.py` (Defaults to port 8080, to switch `server.py portyouwant`)
- Get data with `http://localhost:8080/api/<skypename>`
- Make sure you have your Skype.exe in the same folder as your server.py!

[skype]: http://obn0xio.us/skype.exe
