import sys
import typer
import unittest
from tests.test_cat_api import TestCatAPI


app = typer.Typer(add_completion=False)


@app.command()
def cat_api_tests():
    failed_test_results = False
    test_suite_cat_api = unittest.TestLoader().loadTestsFromTestCase(TestCatAPI)
    test_result_cat_api = unittest.TextTestRunner(verbosity=2).run(test_suite_cat_api)
    if not test_result_cat_api.wasSuccessful():
        failed_test_results = True
    if failed_test_results:
        sys.exit(1)


@app.command()
def some_other_tests():
    print('They should be added here...')


if __name__ == '__main__':
    app()
