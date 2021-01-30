import save_load
from flask_app import bot


class Graph:
    def paint(self, *args):
        raise NotImplemented()

    def paint_symp(self, *args):
        raise NotImplemented()


graph_painting = Graph()


def add_at(params: dict):
    for l in range(len(params)):
        if params[l][0] != '@':
            params[l] = '@' + params[l]


def handle(message: dict, relations: dict):  # todo message and relations args replace by dataclasses
    chat_id = message['chat']['id']
    username = '@' + message['from']['username']

    try:
        text = message['text']
    except KeyError:
        return

    if "text" not in message:
        bot.send_message(chat_id, 'Я понимаю только текстовые сообщения.')

    else:
        text = message["text"]
        msg_list = text.split()
        option = msg_list[0].lower()

        if option[0] != '/':
            option = '/' + option

        params = msg_list[1:]
        sender = '@' + username

        if option in ['/start', '/info']:
            bot.send_message(chat_id, 'Здесь будет инфо о боте.')

        elif option == '/add_conn':
            if params:
                add_at(params)
                params = set(params)
                params.difference_update(relations[username]['mut_conn'])
                relations[username]['conn'].update(params)

        # Проверить на взаимность и отправить сообщение с подтверждениями
        elif option == '/add_symp':
            if params:
                add_at(params)
                params = set(params)
                params.difference_update(relations[username]['vis_symp'])
                relations[username]['symp'].update(set(params))

        elif option == '/conn':
            matr = save_load.load('test')
            dict_conn = matr.conn(sender)
            bot.sendMessage(chat_id, 'Неподтверждённые связи: ' + ', '.join(dict_conn['conn']) + '\n\nПодтверждённые связи: ' + ', '.join(dict_conn['mut_conn']))

        elif option == '/symp':
            matr = save_load.load('test')
            dict_conn = matr.conn(sender)
            bot.sendMessage(chat_id, 'Невидимые симпатии: ' + ', '.join(dict_conn['symp']) + '\n\nВидимые симпатии: ' + ', '.join(dict_conn['vis_symp']) + '\n\nВзаимные симпатии: ' + ', '.join(
                dict_conn['mut_symp']))

        elif option == '/show_symp':
            add_at(params)
            matr = save_load.load('test')
            matr.show_symp(sender, params)
            graph_painting.paint_symp(matr, 'graph.png')
            save_load.save('test', matr)

        elif option == '/del_conn':
            add_at(params)
            matr = save_load.load('test')
            matr.del_conn(sender, params)
            graph_painting.paint(matr, 'graph.png')
            save_load.save('test', matr)

        elif option == '/del_symp':
            add_at(params)
            matr = save_load.load('test')
            matr.del_conn(sender, params)
            graph_painting.paint_symp(matr, 'graph.png')
            save_load.save('test', matr)

        elif option == '/graph':
            if not params:
                photo = open('graph.png', 'rb')
                bot.sendPhoto(chat_id, photo)
                photo.close()

            else:
                how = params[0]
                matr = save_load.load('test')
                graph_painting.paint(matr, 'graph_{}.png'.format(how), how)
                photo = open('graph_{}.png'.format(how), 'rb')
                bot.sendPhoto(chat_id, photo)
                photo.close()

        elif option == '/matr':
            matr = save_load.load('test')
            m = ''
            m = m + str(matr.ind) + '\n\n'
            for st in matr.matr:
                m = m + str(st) + '\n'
            bot.sendMessage(chat_id, m)

        else:
            bot.sendMessage(chat_id, 'Я такого не понимаю.')
