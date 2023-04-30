from decorators import fixture

# top level fixture
async def fixture_client():
    yield {"url": "http://localhost"}

def data_factory(param):

    async def data_1():
        yield {"1": param}

    async def data_2():
        yield {"2": param}

    return data_1, data_2

# assigned fixtures
fixture_data_1, fixture_data_2 = data_factory("data")

fixture_more_data_1, fixture_more_data_2 = data_factory("more_data")