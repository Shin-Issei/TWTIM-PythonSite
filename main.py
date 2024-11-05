from website import create_app

app = create_app()

if __name__ == '__main__': # only run webserver if we run the file itself!
    app.run(debug=True) # auto re run webserver on change.

    