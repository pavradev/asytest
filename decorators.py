
import inspect


_fixture_attr = "_is_atest_fixture"

def validate_is_async_generator(func):
    if not inspect.isasyncgenfunction(func):
        raise ValueError(f"Fixture function {func.__name__} is not async generator")

def fixture(func):
    validate_is_async_generator(func)
    setattr(func, _fixture_attr, True)
    return func

def is_fixture(func):
    return hasattr(func, _fixture_attr)