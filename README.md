# scrapy-mock

A pytest plugin to record Scrapy responses and use them as testing fixtures.
The motivation here is to decrease the friction to write unit tests to Scrapy spiders.

## Usage

```python
@pytest.mark.parametrize(
    ["url", "expected"],
    ("http://foobar.com/item/1",  {"name": "item1", "url": "/item/1"}),
])
def test_parse(spider, response, expected):
    result = next(spider.parse(response))
    assert result == expected
```

## TODO

- v0.1 (MVP)
  - ~~Returns a `scrapy.Response` given a testing URL~~
  - ~~Don't request on CIs by default~~
  - Record the responses as human readable files (including its names)
  - Configure it as a proper pytest plugin
  - Release it as a library
