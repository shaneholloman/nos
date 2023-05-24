import pytest

from nos.executors.ray import RayExecutor
from nos.server.service import InferenceServiceImpl
from nos.test.conftest import ray_executor  # noqa: F401


pytestmark = pytest.mark.e2e


def test_inference_service_impl(ray_executor: RayExecutor):  # noqa: F811
    service = InferenceServiceImpl()
    assert service is not None
