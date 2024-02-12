# FastAPI
# API Description
This API is built using FastAPI and provides two endpoints:

1. POST/date

This endpoint retrieves the current date and time in two different formats based on a boolean parameter.

- Request Type: POST
- Parameters: date_with_minutes (boolean): Set to true to get the date and time in "yyyy-mm-dd hh:ii:ss" format, or false to get the date in "yyyy-dd-mm" format.
- Response:
- 200 OK: Returns the current date and time in the specified format.
- 400 Bad Request: If the request is invalid.

Example Usage:
- Request:
    {
  "format_date": true
}
- Response:
    {
  "fecha": "2024-02-12 15:30:00"
}
2. GET/count
  
This endpoint retrieves the count of how many times any of the two endpoints have been called.

- Request Type: GET
- Response:
    200 OK: Returns the count of API calls.
    400 Bad Request: If the request is invalid.
