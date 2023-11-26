FROM python:3.9

WORKDIR /workspace

RUN apt update \
    && apt install -y curl

RUN curl --proto '=https' --tlsv1.2 -fsSL https://static.pantsbuild.org/setup/get-pants.sh | bash

RUN ln -s ~/bin/pants /bin/pants

WORKDIR /code

COPY bin .

# RUN pants tailor

RUN pip install -r requirements.txt

# RUN pants run :app

# RUN python3 app.py
# 
CMD [""]