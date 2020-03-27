from flask import Flask, render_template, request, redirect, abort
import lib.mongo as db
import time


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', db=db.col.find())


@app.route('/shrink', methods=["POST"])
def shrink():
    url = dict(request.form.items())['url']
    db.add(url)

    return redirect('/')


@app.route('/<shrinked>')
def shrinked(shrinked):
    search = {"shrinked": shrinked}
    data = db.col.find_one(search)

    if data and data['url']:
        data["clicks"] += 1
        db.col.replace_one(search, data)

        return redirect(data['url'])

    return abort(404)


@app.route('/delete/<shrinked>')
def delete(shrinked):
    search = {"shrinked": shrinked}
    exists = db.col.find_one(search)

    if exists:
        db.col.delete_one(search)
        
        return redirect('/')

    return abort(404)


if __name__ == '__main__':
    app.run(debug=True)
