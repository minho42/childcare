import time
from functools import wraps
from typing import List

from random_user_agent.params import OperatingSystem, Popularity, SoftwareName, SoftwareType
from random_user_agent.user_agent import UserAgent

software_names = [
    SoftwareName.CHROME.value,
    SoftwareName.SAFARI.value,
    SoftwareName.EDGE.value,
    SoftwareName.INTERNET_EXPLORER.value,
    SoftwareName.ANDROID.value,
]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.MAC.value]
software_types = [SoftwareType.WEB_BROWSER.value]
popularity = [Popularity.POPULAR.value, Popularity.COMMON.value]
user_agent_rotator = UserAgent(
    software_names=software_names,
    operating_systems=operating_systems,
    software_types=software_types,
    popularity=popularity,
    limit=100,
)


def random_useragent() -> str:
    # https://github.com/Luqman-Ud-Din/random_user_agent
    return user_agent_rotator.get_random_user_agent()


def started_and_finished(func):
    @wraps(func)
    def closure(*args, **kwargs):
        print(f"<{func.__name__}> started")
        result = func(*args, **kwargs)
        print(f"<{func.__name__}> finished")
        return result

    return closure


def timeit(func):
    @wraps(func)
    def closure(*args, **kwargs):
        ts = time.time()
        result = func(*args, **kwargs)
        te = time.time()
        print("<%s> took %0.3fs." % (func.__name__, te - ts))
        return result

    return closure


def get_all_fields_except(model, exclude_list: List[str]) -> List[str]:
    if type(exclude_list) is not list:
        raise TypeError("exclude_list must be list")

    include_list = get_all_fields(model)

    for i in include_list:
        for e in exclude_list:
            e = e.strip()
            if e in include_list:
                include_list.remove(e)

    return include_list


def get_all_fields(model) -> List[str]:
    r = []
    try:
        r = [f.name for f in model._meta.__dict__["local_fields"]]
    except KeyError:
        pass
    else:
        pass
    return r
