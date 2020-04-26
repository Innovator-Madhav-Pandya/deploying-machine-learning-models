 import json
import math

from api import __version__ as api_version


def test_health_endpoint_returns_200(flask_test_client):
    # When
@@ -14,6 +16,17 @@ def test_health_endpoint_returns_200(flask_test_client):
    assert response.status_code == 200


def test_version_endpoint_returns_version(flask_test_client):
    # When
    response = flask_test_client.get('/version')

    # Then
    assert response.status_code == 200
    response_json = json.loads(response.data)
    assert response_json['model_version'] == _version
    assert response_json['api_version'] == api_version


def test_prediction_endpoint_returns_prediction(flask_test_client):
    # Given
    # Load the test data from the regression_model package
  
    # When
    response = flask_test_client.post('/v1/predict/regression',
                                      json=post_json)
                                      json=json.loads(post_json))

    # Then
    assert response.status_code == 200
    response_json = json.loads(response.data)
    prediction = response_json['predictions']
    response_version = response_json['version']
    assert math.ceil(prediction) == 112476
    assert math.ceil(prediction[0]) == 112476
    assert response_version == _version
