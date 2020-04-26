
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
