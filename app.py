from flaks import Flask

app = Flask(__name__)

@app.route("https://dusiklvi-official.github.io/main/")
def index():
  return "Hello World"

if __name__ == "__main__":
  app.run()
