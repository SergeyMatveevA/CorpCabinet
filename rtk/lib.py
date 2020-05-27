import os
import smtplib

from datetime import datetime as dt
from email.mime.text import MIMEText
from pydub import AudioSegment

from arrangement.consts import AUDIO_SHARES
from nipo_db.models import Samplertk06B
from rtk.consts import AUDIO_UPLOAD_RTK
from rtk.models import Complaint

S_NAME = 'anonymous'


def complaint_translate():
    """
    Записать в базу тикеты по жалобам клиентов и сообщить менеджменту
    """
    # Северо-Западный регион
    region_range = list(range(100, 500))
    # Сибирь
    region_range.extend(list(range(501, 999)))

    check_date = dt(dt.now().year, dt.now().month, dt.now().day, 0, 0, 0)
    successful_interviews = Samplertk06B.objects.filter(
        q_neg_res1='1', responsecode=18, city_quota__in=region_range, contacttime__gt=check_date
    )
    for interview in successful_interviews:
        if len(Complaint.objects.filter(survey_name=S_NAME, interview_number=interview.interviewnumber)) == 0:
            create_ticket(interview)


def create_ticket(interview):
    """
    Создать тикет для менеджмента
    :param interview: интервью респа
    :type interview: nipo_db.models.Samplertk06B
    """
    trans_reason = ''
    if interview.q_nps in ('0', '1', '2', '3', '4', '5', '6'):
        trans_reason = 'small_mark_nps'
    elif interview.q_csi in ('1', '2', '3'):
        trans_reason = 'small_mark_cc'
    elif interview.q_res in ('2', '3'):
        trans_reason = 'unresolved_question'
    elif interview.q_neg_res_1 == '1':
        trans_reason = 'region_moving'
    elif interview.q_neg_res_2 == '1':
        trans_reason = 'ready_to_desertion'

    appointment_time = None
    if int(interview.q_neg_res2_yyyy) > 0:
        appointment_time = dt(
            int(interview.q_neg_res2_yyyy), int(interview.q_neg_res2_mm), int(interview.q_neg_res2_dd),
            int(interview.q_neg_res2_hh), int(interview.q_neg_res2_min), 0
        )
    negative_reason_cc = interview.q_csi_oe
    if not interview.q_csi_oe:
        negative_reason_cc = ' '
    negative_reason_rtk = interview.q_nps_oe
    if not interview.q_nps_oe:
        negative_reason_rtk = ' '

    new_ticket = Complaint(
        telephone=interview.telephonenumber, abonent_id=interview.id_abonent, translate_reason=trans_reason,
        appointment_time=appointment_time, appointment_comment=interview.q_neg_res2_com,
        ready_recommend=int(interview.q_nps), negative_reason_rtk=negative_reason_rtk, cc_satisfaction=interview.q_csi,
        negative_reason_cc=negative_reason_cc, creation_date=dt.now(), survey_name=S_NAME,
        interview_number=interview.interviewnumber, region=str(int(interview.city_quota) // 100),
        touch_point=interview.touchpoint, city_quota=interview.city_quota, region_name=interview.region
    )
    new_ticket.save()


def send_mail(recipients, tt_id, reg_name):
    """
    Отправить уведомление сотрудникам о новом трабл-тикете
    :param recipient: почта нужного филиала
    :param tt_id: id заявки
    """
    sender = 'anonymous@anonymous.ru'
    server = 'anonymous.ru:2525'
    letter_text = '<br>Коллеги,<br>'
    letter_text += '<br>Создан новый траблтикет № {id}, подробная информация по ссылке: ' \
                   r'http://anonymous.ru/{id}/change/'.format(id=tt_id)
    msg = MIMEText(letter_text.encode('utf-8'), _charset='utf-8', _subtype='html')
    msg['Subject'] = 'Заявка о проблеме {id} {region_name}'.format(id=tt_id, region_name=reg_name)
    msg['From'] = sender
    msg['To'] = ','.join(recipients)

    s = smtplib.SMTP(server)
    s.login('anonymous@anonymous.ru', 'anonymous')
    s.sendmail(sender, recipients, msg.as_string())
    s.quit()


def audio_upload():
    """
    Подгрузить записи к уже сформированным ТТ
    """
    for ticket in Complaint.objects.filter(state_compl='preparing'):
        if upload_audio(ticket):
            rtk_employees = {
                7: ['anonymous@anonymous.ru'], 3: ['anonymous@anonymous.ru'],
                4: ['anonymous@anonymous.ru', 'anonymous@anonymous.ru'],
                2: ['anonymous@anonymous.ru', 'anonymous@anonymous.ru'],
                5: ['anonymous@anonymous.ru', 'anonymous@anonymous.ru'],
            }
            recipients = ['anonymous@anonymous.ru', 'anonymous@anonymous.ru'],
            if int(ticket.city_quota) > 199:
                recipients.extend(rtk_employees[int(ticket.city_quota) // 100])
            elif int(ticket.city_quota) == 101:
                recipients.extend(['anonymous@anonymous.ru', 'anonymous@anonymous.ru'])
            elif int(ticket.city_quota) in (102, 103, 104):
                recipients.append('anonymous@anonymous.ru')

            send_mail(recipients, ticket.pk, ticket.region_name)


def upload_audio(ticket):
    """
    Загрузить записи на ребус
    :type ticket: Complaint
    """
    fragments = []
    responses = []
    audio_source = os.path.join(AUDIO_SHARES['NEW'], S_NAME)
    for root, dirs, files in os.walk(audio_source):
        for file in files:
            if file[0] == 'w':
                audio_id = int(file.split('_')[1])
                responses.append(int(file.split('_')[2]))
                inter = file.split('_')[4]
            else:
                audio_id = int(file.split('_')[0])
                responses.append(int(file.split('_')[1]))
                inter = file.split('_')[3]

            if audio_id == ticket.interview_number and inter != '00000000':
                fragments.append(AudioSegment.from_mp3(os.path.join(root, file)))

    if fragments and 18 in responses:
        new_name = os.path.join(
            AUDIO_UPLOAD_RTK, '{tt_num}_{tel_num}.mp3'.format(tt_num=ticket.pk, tel_num=ticket.telephone)
        )
        sum(fragments).export(new_name, format='mp3')
        ticket.audio = new_name
        ticket.state_compl = 'new'
        ticket.save()
        return True
    else:
        return False
