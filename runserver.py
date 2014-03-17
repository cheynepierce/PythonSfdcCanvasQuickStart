import os
from canvas import app
if __name__ == '__main__':
    #if we're running on Heroku, Heroku will set an environment variable containing the correct port
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)