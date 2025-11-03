# /services/ml_service/query_check.py

# ---------- PARAMETERS VALIDATION ---------- #
class QueryValidator:
    '''
        Validates API request parameters.
    '''

    def __init__(self, required_model_params: list):
        self.required_model_params = required_model_params
        self.param_types = {
            'apartment_id': str,
            'model_params': dict
        }

    def check_required_query_params(self, query_params: dict) -> bool:
        if 'apartment_id' not in query_params or 'model_params' not in query_params:
            return False
        if not isinstance(query_params['apartment_id'], self.param_types['apartment_id']):
            return False
        if not isinstance(query_params['model_params'], self.param_types['model_params']):
            return False
        return True

    def check_required_model_params(self, model_params: dict) -> bool:
        return set(self.required_model_params).issubset(model_params.keys())

    def validate(self, params: dict) -> bool:
        if not self.check_required_query_params(params):
            print("Missing or invalid 'apartment_id' or 'model_params'")
            return False
        if not self.check_required_model_params(params['model_params']):
            print("Missing required model parameters")
            return False
        return True