#Python Canvas App Quick Start

###Introduction
This is a basic Python web app, written using [Flask](http://flask.pocoo.org/) and the [SalesforceCanvasFrameworkSDK](https://github.com/forcedotcom/SalesforceCanvasFrameworkSDK). You can use it to get a Salesforce Canvas app using Python up and running quickly.

###Basic Setup
First, ensure you have [pip](https://pypi.python.org/pypi/pip) and [virtualenv](https://pypi.python.org/pypi/virtualenv) installed. Create a directory for your project and clone the repository into that directory.

```
git clone https://github.com/cheynepierce/PythonSfdcCanvasQuickStart.git
cd PythonSfdcCanvasQuickStart
git submodule init
git submodule update
```

Now, create a Python virtualenv

```
virtualenv venv
source venv/bin/activate
```

Next, install dependencies using pip:

```
pip install Flask gunicorn
```

###Deploy to Heroku
You can deploy this app anywhere you want and it will be able to run on Force.com Canvas, as long as it has an https endpoint. To deploy to Heroku, do the following:

```
heroku create
git push heroku master
```

After committing changes, you can always do "git push heroku master" again to deploy the changes.

###Create a Salesforce Connected App
To set up the Canvas app, log into your Salesforce development environment, and go to Setup -> Create -> Apps, scroll down to the connected apps section, and create a new conencted app. Under the API section, check the box to "Enable OAuth Settings." Set the callback URL to "https://yourAppName.herokuapp.com/callback.html". Under Canvas App Settings, check the "Force.com Canvas" box. Set the Canvas App URL to "https://yourAppName.herokuapp.com/". 

Click Create. Once your app is created, copy the app's Consumer Secret. Create an environment variable called CANVAS_CONSUMER_SECRET and set it to this value. If your app is running on Heroku, you can do this as follows:

```
heroku config:add CANVAS_CONSUMER_SECRET=<consumer_secret>
```

Now, go to Setup -> Canvas App Previewer and click on your app's name in the left panel. The app should display in the right panel.