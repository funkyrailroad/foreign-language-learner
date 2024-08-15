import requests
import argparse
from pprint import pprint


parser = argparse.ArgumentParser()
parser.add_argument(
    "--fp", help="path to audio file", default="./mysite/fll/Voice 182.wav"
)
parser.add_argument(
    "--base_url", help="url to send request", default="http://localhost:8000"
)
args = parser.parse_args()


endpoint = f"{args.base_url}/fll/transcribe/"
files = {"audio": open(args.fp, "rb")}

r = requests.post(endpoint, files=files)

assert r.status_code == 200

pprint(r.json())
