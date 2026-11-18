run:
	python3 elevator.py

test:
	mkdir -p actual_output
	@failed=0; \
	for test_in in tests/*.in; do \
		test_name=$$(basename "$$test_in" .in); \
		expected_out="tests/$${test_name}.out"; \
		actual_out="actual_output/$${test_name}.out"; \
		python3 elevator.py < "$$test_in" > "$$actual_out"; \
		if ! diff -u "$$actual_out" "$$expected_out"; then \
			echo "Test failed: $$test_name"; \
			failed=1; \
		else \
			echo "Test passed: $$test_name"; \
		fi; \
	done; \
	exit $$failed
