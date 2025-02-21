## Run code formatting check with Black
run-black:
	@echo ">>> Running Black..."
	poetry run black gdpr_obfuscator test

## Run test coverage check, omitting unnecessary files
check-coverage:
	@echo ">>> Running test coverage..."
	poetry run coverage run -m pytest --testdox && poetry run coverage report -m

## Run all checks
run-checks: run-black check-coverage