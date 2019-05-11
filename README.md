# PythonAPI
Python API with Flask for token system

# Token Registry Service

## Usage

All responses will have the form

```json
{
    "data": "Mixed type holding the content of the response",
    "message": "Description of what happened"
}
```

Subsequent response definitions will only detail the expected value of the `data field`

### List all tokens

**Definition**

`GET /tokens`

**Response**

- `200 OK` on success

```json
[
    {
        "identifier": "token_1",
        "name": "Jonesh Shrestha",
    },
    {
        "identifier": "token_2",
        "name": "Aditya Thebe",
    }
]
```

### Registering a token

**Definition**

`POST /tokens`

**Arguments**

- `"identifier":string` a globally unique identifier for this token
- `"name":string` name of the token owner

If a token with the given identifier already exists, the existing token will be overwritten.

**Response**

- `201 Created` on success

```json
{
    "identifier": "token_1",
    "name": "Jonesh Shrestha",
}
```

## Lookup token details

`GET /token/<identifier>`

**Response**

- `404 Not Found` if the token does not exist
- `200 OK` on success

```json
{
    "identifier": "token_1",
    "name": "Jonesh Shrestha",
}
```

## Delete a token

**Definition**

`DELETE /token/<identifier>`

**Response**

- `404 Not Found` if the token does not exist
- `204 No Content` on success
