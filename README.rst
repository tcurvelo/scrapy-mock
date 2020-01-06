scrapy-mock
===========
A Pytest plugin to record Scrapy responses and use them as testing fixtures.
The motivation here is to decrease the friction to write unit tests for Scrapy spiders.

Install
-------
::

    pip install scrapy-mock

Usage
-----
::

    @pytest.mark.parametrize(
        ["url", "expected"],
        ("http://foobar.com/item/1",  {"name": "item1", "url": "/item/1"}),
    ])
    def test_parse(spider, response, expected):
        result = next(spider.parse(response))
        assert result == expected
