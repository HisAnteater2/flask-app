### How to use the API
* use the url ```<domain-name>/user/<username>/<password>/<score>``` to post username and score

* send get request to ```<domain-name>``` to get Leader Board

### Test if API working properly on local server
``` bash
pip install -r requirements.txt
python app.py
```
In a separate terminal
```bash
# Login by passing score as 0
$ curl -X POST http://127.0.0.1:5000/user/test4/dummy_passwd/0
{
  "action": "success"
}
# If a login attempt is made again with different password it would lead to failure
$ curl -X POST http://127.0.0.1:5000/user/test4/dmmy_passwd/0
{
  "action": "failure"
}
# After game ends post the score of the user with correct username and password
$ curl -X POST http://127.0.0.1:5000/user/test4/dummy_passwd/1
{
  "action": "success"
}
# When data for Leader Board is to be fetched
$ curl http://127.0.0.1:5000/
{
  "test4": {
    "score": 1
  }
}
```
