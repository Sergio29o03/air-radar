# Air Radar FastAPI Application

Air Radar is a FastAPI application for monitoring and reporting air quality.


### Prerequisites
In order to run this container you'll need docker and docker compose installed.

## Usage

### Development

List the different parameters available to your container

```shell
docker-compose up
```

## Tasks

Here is a list of updated tasks for further development:

### API Development

**Datetime Range Measurement Endpoint**: Enhance the endpoint to accept a start datetime and an end datetime as parameters and return measurements within this datetime range. The response should be formatted as JSON.
- [ ] Define the endpoint route and parameters to include time (e.g., `/measurements?start_datetime=YYYY-MM-DDTHH:MM:SS&end_datetime=YYYY-MM-DDTHH:MM:SS`).
- [ ] Adjust the logic to fetch measurements from the database based on the provided datetime range.
- [ ] Format the fetched data as JSON and return it as a response, ensuring the datetime format is correctly handled.

### IoT Integration

**ESP32 Connection Setup**: Implement functionality on the ESP32 to connect to the API and send air quality measurements, including precise timestamps.
  - [ ] Modify ESP32 firmware to collect air quality measurements with accurate timestamps.
  - [ ] Implement HTTP requests from the ESP32 to the FastAPI endpoint for posting new measurements, including the datetime of each measurement.
  - [ ] Ensure securty on the data transmition

### General Tasks

- [ ] **Unit Tests**: Write comprehensive unit tests for the datetime range endpoint and ESP32 integration functionality, focusing on datetime handling.
- [ ] **Documentation**: Update the API documentation to clearly explain the datetime range parameters and ESP32 setup guide to reflect new features and endpoints, including how to format datetimes for requests.

