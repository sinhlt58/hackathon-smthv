# hackathon-smthv

### create env
`virtualenv .env`
### active env
`source .env/bin/activate`
### install packages
`pip install -r requirements.txt`
### dowload data (if you want)
`python -m textblob.download_corpora`
### run server
`gunicorn --worker-class eventlet -w 1 run:app --bind 0.0.0.0:5000 --reload`
