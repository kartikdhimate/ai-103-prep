import time

import openai


def call_with_retry(fn, attempts=5):
    for i in range(attempts):
        try:
            return fn()
        except openai.RateLimitError:
            time.sleep(2 ** i)
    raise RuntimeError("Still throttled after retries")
