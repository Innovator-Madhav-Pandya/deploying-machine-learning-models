def test_make_single_prediction():
    # Given
    test_data = load_dataset(file_name='test.csv')
    single_test_json = test_data[0:1].to_json(orient='records')
    single_test_json = test_data[0:1]

    # When
    subject = make_prediction(input_data=single_test_json)
@@ -22,7 +22,7 @@ def test_make_multiple_predictions():
    # Given
    test_data = load_dataset(file_name='test.csv')
    original_data_length = len(test_data)
    multiple_test_json = test_data.to_json(orient='records')
    multiple_test_json = test_data

    # When
    subject = make_prediction(input_data=multiple_test_json)
