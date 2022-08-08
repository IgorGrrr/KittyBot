import logging

# Здесь задана глобальная конфигурация для логирования
logging.basicConfig(
    level=logging.DEBUG,
    filename='main.log',
    filemode='w'
)

logging.debug('123')
logging.info('Сообщение отправлено')
logging.warning('Большая нагрузка!')
logging.error('Бот не смог отправить сообщение')
logging.critical('Всё упало! Зовите админа!1!111')  