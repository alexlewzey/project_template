"""Script that runs the pipeline."""

from src.pipeline.pipeline import run_pipeline

if __name__ == "__main__":
    try:
        run_pipeline()
    except Exception as e:
        raise e
