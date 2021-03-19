### How to use the API
* use the url ```<domain-name>/user/<username>/<score>``` to post username and score

* send get request to ```<domain-name>``` to get Leader Board

### Test if API working properly on local server
``` bash
pip install -r requirements.txt
python app.py
```
In a separate terminal
```bash
$ curl -X POST http://127.0.0.1:5000/user/test4/1
{
  "action": "success"
}

$ curl http://127.0.0.1:5000/
{
  "test4": 12
}
```
