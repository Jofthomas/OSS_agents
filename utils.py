
def get_args_kwargs(*args, **kwargs):
  return args, kwargs


def decompose_function_call(function_call: str):
    function_name = function_call.split('(')[0]
    args, kwargs = eval("get_args_kwargs("+function_call.split('(')[1])
    return function_name, args, kwargs


def extract_function_call_raven(call: str):
    """Extracts function name and arguments from a text function call"""
    function_name, _, function_kwargs = decompose_function_call(call)
    return function_name, function_kwargs