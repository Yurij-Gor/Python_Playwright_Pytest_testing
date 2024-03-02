FROM mcr.microsoft.com/playwright:v1.17.0-focal

WORKDIR /tests_project/

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN playwright install

ENV ENV=prod

CMD ["python", "-m", "pytest", "-s", "--alluredir=test_results/", "tests/"]
