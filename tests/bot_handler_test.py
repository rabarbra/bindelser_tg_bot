import pytest

from bothandler import BotHandler

EMPTY_TOKEN = 'token-123456'
bot = BotHandler(EMPTY_TOKEN)


@pytest.mark.parametrize("url", ['random/url/one', '', '-45465546'])
def test_url_format(url: str):
    res = BotHandler('token-123').url_format(url)
    assert f'https://api.telegram.org/bot/token-123/{url}' == res


def test_send_message(requests_mock):
    requests_mock.post('https://api.telegram.org/bot/token-123/sendMessage', json={'status': 'ok'})
    res = BotHandler('token-123').send_message('chat-123456', 'unittest message text')
    assert {'status': 'ok'} == res


#  todo need more tests
