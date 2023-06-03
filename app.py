import logging
from logging.config import dictConfig
from fastapi import FastAPI
from data_models import SamplePostRequest
import time
from typing import List
from binary_search import search
from hello import sum_xy

LOG_LEVEL: str = "DEBUG"
FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

app = FastAPI()

log_format = "[%(name)s][%(levelname)-6s] %(message)s"
logging.basicConfig(format=log_format)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')



@app.get('/')
def home():
    return 'hellooo'


@app.get('/health')
def healh_check():
    return 'ok'


@app.post("/predict")
def predict(request: SamplePostRequest):
    return [request.a + request.c[0]]
    
@app.get("/predict")
def predict():
    return "From predict function get"


@app.post("/search")
def search_endpoint(nums: List[int], target: int):
    logger.info("Recieved request.")

    start_time = time.time()
    output = str(search(nums, target))
    end_time = time.time()
    total_time = end_time - start_time

    logger.info(f"The processing took {total_time}s")
    
    logger.debug(f"Debug: Recieved {nums=}, {target=}")
    return output


@app.get("/sum/{c}")
def sum_xy_endpoint(c:str, a: int, b: int):
    logger.info("Recieved request.")

    try:
        unknown_function(c)
    except Exception:
        logger.error("Can't find `unknown_function`")

    start_time = time.time()
    output = c + " " + str(sum_xy(a, b))
    end_time = time.time()
    total_time = end_time - start_time

    logger.info(f"The processing took {total_time}s")
    
    logger.debug(f"Debug: Recieved {c=}, {a=}, {b=}")
    return output
