@@ -3,6 +3,7 @@
from regression_model import __version__ as _version

from api.config import get_logger
from api.validation import validate_inputs
from api import __version__ as api_version

_logger = get_logger(logger_name=__name__)
@@ -28,14 +29,22 @@ def version():
@prediction_app.route('/v1/predict/regression', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Step 1: Extract POST data from request body as JSON
        json_data = request.get_json()
        _logger.info(f'Inputs: {json_data}')
        _logger.debug(f'Inputs: {json_data}')

        result = make_prediction(input_data=json_data)
        _logger.info(f'Outputs: {result}')
        # Step 2: Validate the input using marshmallow schema
        input_data, errors = validate_inputs(input_data=json_data)

        predictions = result.get('predictions')[0]
        # Step 3: Model prediction
        result = make_prediction(input_data=input_data)
        _logger.debug(f'Outputs: {result}')

        # Step 4: Convert numpy ndarray to list
        predictions = result.get('predictions').tolist()
        version = result.get('version')

        # Step 5: Return the response as JSON
        return jsonify({'predictions': predictions,
                        'version': version})
                        'version': version,
                        'errors': errors})
