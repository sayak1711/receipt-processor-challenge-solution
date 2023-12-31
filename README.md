# receipt-processor-challenge-solution


## Step1: Commands to run this application using Docker:

`docker build -t fetch-receipts-app .`

`docker run -d -p 8000:8000 fetch-receipts-app`


## Step2: Use the application endpoints (just as it is mentioned in the question):

`POST http://localhost:8000/receipts/process`

`GET http://localhost:8000/{id}/points`

---
## Summary of API Specification

### Endpoint: Process Receipts

* Path: `/receipts/process`
* Method: `POST`
* Payload: Receipt JSON
* Response: JSON containing an id for the receipt.

Description:

Takes in a JSON receipt (see example in the example directory) and returns a JSON object with an ID generated by code.

The ID returned is the ID that should be passed into `/receipts/{id}/points` to get the number of points the receipt
was awarded.


## Endpoint: Get Points

* Path: `/receipts/{id}/points`
* Method: `GET`
* Response: A JSON object containing the number of points awarded.

A simple Getter endpoint that looks up the receipt by the ID and returns an object specifying the points awarded.