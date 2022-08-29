# Pytest sample project

## How to use the project

- Fill `tr_config.cfg` with your TestRail instance details
- Execute the commands on the script below

```sh
# Install test project
pip install -r requirements.txt

# Add your testrail username and password as environment variables
export TESTRAIL_USER=<Testrail username>
export TESTRAIL_KEY=<Testrail API key or Password>

# Run tests (Without uploading results)
pytest --junitxml "junit-report.xml" "./tests"

# Run tests and Upload test results
pytest ./tests --testrail --tr-email=$TESTRAIL_USER --tr-password=$TESTRAIL_KEY --tr-config=tr_config.cfg
```

- Information on the library and command line parameters can be found [here](https://github.com/allankp/pytest-testrail#usage).
- First you need to create testcases in Testrail create a Test Plan/ Test Run including those test cases
- Retrieve the project_id, suit_id, run_id etc. by changing the ```main.py``` and executing it.
    ```commandline
  python main.py
  ```
- You just need to update the ```tr_config.cfg``` and decorate the test methods in ```tests/test_sum.py``` and ```tests/test_subtraction.py``` with the case IDs.

Example: 
```python
@case("C63") #See the lib/utils.py to see case method built using pytest_testrail.plugin to avoid longer decorator names
def test_sum_two_numbers():
    assert 1 + 1 == 2
```