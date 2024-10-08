import inspect
def introspection_info(obj):
    all_attrs = dir(obj)
    methods = [attr for attr in all_attrs if callable(getattr(obj, attr)) and not attr.startswith("__")]
    attributes = [attr for attr in all_attrs if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    modul = inspect.getmodule(introspection_info)
    return {'type':type(obj),'attributes':attributes,'methods':methods,'modul': modul}



number_info = introspection_info(53)
print(number_info)
