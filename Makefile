migrate:
	flask db migrate; \

test:
	. .env.test; \
	python -m pytest -s; \

run:
	. .env.development; \
	flask run
