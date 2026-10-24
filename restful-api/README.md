# RESTful API

This project covers how systems talk to each other over the web using
RESTful APIs: HTTP basics, consuming APIs with the command line and Python,
building APIs with `http.server` and Flask, securing them, and documenting
them with OpenAPI.

## Requirements
* Python 3.9
* `requests` library (`pip install requests` or `sudo apt install python3-requests`)

## How REST communication works
1. The client sends an HTTP/HTTPS request.
2. The web server routes it to the API server.
3. The API server runs the logic and reads or changes the database.
4. The response travels back to the client.

---

## 0. Basics of HTTP/HTTPS

### HTTP vs HTTPS
| | HTTP | HTTPS |
|---|---|---|
| Security | Data is sent as plain text, so anyone on the network can read or change it | Data is encrypted with SSL/TLS, so eavesdroppers can't read or tamper with it |
| Default port | 80 | 443 |
| Identity | No proof of who the server is | A certificate proves the server is who it claims to be |
| Use | Simple, non-sensitive pages | Logins, payments, email, and any personal data |

### Structure of an HTTP request

### Structure of an HTTP response

### Common HTTP methods
| Method | Description | Use case |
|---|---|---|
| GET | Retrieves data without changing it | Fetching a web page or a list of posts |
| POST | Sends data to create a new resource | Submitting a sign-up form |
| PUT | Replaces an existing resource | Updating a whole user profile |
| PATCH | Partially updates a resource | Changing only a user's email |
| DELETE | Removes a resource | Deleting a comment |

### Common HTTP status codes
| Code | Description | Scenario |
|---|---|---|
| 200 OK | The request succeeded | A page or API data loads normally |
| 201 Created | A new resource was created | After a POST that creates a user |
| 301 Moved Permanently | The resource has a new URL | A site moved from http:// to https:// |
| 400 Bad Request | The request is invalid | Sending malformed JSON to an API |
| 401 Unauthorized | Authentication missing or failed | Calling an API without a valid token |
| 403 Forbidden | Authenticated but not allowed | A normal user opening an admin page |
| 404 Not Found | The resource doesn't exist | Visiting a mistyped URL |
| 500 Internal Server Error | The server failed | A bug in the server code |

Groups: `1xx` informational, `2xx` success, `3xx` redirection,
`4xx` client errors, `5xx` server errors.

---

## 2. Consuming and processing data from an API using Python

**File:** `task_02_requests.py`

| Function | What it does |
|---|---|
| `fetch_and_print_posts()` | Fetches all posts from JSONPlaceholder, prints `Status Code: <code>`, then prints each post's title |
| `fetch_and_save_posts()` | Fetches all posts and saves their `id`, `title` and `body` to `posts.csv` |

### Usage

### Key ideas
* `requests.get(url)` returns a response with `.status_code` and `.json()`.
* `.json()` turns the JSON text into Python lists and dictionaries.
* `csv.DictWriter` writes dictionaries as CSV rows, with `writeheader()`
  adding the column names.

## Author
Shada
