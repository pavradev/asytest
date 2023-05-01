from src.atest import run_tests

def test_asytest_runs_succesfully():
    test_results = run_tests("example_tests")
    assert len(test_results) == 5