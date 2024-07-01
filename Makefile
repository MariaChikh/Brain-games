install:
	poetry install

brain-games:
	@poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --force-reinstall --user dist/*whl

lint:
	poetry run flake8 brain_games

brain-even:
	poetry run brain-even



