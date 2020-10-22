
from flask import Flask, render_template,request,redirect,url_for
from authenicationcontrol import Authentication
app = Flask(__name__)


@app.route('/',methods=['POST','GET'])
def index():
    control =Authentication()
    if request.method == 'POST':
        register_status=control.registerNewUser(request)
        if register_status ==1:
            return render_template('index.html')
        else:
            return redirect(url_for(index))

    return render_template('index.html')

@app.route('/movies')
def movies():
    return render_template('movies.html')




if __name__ == '__main__':
    app.run()
