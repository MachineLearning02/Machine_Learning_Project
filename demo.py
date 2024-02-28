from housing.pipeline.pipeline import pipeline
from housing.excepton import HousingException
from housing.logger import logging

def main():
    try:
        pipeline = pipeline()
        pipeline.run_pipeline()
    except Exception as e:
        logging.info(f"{e}")
        print(e)


if __name__=="__main__":
    main()   