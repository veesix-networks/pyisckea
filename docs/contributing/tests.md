<a href="https://docs.pytest.org/en/stable/" target="_blank">pytest</a> is the testing framework of choice in this project. If you are not very familiar with the basics of pytest, I would recommend reading the documentation or having a look at the tests in this project to see the structure and provided functionality.

Each API endpoint or class/function that interacts with a resource which changes potential production data must implement a test and pass before a merge request is accepted.

## Test Structure

All tests belong in the tests directory of the project. The structure of this folder may change from time to time but the basis is that for every API endpoint, you try to group them cleanly into their respective files according to the API endpoint path, prefixed with test_. Here are some examples:


TO DO.