import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')



website_name = 'https://dvmn.org/referrals/m7ojXRXvZKy0e5rH3AMFzVjPOCDkwKStCFEzKLiy/'
friend_name  = 'Леха'
sender_name =  'Илья'
email_recipient = login
email_sender = 'hitomi.jpeg@gmail.com'
title_letter = 'Го го го го заниматься на сайте dvmn.org'

letter = '''From: {email_r} 
To: {email_s}
Subject: {title_l}
Content-Type: text/plain; charset="UTF-8";
'''.format(email_r = email_recipient, email_s = email_sender, title_l = title_letter )

template_letter = '''Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.'''



template_letter= template_letter.replace('%website%', website_name)
template_letter = template_letter.replace('%friend_name%', friend_name)
template_letter = template_letter.replace('%my_name%', sender_name)
full_letter = letter + template_letter

full_letter = full_letter.encode("UTF-8")


server = smtplib.SMTP_SSL('smtp.mail.ru:465')
server.login(login,password)
server.sendmail(login, 'hitomi.jpeg@gmail.com', full_letter)
server.quit()