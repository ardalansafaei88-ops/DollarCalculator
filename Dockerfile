FROM python:3.11-slim

ENV XDG_CONFIG_HOME=/tmp/.chromium
ENV XDG_CACHE_HOME=/tmp/.chromium

RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

RUN echo "=== CHROMIUM ===" && \
    which chromium && \
    chromium --version && \
    echo "=== CHROMEDRIVER ===" && \
    which chromedriver && \
    chromedriver --version

RUN python -c "import urllib.request; print('TGJU STATUS:', urllib.request.urlopen('https://www.tgju.org/profile/price_aed', timeout=20).status)"

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN echo "=== /app CONTENTS ===" && ls -la /app && \
    echo "=== TGJU FILES (case-insensitive search) ===" && find /app -iname "tgju*" && \
    echo "=== TRY IMPORT ===" && python -c "import sys; print(sys.path); import TGJU; print('OK:', TGJU.__file__)"

CMD ["python", "web.py"]