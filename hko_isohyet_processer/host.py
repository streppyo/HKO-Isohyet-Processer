from flask import Flask, render_template, url_for, request, send_from_directory
import os
import main


app = Flask(__name__)

@app.route('/weather/isohyet', methods=['GET'])
def isohyet():
    ts = request.args.get("date")
    print(ts)
    main.GenerateIsohyet(str(ts))
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)) + r'\static\images', str(ts) + '.png')

if __name__ == '__main__':
    app.run()
