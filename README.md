# github-explorer
Simple Python Flask API and UI for exploring github org repositories


git clone and cd to directory...

#### install dependencies (python2.7)
```
python setup.py develop
```
######OR
```
pip install requirements.txt
```

#### web server (http://localhost:8080)
```
python server.py
```

#### tests
```
nosetests
```


####Notes
This is a python (flask) web server with two api endpoints, and a single page app.


######JS
I chose to keep the client build simple by not including a package manager and commonJS style module loader.
On larger projects this is standard but I didn't feel it was required here. I did however still want to use react for my view templates.
To do this I'm using the client-side transformer. I layed out the client code mostly in the
`main.js` file. If I had included a module loader guaranteed each of those literal objects would have gone into their own separate file.

######UI
I used [skeleton](http://getskeleton.com/) for the CSS and responsive layout.


If there was more time here are a few of the things I would have included:
- caching on the server requests
- browser history support (back/forward) between commits and repos
- javascript common style module loader and gulp/grunt build
