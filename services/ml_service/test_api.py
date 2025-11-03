import os
import time
import argparse
import pandas as pd
import requests
from dotenv import load_dotenv

# ---------- LOAD ENVIRONMENT VARIABLES ---------- #
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

HOST = os.getenv('MAIN_APP_HOST', 'localhost')
PORT = os.getenv('MAIN_APP_VM_PORT', '8080')
API_URL = f"http://{HOST}:{PORT}/predict"
CSV_PATH = os.getenv('CSV_PATH')
SLEEP_SECONDS = float(os.getenv('SLEEP_SECONDS', 0.5))
MAX_REQUESTS = int(os.getenv('MAX_REQUESTS', 100))
TEST_MODE = os.getenv('TEST_MODE', 'limited')

# ---------- PARSE COMMAND-LINE ARGUMENTS ---------- #
parser = argparse.ArgumentParser(description='Load testing for FastAPI service')
parser.add_argument('--mode', type=str, default=TEST_MODE, help='Test mode: limited or stress')
parser.add_argument('--limit', type=int, default=MAX_REQUESTS, help='Max requests in limited mode')
parser.add_argument('--sleep', type=float, default=SLEEP_SECONDS, help='Sleep time between requests in seconds')
args = parser.parse_args()

# ---------- LOAD DATA ---------- #
if not CSV_PATH:
    CSV_PATH = os.path.join(os.path.dirname(__file__), '..', 'test_data', 'test_data.csv')
CSV_PATH = os.path.abspath(CSV_PATH)

if not os.path.exists(CSV_PATH):
    raise FileNotFoundError(f'CSV file not found: {CSV_PATH}')

df = pd.read_csv(CSV_PATH)
print(f'Data loaded: {len(df)} rows from {CSV_PATH}')

# ---------- HELPER FUNCTION ---------- #
def send_request(i, row):
    '''
        Sends one POST request to the FastAPI prediction API using data from a single row.
        Args:
            i (int): Row number (used for apartment_id).
            row (pd.Series): One row from the DataFrame containing model parameters.
    '''
    payload = {
        'apartment_id': f'APT_{i}',
        'model_params': row.to_dict()
    }

    try:
        # Measure request duration
        start_time = time.time()
        response = requests.post(API_URL, json=payload)
        duration = time.time() - start_time

        # Handle the response
        if response.status_code == 200:
            data = response.json()
            print(f"[{i:04d}] Done | price={data['price']:.2f} | request_duration={duration:.3f}s")
        else:
            print(f'[{i:04d}] Failed | response_code={response.status_code} | {response.text[:100]}')

    except requests.exceptions.RequestException as e:
        print(f'[{i:04d}] Request error: {e}')

# ---------- MAIN EXECUTION ---------- #
if __name__ == '__main__':

    if args.mode == 'limited':
        print(f'Running limited test for {args.limit} requests')
        for i, (_, row) in enumerate(df.head(args.limit).iterrows(), 1):
            send_request(i, row) # i as an apartment id of test_data
            time.sleep(args.sleep)
        print('Test finished successfully')

    elif args.mode == 'stress':
        print('Running infinite stress test. Press Ctrl+C to stop')
        i = 1  # start counter
        try:
            while True:
                row = df.sample(n=1).iloc[0]  # randomly select a row
                send_request(i, row) # i as a simle counter return
                i += 1  # increment counter
                time.sleep(args.sleep)
        except KeyboardInterrupt:
            print('Stress test stopped')

    else:
        print('Invalid mode')
