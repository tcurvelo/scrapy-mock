import pytest

from spiders.quotes import QuotesSpider


@pytest.fixture()
def spider():
    return QuotesSpider()


@pytest.mark.parametrize(
    ["url", "expected"],
    [
        (
            "http://quotes.toscrape.com/",
            {
                "text": "The world as we have created it is a process of our "
                "thinking. It cannot be changed without changing our thinking.",
                "author": "Albert Einstein",
            },
        )
    ],
)
def test_parse(spider, response, expected):
    result = next(spider.parse(response))
    assert result == expected
