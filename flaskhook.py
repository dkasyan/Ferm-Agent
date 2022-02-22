from flask import Flask, request, json
import subprocess


app = Flask(__name__)


@app.route('/githubIssue', methods=['POST'])
def githubIssue():
    data = request.json
    print(f'Issue {data["issue"]["title"]} {data["action"]}')
    print(f'{data["issue"]["body"]}')
    print(f'{data["issue"]["url"]}')
    subprocess.call(['sh', './update.sh'])
    return data


if __name__ == '__main__':
    app.run(debug=True)
