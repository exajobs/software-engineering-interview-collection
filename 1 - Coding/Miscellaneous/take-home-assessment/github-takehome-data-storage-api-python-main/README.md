# Coding Exercise: Data Storage API

Implement a small HTTP service to store objects organized by repository.
Clients of this service must implement the API below.


We value your time, and ask that you spend no more than **2 hours** on this exercise.

## General Requirements

* The service should identify objects by their content. This means that two objects with the same content should be considered identical, and only one such object should be stored per repository.
* Two objects with the same content that are in separate repositories should be stored separately.
* The included tests should pass and should not be modified.
* Do not move or rename any of the existing files.
* The service must implement the API as described below.
* The data can be persisted in memory, on disk, or wherever you like.
* Prefer using the standard library over external dependencies. If you must include an external dependency, please explain your choice in the pull request.

## Recommendations

* Your code will be read by humans, please take the time to optimize for that.
* Add extra tests to test the functionality of your implementation.
* The description of your submission should be used to describe your reasoning, your assumptions and the tradeoffs in your implementation.
* If your chosen language allows for concurrency, remember that this is a web application and concurrent requests will come in.
* Focus on getting a working solution and avoid external dependencies for data storage.

## API

### Upload an Object

```
PUT /data/{repository}
```

#### Response

```
Status: 201 Created
{
  "oid": "2845f5a412dbdfacf95193f296dd0f5b2a16920da5a7ffa4c5832f223b03de96",
  "size": 1234
}
```

### Download an Object

```
GET /data/{repository}/{objectID}
```

#### Response

```
Status: 200 OK
{object data}
```

Objects that are not on the server will return a `404 Not Found`.

### Delete an Object

```
DELETE /data/{repository}/{objectID}
```

#### Response

```
Status: 200 OK
```

## Getting started and Testing

This exercise requires a python 3.9. Get started by installing dependencies:

```sh
pip install -r requirements.txt
```

Write your server implementation in `server.py`. Then run the tests:

```sh
python -m unittest server_test.py
```

## Submitting Your Work
When you are finished:
  - Commit all of your code.
  - Push your changes to GitHub.
  - Open a [pull request](https://help.github.com/articles/creating-a-pull-request/).
  - Visit https://interviews.githubapp.com/ and click `Done`.
  - Thank you! 🎉
