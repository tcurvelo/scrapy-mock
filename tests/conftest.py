import os
import re

import pytest
import requests
import scrapy
import vcr


def slugify(request):
    name = request.node.name
    name = re.sub(r"(?:\])", "", name)
    name = re.sub(r"(?:\[|-)", "__", name)
    name = re.sub(r"[:/\.?&=]+", "-", name)
    if request.cls:
        return f"{request.cls}.{name}"
    else:
        return name


@pytest.fixture(scope="session")
def vcr_settings():
    # Avoid HTTP requests in CI environments.
    # (Bitbucket, Gitlab and Travis use `CI=true` as default)
    record_mode = "none" if os.getenv("CI") else "once"

    return vcr.VCR(
        serializer="yaml",
        decode_compressed_response=True,
        cassette_library_dir="tests/fixtures/cassettes",
        record_mode=record_mode,
    )


@pytest.fixture()
def response(request, vcr_settings, url):
    filename = slugify(request)
    session = MockSession()
    with vcr_settings.use_cassette(f"{filename}.yaml"):
        yield session.get(url)


class MockSession(requests.Session):
    def get(self, url, meta=None):
        return self._request("GET", url, meta)

    def _request(self, method, url, meta=None, **kwargs):
        response = super(MockSession, self).request(method, url, **kwargs)
        return scrapy.http.HtmlResponse(
            body=response.content, url=url, request=scrapy.http.Request(url, meta=meta)
        )
