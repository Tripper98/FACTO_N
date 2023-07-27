init:
	pip install -r requirements.txt

test:
	nosetests tests

LL=flake8
LL_ARGS=--max-line-length=100 --ignore=E501,E371,W503,E241,E203 --show-source --statistics

lint:
	@
	git ls-tree --full-tree -r --name-only HEAD \
	| grep ".py$$" \
	| xargs $(LL) $(LL_ARGS)

## Formatting
LL=black
FMT_ARGS=-l 100 -S

fmt:
	@
	git ls-tree --full-tree -r --name-only HEAD \
	| grep ".py$$" \
	| xargs $(FMT) $(FMT_ARGS)