# Minimalistic Flask App 
Minimalistic flask application factory, to start from. Already with a blueprint configured.
## Setup
On a console, e.g. terminal in PyCharm type:
1. `git clone https://github.com/btcorgtfo/flask_app_minimalistic.git` 
2. Windows: `conda create -n minimalistic_flask_app python=3.8`
3. Linux: have a look how to create a virutal env e.g. [here](https://wiki.ubuntuusers.de/virtualenv/)
3. `pip install -r requirements.txt`
4. `python wsgi.py` will start the server locally

Output will then look like

``` 
* Serving Flask app "application" (lazy loading) 
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 225-396-979
 * Running on http://localhost:5000/ (Press CTRL+C to quit)
```
## Debug mode 
Per default, debug mode is active. This means than once you chance something in the code, the server will restart. 
Turn it of in  `config.py` if not needed.

## Access the web api
Now either click on the link or open a browser and go to [http://localhost:5000](http://localhost:5000).

As there are two routes (endpoints) in this example you can also go to `/songs` to explore the html example.
