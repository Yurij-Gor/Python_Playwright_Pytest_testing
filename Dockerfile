FROM mcr.microsoft.com/playwright:v1.17.0-focal

WORKDIR /tests_project/

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN playwright install

# Установка Allure CLI
RUN apt-get update && \
    apt-get install -y wget && \
    wget https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.27.0/allure-commandline-2.27.0.tgz -O allure-commandline.tgz && \
    tar -zxvf allure-commandline.tgz -C /opt/ && \
    ln -s /opt/allure-2.27.0/bin/allure /usr/bin/allure && \
    rm -f allure-commandline.tgz

ENV ENV=prod

CMD ["python", "-m", "pytest", "-s", "--alluredir=test_results/", "tests/"]
