def make_prediction(*, input_data) -> dict:
    """Make a prediction using the saved model pipeline."""

    data = pd.read_json(input_data)
    data = pd.DataFrame(input_data)
    validated_data = validate_inputs(input_data=data)
    prediction = _price_pipe.predict(validated_data[config.FEATURES])
    output = np.exp(prediction)
