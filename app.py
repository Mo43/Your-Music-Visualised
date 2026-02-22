from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    conn = sqlite3.connect("music.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, artist, album, duration_ms, popularity FROM tracks")
    songs = cursor.fetchall()
    conn.close
    return render_template('index.html', songs = songs)




if __name__ == "__main__":
    app.run(debug=True)

