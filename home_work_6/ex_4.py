# Задание 4
# Жду от вас письмо! (слайды 15-19). Воспользуйтесь менеджером контекста (with … as) (слайд 20)
# (Не забудьте для себя понять код из официальной документации – слайд 18)
import smtplib

#help(smtplib)
with smtplib.SMTP('smtp.gmail.com', 587) as smtpObj:
    smtpObj.starttls()
    smtpObj.login('vitalii.tolkachov@gmail.com','******')
    smtpObj.sendmail("vitalii.tolkachov@gmail.com",["el.piankova@gmail.com", "auto.qa.lessons@gmail.com"],"I didi it!!")




