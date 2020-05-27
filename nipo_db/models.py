from django.db import models


class Contactlog(models.Model):
    appointmenttime = models.DateTimeField(db_column='AppointmentTime', blank=True, null=True)  # Field name made lowercase.
    areacoderespondent = models.CharField(db_column='AreaCodeRespondent', max_length=17, blank=True, null=True)  # Field name made lowercase.
    channel = models.IntegerField(db_column='Channel', blank=True, null=True)  # Field name made lowercase.
    contactdatetime = models.DateTimeField(db_column='ContactDateTime', primary_key=True)  # Field name made lowercase.
    contactnumber = models.IntegerField(db_column='ContactNumber', blank=True, null=True)  # Field name made lowercase.
    edittime = models.IntegerField(db_column='EditTime', blank=True, null=True)  # Field name made lowercase.
    interviewernumber = models.IntegerField(db_column='InterviewerNumber', blank=True, null=True)  # Field name made lowercase.
    interviewnumber = models.IntegerField(db_column='InterviewNumber')  # Field name made lowercase.
    introductiontime = models.IntegerField(db_column='IntroductionTime', blank=True, null=True)  # Field name made lowercase.
    numberofscreens = models.IntegerField(db_column='NumberOfScreens', blank=True, null=True)  # Field name made lowercase.
    responsestatus = models.IntegerField(db_column='ResponseStatus', blank=True, null=True)  # Field name made lowercase.
    stationid = models.CharField(db_column='StationID', max_length=100)  # Field name made lowercase.
    surveyname = models.CharField(db_column='SurveyName', max_length=7)  # Field name made lowercase.
    telephonetime = models.IntegerField(db_column='TelephoneTime', blank=True, null=True)  # Field name made lowercase.
    totalsurveyname = models.CharField(db_column='TotalSurveyName', max_length=7, blank=True, null=True)  # Field name made lowercase.
    totaltime = models.IntegerField(db_column='TotalTime', blank=True, null=True)  # Field name made lowercase.
    waitingtime = models.IntegerField(db_column='WaitingTime', blank=True, null=True)  # Field name made lowercase.
    samplewaittime = models.IntegerField(db_column='SampleWaitTime', blank=True, null=True)  # Field name made lowercase.
    bill = models.IntegerField(db_column='Bill', blank=True, null=True)  # Field name made lowercase.
    dialer = models.BooleanField(db_column='DIALER')  # Field name made lowercase.
    server = models.CharField(db_column='SERVER', max_length=16, blank=True, null=True)  # Field name made lowercase.
    netid = models.IntegerField(db_column='NetID', blank=True, null=True)  # Field name made lowercase.
    screencount = models.IntegerField(db_column='ScreenCount', blank=True, null=True)  # Field name made lowercase.
    smssent = models.BooleanField(db_column='SMSSent', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ContactLog'
        unique_together = (('contactdatetime', 'surveyname', 'interviewnumber'),)


class Sample5Star(models.Model):
    interviewnumber = models.IntegerField(db_column='InterviewNumber', primary_key=True)  # Field name made lowercase.
    responsecode = models.IntegerField(db_column='ResponseCode', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    suspendimage = models.BinaryField(db_column='SuspendImage', blank=True, null=True)  # Field name made lowercase.
    numberofcontacts = models.IntegerField(db_column='NumberOfContacts', blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    contacttime = models.DateTimeField(db_column='ContactTime', blank=True, null=True)  # Field name made lowercase.
    channel = models.IntegerField(db_column='Channel', blank=True, null=True)  # Field name made lowercase.
    initialchannel = models.IntegerField(db_column='InitialChannel', blank=True, null=True)  # Field name made lowercase.
    systemdata = models.CharField(db_column='SystemData', max_length=10, blank=True, null=True)  # Field name made lowercase.
    appointmenttime = models.DateTimeField(db_column='AppointmentTime', blank=True, null=True)  # Field name made lowercase.
    appointmentname = models.CharField(db_column='AppointmentName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    telephonenumber = models.CharField(db_column='TelephoneNumber', max_length=17, blank=True, null=True)  # Field name made lowercase.
    interviewernumber = models.IntegerField(db_column='InterviewerNumber', blank=True, null=True)  # Field name made lowercase.
    targetinterviewer = models.IntegerField(db_column='TargetInterviewer', blank=True, null=True)  # Field name made lowercase.
    showdisplayfields = models.IntegerField(db_column='ShowDisplayFields', blank=True, null=True)  # Field name made lowercase.
    displayfield1 = models.CharField(db_column='DisplayField1', max_length=45, blank=True, null=True)  # Field name made lowercase.
    displayfield2 = models.CharField(db_column='DisplayField2', max_length=35, blank=True, null=True)  # Field name made lowercase.
    displayfield3 = models.CharField(db_column='DisplayField3', max_length=35, blank=True, null=True)  # Field name made lowercase.
    displayfield4 = models.CharField(db_column='DisplayField4', max_length=35, blank=True, null=True)  # Field name made lowercase.
    showsecondphonenumber = models.IntegerField(db_column='ShowSecondPhoneNumber', blank=True, null=True)  # Field name made lowercase.
    indicator2ndnumber = models.IntegerField(db_column='Indicator2ndNumber', blank=True, null=True)  # Field name made lowercase.
    secondphonenumber = models.CharField(db_column='SecondPhoneNumber', max_length=17, blank=True, null=True)  # Field name made lowercase.
    timedifference = models.IntegerField(db_column='TimeDifference', blank=True, null=True)  # Field name made lowercase.
    groupid = models.CharField(db_column='GroupID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    callintervalbegin = models.IntegerField(db_column='CallIntervalBegin', blank=True, null=True)  # Field name made lowercase.
    callintervalend = models.IntegerField(db_column='CallIntervalEnd', blank=True, null=True)  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=50, blank=True, null=True)  # Field name made lowercase.
    extradata = models.CharField(db_column='ExtraData', max_length=215, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    date_obs = models.CharField(db_column='DATE_OBS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    remont_zakaz = models.CharField(db_column='REMONT_ZAKAZ', max_length=100, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='PHONE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    vin = models.CharField(db_column='VIN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    vehicle_year = models.CharField(db_column='VEHICLE_YEAR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    client_type = models.CharField(db_column='CLIENT_TYPE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='GENDER', max_length=100, blank=True, null=True)  # Field name made lowercase.
    s_family = models.CharField(db_column='S_FAMILY', max_length=100, blank=True, null=True)  # Field name made lowercase.
    wave = models.CharField(db_column='WAVE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    survey = models.CharField(db_column='SURVEY', max_length=100, blank=True, null=True)  # Field name made lowercase.
    consent = models.CharField(db_column='CONSENT', max_length=100, blank=True, null=True)  # Field name made lowercase.
    screenoutquestion = models.CharField(db_column='SCREENOUTQUESTION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dealername = models.CharField(db_column='DEALERNAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dealercode = models.CharField(db_column='DEALERCODE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    respnum = models.CharField(db_column='RESPNUM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dealercodewave = models.CharField(db_column='DEALERCODEWAVE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    csidate = models.CharField(db_column='CSIDATE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='MODEL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ttrespemail = models.CharField(db_column='TTRESPEMAIL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modelcode = models.CharField(db_column='MODELCODE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    qst = models.CharField(db_column='QST', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customeraddress = models.CharField(db_column='CUSTOMERADDRESS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    groupset = models.CharField(db_column='GROUPSET', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dealercodewavephase = models.CharField(db_column='DEALERCODEWAVEPHASE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    salesman = models.CharField(db_column='SALESMAN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    salesman_code = models.CharField(db_column='SALESMAN_CODE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ipsos_region = models.CharField(db_column='IPSOS_REGION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    datelload = models.CharField(db_column='Datelload', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fileload = models.CharField(db_column='Fileload', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dateload = models.CharField(db_column='Dateload', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sample5star'
        verbose_name = 'Мерседес продажи легковые 2020'
        verbose_name_plural = 'Мерседес продажи легковые 2020'


class Sample5Stasm(models.Model):
    interviewnumber = models.IntegerField(db_column='InterviewNumber', primary_key=True)  # Field name made lowercase.
    responsecode = models.IntegerField(db_column='ResponseCode', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    suspendimage = models.BinaryField(db_column='SuspendImage', blank=True, null=True)  # Field name made lowercase.
    numberofcontacts = models.IntegerField(db_column='NumberOfContacts', blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    contacttime = models.DateTimeField(db_column='ContactTime', blank=True, null=True)  # Field name made lowercase.
    channel = models.IntegerField(db_column='Channel', blank=True, null=True)  # Field name made lowercase.
    initialchannel = models.IntegerField(db_column='InitialChannel', blank=True, null=True)  # Field name made lowercase.
    systemdata = models.CharField(db_column='SystemData', max_length=10, blank=True, null=True)  # Field name made lowercase.
    appointmenttime = models.DateTimeField(db_column='AppointmentTime', blank=True, null=True)  # Field name made lowercase.
    appointmentname = models.CharField(db_column='AppointmentName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    telephonenumber = models.CharField(db_column='TelephoneNumber', max_length=17, blank=True, null=True)  # Field name made lowercase.
    interviewernumber = models.IntegerField(db_column='InterviewerNumber', blank=True, null=True)  # Field name made lowercase.
    targetinterviewer = models.IntegerField(db_column='TargetInterviewer', blank=True, null=True)  # Field name made lowercase.
    showdisplayfields = models.IntegerField(db_column='ShowDisplayFields', blank=True, null=True)  # Field name made lowercase.
    displayfield1 = models.CharField(db_column='DisplayField1', max_length=45, blank=True, null=True)  # Field name made lowercase.
    displayfield2 = models.CharField(db_column='DisplayField2', max_length=35, blank=True, null=True)  # Field name made lowercase.
    displayfield3 = models.CharField(db_column='DisplayField3', max_length=35, blank=True, null=True)  # Field name made lowercase.
    displayfield4 = models.CharField(db_column='DisplayField4', max_length=35, blank=True, null=True)  # Field name made lowercase.
    showsecondphonenumber = models.IntegerField(db_column='ShowSecondPhoneNumber', blank=True, null=True)  # Field name made lowercase.
    indicator2ndnumber = models.IntegerField(db_column='Indicator2ndNumber', blank=True, null=True)  # Field name made lowercase.
    secondphonenumber = models.CharField(db_column='SecondPhoneNumber', max_length=17, blank=True, null=True)  # Field name made lowercase.
    timedifference = models.IntegerField(db_column='TimeDifference', blank=True, null=True)  # Field name made lowercase.
    groupid = models.CharField(db_column='GroupID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    callintervalbegin = models.IntegerField(db_column='CallIntervalBegin', blank=True, null=True)  # Field name made lowercase.
    callintervalend = models.IntegerField(db_column='CallIntervalEnd', blank=True, null=True)  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=50, blank=True, null=True)  # Field name made lowercase.
    extradata = models.CharField(db_column='ExtraData', max_length=215, blank=True, null=True)  # Field name made lowercase.
    ipsos_region = models.CharField(db_column='IPSOS_REGION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    obsdate = models.CharField(db_column='OBSDATE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    remont_zakaz = models.CharField(db_column='REMONT_ZAKAZ', max_length=100, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='PHONE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    vin = models.CharField(db_column='VIN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    vehicle_year = models.CharField(db_column='VEHICLE_YEAR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    client_type = models.CharField(db_column='CLIENT_TYPE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    wave = models.CharField(db_column='WAVE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    consent = models.CharField(db_column='CONSENT', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dealer_name = models.CharField(db_column='DEALER_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dealer_city = models.CharField(db_column='DEALER_CITY', max_length=100, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='MODEL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    origin_dealer_code = models.CharField(db_column='ORIGIN_DEALER_CODE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dealercodewave = models.CharField(db_column='DEALERCODEWAVE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    master_name = models.CharField(db_column='MASTER_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    respnum = models.CharField(db_column='RESPNUM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    screenoutquestion = models.CharField(db_column='SCREENOUTQUESTION', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sample5stasm'
        verbose_name = 'Мерседес сервис легковые 2020'
        verbose_name_plural = 'Мерседес сервис легковые 2020'


class Sampledkcsias(models.Model):
    interviewnumber = models.IntegerField(db_column='InterviewNumber', primary_key=True)  # Field name made lowercase.
    responsecode = models.IntegerField(db_column='ResponseCode', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    suspendimage = models.BinaryField(db_column='SuspendImage', blank=True, null=True)  # Field name made lowercase.
    numberofcontacts = models.IntegerField(db_column='NumberOfContacts', blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    contacttime = models.DateTimeField(db_column='ContactTime', blank=True, null=True)  # Field name made lowercase.
    channel = models.IntegerField(db_column='Channel', blank=True, null=True)  # Field name made lowercase.
    initialchannel = models.IntegerField(db_column='InitialChannel', blank=True, null=True)  # Field name made lowercase.
    systemdata = models.CharField(db_column='SystemData', max_length=10, blank=True, null=True)  # Field name made lowercase.
    appointmenttime = models.DateTimeField(db_column='AppointmentTime', blank=True, null=True)  # Field name made lowercase.
    appointmentname = models.CharField(db_column='AppointmentName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    telephonenumber = models.CharField(db_column='TelephoneNumber', max_length=17, blank=True, null=True)  # Field name made lowercase.
    interviewernumber = models.IntegerField(db_column='InterviewerNumber', blank=True, null=True)  # Field name made lowercase.
    targetinterviewer = models.IntegerField(db_column='TargetInterviewer', blank=True, null=True)  # Field name made lowercase.
    showdisplayfields = models.IntegerField(db_column='ShowDisplayFields', blank=True, null=True)  # Field name made lowercase.
    displayfield1 = models.CharField(db_column='DisplayField1', max_length=45, blank=True, null=True)  # Field name made lowercase.
    displayfield2 = models.CharField(db_column='DisplayField2', max_length=35, blank=True, null=True)  # Field name made lowercase.
    displayfield3 = models.CharField(db_column='DisplayField3', max_length=35, blank=True, null=True)  # Field name made lowercase.
    displayfield4 = models.CharField(db_column='DisplayField4', max_length=35, blank=True, null=True)  # Field name made lowercase.
    showsecondphonenumber = models.IntegerField(db_column='ShowSecondPhoneNumber', blank=True, null=True)  # Field name made lowercase.
    indicator2ndnumber = models.IntegerField(db_column='Indicator2ndNumber', blank=True, null=True)  # Field name made lowercase.
    secondphonenumber = models.CharField(db_column='SecondPhoneNumber', max_length=17, blank=True, null=True)  # Field name made lowercase.
    timedifference = models.IntegerField(db_column='TimeDifference', blank=True, null=True)  # Field name made lowercase.
    groupid = models.CharField(db_column='GroupID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    callintervalbegin = models.IntegerField(db_column='CallIntervalBegin', blank=True, null=True)  # Field name made lowercase.
    callintervalend = models.IntegerField(db_column='CallIntervalEnd', blank=True, null=True)  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=50, blank=True, null=True)  # Field name made lowercase.
    extradata = models.CharField(db_column='ExtraData', max_length=215, blank=True, null=True)  # Field name made lowercase.
    dealer_code = models.CharField(db_column='DEALER_CODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dealer_name = models.CharField(db_column='DEALER_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dateobs = models.CharField(db_column='DATEOBS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    remontzakaz = models.CharField(db_column='REMONTZAKAZ', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='PHONE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vin = models.CharField(db_column='VIN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vin_am = models.CharField(db_column='VIN_AM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vehicle_year = models.CharField(db_column='VEHICLE_YEAR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    client_type = models.CharField(db_column='CLIENT_TYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    master = models.CharField(db_column='MASTER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    master_name = models.CharField(db_column='MASTER_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='REGION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    respnum = models.CharField(db_column='RespNum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=65, blank=True, null=True)  # Field name made lowercase.
    screenoutquestion = models.CharField(db_column='ScreenOutQuestion', max_length=65, blank=True, null=True)  # Field name made lowercase.
    dealercodewave = models.CharField(db_column='DealerCodeWave', max_length=50, blank=True, null=True)  # Field name made lowercase.
    wave = models.CharField(db_column='WAVE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    priznak = models.CharField(max_length=150, blank=True, null=True)
    block = models.CharField(db_column='BLOCK', max_length=50, blank=True, null=True)  # Field name made lowercase.
    blcok = models.CharField(db_column='Blcok', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SampleDkcsias'
        verbose_name = 'Камаз сервис 2020'
        verbose_name_plural = 'Камаз сервис 2020'


class Sampledkcsisa(models.Model):
    interviewnumber = models.IntegerField(db_column='InterviewNumber', primary_key=True)  # Field name made lowercase.
    responsecode = models.IntegerField(db_column='ResponseCode', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    suspendimage = models.BinaryField(db_column='SuspendImage', blank=True, null=True)  # Field name made lowercase.
    numberofcontacts = models.IntegerField(db_column='NumberOfContacts', blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    contacttime = models.DateTimeField(db_column='ContactTime', blank=True, null=True)  # Field name made lowercase.
    channel = models.IntegerField(db_column='Channel', blank=True, null=True)  # Field name made lowercase.
    initialchannel = models.IntegerField(db_column='InitialChannel', blank=True, null=True)  # Field name made lowercase.
    systemdata = models.CharField(db_column='SystemData', max_length=10, blank=True, null=True)  # Field name made lowercase.
    appointmenttime = models.DateTimeField(db_column='AppointmentTime', blank=True, null=True)  # Field name made lowercase.
    appointmentname = models.CharField(db_column='AppointmentName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    telephonenumber = models.CharField(db_column='TelephoneNumber', max_length=17, blank=True, null=True)  # Field name made lowercase.
    interviewernumber = models.IntegerField(db_column='InterviewerNumber', blank=True, null=True)  # Field name made lowercase.
    targetinterviewer = models.IntegerField(db_column='TargetInterviewer', blank=True, null=True)  # Field name made lowercase.
    showdisplayfields = models.IntegerField(db_column='ShowDisplayFields', blank=True, null=True)  # Field name made lowercase.
    displayfield1 = models.CharField(db_column='DisplayField1', max_length=45, blank=True, null=True)  # Field name made lowercase.
    displayfield2 = models.CharField(db_column='DisplayField2', max_length=35, blank=True, null=True)  # Field name made lowercase.
    displayfield3 = models.CharField(db_column='DisplayField3', max_length=35, blank=True, null=True)  # Field name made lowercase.
    displayfield4 = models.CharField(db_column='DisplayField4', max_length=35, blank=True, null=True)  # Field name made lowercase.
    showsecondphonenumber = models.IntegerField(db_column='ShowSecondPhoneNumber', blank=True, null=True)  # Field name made lowercase.
    indicator2ndnumber = models.IntegerField(db_column='Indicator2ndNumber', blank=True, null=True)  # Field name made lowercase.
    secondphonenumber = models.CharField(db_column='SecondPhoneNumber', max_length=17, blank=True, null=True)  # Field name made lowercase.
    timedifference = models.IntegerField(db_column='TimeDifference', blank=True, null=True)  # Field name made lowercase.
    groupid = models.CharField(db_column='GroupID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    callintervalbegin = models.IntegerField(db_column='CallIntervalBegin', blank=True, null=True)  # Field name made lowercase.
    callintervalend = models.IntegerField(db_column='CallIntervalEnd', blank=True, null=True)  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=50, blank=True, null=True)  # Field name made lowercase.
    extradata = models.CharField(db_column='ExtraData', max_length=215, blank=True, null=True)  # Field name made lowercase.
    dealer_code = models.CharField(db_column='DEALER_CODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dealer_name = models.CharField(db_column='DEALER_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dateobs = models.CharField(db_column='DATEOBS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    remontzakaz = models.CharField(db_column='REMONTZAKAZ', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='PHONE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vin = models.CharField(db_column='VIN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vin_am = models.CharField(db_column='VIN_AM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vehicle_year = models.CharField(db_column='VEHICLE_YEAR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    client_type = models.CharField(db_column='CLIENT_TYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seller_name = models.CharField(db_column='SELLER_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    screenoutquestion = models.CharField(db_column='SCREENOUTQUESTION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='REGION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    respnum = models.CharField(db_column='RESPNUM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='MODEL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seller_code = models.CharField(db_column='SELLER_CODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    wave = models.CharField(db_column='WAVE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dealercodewave = models.CharField(db_column='DealerCodeWave', max_length=50, blank=True, null=True)  # Field name made lowercase.
    priznak = models.CharField(max_length=150, blank=True, null=True)
    block = models.CharField(db_column='Block', max_length=50, blank=True, null=True)  # Field name made lowercase.
    s4_1_1_failed = models.CharField(db_column='S4_1_1_failed', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SampleDkcsisa'
        verbose_name = 'Камаз продажи 2020'
        verbose_name_plural = 'Камаз продажи 2020'


class Samplehcsisal(models.Model):
    interviewnumber = models.IntegerField(db_column='InterviewNumber', primary_key=True)  # Field name made lowercase.
    responsecode = models.IntegerField(db_column='ResponseCode', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    suspendimage = models.BinaryField(db_column='SuspendImage', blank=True, null=True)  # Field name made lowercase.
    numberofcontacts = models.IntegerField(db_column='NumberOfContacts', blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    contacttime = models.DateTimeField(db_column='ContactTime', blank=True, null=True)  # Field name made lowercase.
    channel = models.IntegerField(db_column='Channel', blank=True, null=True)  # Field name made lowercase.
    initialchannel = models.IntegerField(db_column='InitialChannel', blank=True, null=True)  # Field name made lowercase.
    systemdata = models.CharField(db_column='SystemData', max_length=10, blank=True, null=True)  # Field name made lowercase.
    appointmenttime = models.DateTimeField(db_column='AppointmentTime', blank=True, null=True)  # Field name made lowercase.
    appointmentname = models.CharField(db_column='AppointmentName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    telephonenumber = models.CharField(db_column='TelephoneNumber', max_length=17, blank=True, null=True)  # Field name made lowercase.
    interviewernumber = models.IntegerField(db_column='InterviewerNumber', blank=True, null=True)  # Field name made lowercase.
    targetinterviewer = models.IntegerField(db_column='TargetInterviewer', blank=True, null=True)  # Field name made lowercase.
    showdisplayfields = models.IntegerField(db_column='ShowDisplayFields', blank=True, null=True)  # Field name made lowercase.
    displayfield1 = models.CharField(db_column='DisplayField1', max_length=45, blank=True, null=True)  # Field name made lowercase.
    displayfield2 = models.CharField(db_column='DisplayField2', max_length=35, blank=True, null=True)  # Field name made lowercase.
    displayfield3 = models.CharField(db_column='DisplayField3', max_length=35, blank=True, null=True)  # Field name made lowercase.
    displayfield4 = models.CharField(db_column='DisplayField4', max_length=35, blank=True, null=True)  # Field name made lowercase.
    showsecondphonenumber = models.IntegerField(db_column='ShowSecondPhoneNumber', blank=True, null=True)  # Field name made lowercase.
    indicator2ndnumber = models.IntegerField(db_column='Indicator2ndNumber', blank=True, null=True)  # Field name made lowercase.
    secondphonenumber = models.CharField(db_column='SecondPhoneNumber', max_length=17, blank=True, null=True)  # Field name made lowercase.
    timedifference = models.IntegerField(db_column='TimeDifference', blank=True, null=True)  # Field name made lowercase.
    groupid = models.CharField(db_column='GroupID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    callintervalbegin = models.IntegerField(db_column='CallIntervalBegin', blank=True, null=True)  # Field name made lowercase.
    callintervalend = models.IntegerField(db_column='CallIntervalEnd', blank=True, null=True)  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=50, blank=True, null=True)  # Field name made lowercase.
    extradata = models.CharField(db_column='ExtraData', max_length=215, blank=True, null=True)  # Field name made lowercase.
    vin = models.CharField(db_column='VIN', max_length=150, blank=True, null=True)  # Field name made lowercase.
    fio = models.CharField(db_column='FIO', max_length=150, blank=True, null=True)  # Field name made lowercase.
    dealer_code = models.CharField(db_column='DEALER_CODE', max_length=150, blank=True, null=True)  # Field name made lowercase.
    dealername = models.CharField(db_column='DEALERNAME', max_length=150, blank=True, null=True)  # Field name made lowercase.
    modelcode = models.CharField(db_column='MODELCODE', max_length=150, blank=True, null=True)  # Field name made lowercase.
    wave = models.CharField(db_column='WAVE', max_length=150, blank=True, null=True)  # Field name made lowercase.
    dealercodewave = models.CharField(db_column='DEALERCODEWAVE', max_length=150, blank=True, null=True)  # Field name made lowercase.
    ipsos_region = models.CharField(db_column='IPSOS_REGION', max_length=150, blank=True, null=True)  # Field name made lowercase.
    dateload = models.CharField(db_column='DATELOAD', max_length=150, blank=True, null=True)  # Field name made lowercase.
    fileload = models.CharField(db_column='FILELOAD', max_length=150, blank=True, null=True)  # Field name made lowercase.
    screenoutquestion = models.CharField(db_column='SCREENOUTQUESTION', max_length=150, blank=True, null=True)  # Field name made lowercase.
    block = models.CharField(db_column='Block', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SampleHcsisal'


class Samplehcsiser(models.Model):
    interviewnumber = models.IntegerField(db_column='InterviewNumber', primary_key=True)  # Field name made lowercase.
    responsecode = models.IntegerField(db_column='ResponseCode', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    suspendimage = models.BinaryField(db_column='SuspendImage', blank=True, null=True)  # Field name made lowercase.
    numberofcontacts = models.IntegerField(db_column='NumberOfContacts', blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    contacttime = models.DateTimeField(db_column='ContactTime', blank=True, null=True)  # Field name made lowercase.
    channel = models.IntegerField(db_column='Channel', blank=True, null=True)  # Field name made lowercase.
    initialchannel = models.IntegerField(db_column='InitialChannel', blank=True, null=True)  # Field name made lowercase.
    systemdata = models.CharField(db_column='SystemData', max_length=10, blank=True, null=True)  # Field name made lowercase.
    appointmenttime = models.DateTimeField(db_column='AppointmentTime', blank=True, null=True)  # Field name made lowercase.
    appointmentname = models.CharField(db_column='AppointmentName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    telephonenumber = models.CharField(db_column='TelephoneNumber', max_length=17, blank=True, null=True)  # Field name made lowercase.
    interviewernumber = models.IntegerField(db_column='InterviewerNumber', blank=True, null=True)  # Field name made lowercase.
    targetinterviewer = models.IntegerField(db_column='TargetInterviewer', blank=True, null=True)  # Field name made lowercase.
    showdisplayfields = models.IntegerField(db_column='ShowDisplayFields', blank=True, null=True)  # Field name made lowercase.
    displayfield1 = models.CharField(db_column='DisplayField1', max_length=45, blank=True, null=True)  # Field name made lowercase.
    displayfield2 = models.CharField(db_column='DisplayField2', max_length=35, blank=True, null=True)  # Field name made lowercase.
    displayfield3 = models.CharField(db_column='DisplayField3', max_length=35, blank=True, null=True)  # Field name made lowercase.
    displayfield4 = models.CharField(db_column='DisplayField4', max_length=35, blank=True, null=True)  # Field name made lowercase.
    showsecondphonenumber = models.IntegerField(db_column='ShowSecondPhoneNumber', blank=True, null=True)  # Field name made lowercase.
    indicator2ndnumber = models.IntegerField(db_column='Indicator2ndNumber', blank=True, null=True)  # Field name made lowercase.
    secondphonenumber = models.CharField(db_column='SecondPhoneNumber', max_length=17, blank=True, null=True)  # Field name made lowercase.
    timedifference = models.IntegerField(db_column='TimeDifference', blank=True, null=True)  # Field name made lowercase.
    groupid = models.CharField(db_column='GroupID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    callintervalbegin = models.IntegerField(db_column='CallIntervalBegin', blank=True, null=True)  # Field name made lowercase.
    callintervalend = models.IntegerField(db_column='CallIntervalEnd', blank=True, null=True)  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=50, blank=True, null=True)  # Field name made lowercase.
    extradata = models.CharField(db_column='ExtraData', max_length=215, blank=True, null=True)  # Field name made lowercase.
    vin = models.CharField(db_column='VIN', max_length=150, blank=True, null=True)  # Field name made lowercase.
    fio = models.CharField(db_column='FIO', max_length=150, blank=True, null=True)  # Field name made lowercase.
    dealer_code = models.CharField(db_column='DEALER_CODE', max_length=150, blank=True, null=True)  # Field name made lowercase.
    dealername = models.CharField(db_column='DEALERNAME', max_length=150, blank=True, null=True)  # Field name made lowercase.
    dealercodewave = models.CharField(db_column='DEALERCODEWAVE', max_length=150, blank=True, null=True)  # Field name made lowercase.
    wave = models.CharField(db_column='WAVE', max_length=150, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='MODEL', max_length=150, blank=True, null=True)  # Field name made lowercase.
    ipsos_region = models.CharField(db_column='IPSOS_REGION', max_length=150, blank=True, null=True)  # Field name made lowercase.
    dateload = models.CharField(db_column='Dateload', max_length=150, blank=True, null=True)  # Field name made lowercase.
    fileload = models.CharField(db_column='Fileload', max_length=150, blank=True, null=True)  # Field name made lowercase.
    screenoutquestion = models.CharField(db_column='SCREENOUTQUESTION', max_length=150, blank=True, null=True)  # Field name made lowercase.
    modelcode = models.CharField(db_column='MODELCODE', max_length=150, blank=True, null=True)  # Field name made lowercase.
    block = models.CharField(max_length=65, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SampleHcsiser'


class Samplemta2020(models.Model):
    interviewnumber = models.IntegerField(db_column='InterviewNumber', primary_key=True)  # Field name made lowercase.
    responsecode = models.IntegerField(db_column='ResponseCode', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    suspendimage = models.BinaryField(db_column='SuspendImage', blank=True, null=True)  # Field name made lowercase.
    numberofcontacts = models.IntegerField(db_column='NumberOfContacts', blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    contacttime = models.DateTimeField(db_column='ContactTime', blank=True, null=True)  # Field name made lowercase.
    channel = models.IntegerField(db_column='Channel', blank=True, null=True)  # Field name made lowercase.
    initialchannel = models.IntegerField(db_column='InitialChannel', blank=True, null=True)  # Field name made lowercase.
    systemdata = models.CharField(db_column='SystemData', max_length=10, blank=True, null=True)  # Field name made lowercase.
    appointmenttime = models.DateTimeField(db_column='AppointmentTime', blank=True, null=True)  # Field name made lowercase.
    appointmentname = models.CharField(db_column='AppointmentName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    telephonenumber = models.CharField(db_column='TelephoneNumber', max_length=17, blank=True, null=True)  # Field name made lowercase.
    interviewernumber = models.IntegerField(db_column='InterviewerNumber', blank=True, null=True)  # Field name made lowercase.
    targetinterviewer = models.IntegerField(db_column='TargetInterviewer', blank=True, null=True)  # Field name made lowercase.
    showdisplayfields = models.IntegerField(db_column='ShowDisplayFields', blank=True, null=True)  # Field name made lowercase.
    displayfield1 = models.CharField(db_column='DisplayField1', max_length=45, blank=True, null=True)  # Field name made lowercase.
    displayfield2 = models.CharField(db_column='DisplayField2', max_length=35, blank=True, null=True)  # Field name made lowercase.
    displayfield3 = models.CharField(db_column='DisplayField3', max_length=35, blank=True, null=True)  # Field name made lowercase.
    displayfield4 = models.CharField(db_column='DisplayField4', max_length=35, blank=True, null=True)  # Field name made lowercase.
    showsecondphonenumber = models.IntegerField(db_column='ShowSecondPhoneNumber', blank=True, null=True)  # Field name made lowercase.
    indicator2ndnumber = models.IntegerField(db_column='Indicator2ndNumber', blank=True, null=True)  # Field name made lowercase.
    secondphonenumber = models.CharField(db_column='SecondPhoneNumber', max_length=17, blank=True, null=True)  # Field name made lowercase.
    timedifference = models.IntegerField(db_column='TimeDifference', blank=True, null=True)  # Field name made lowercase.
    groupid = models.CharField(db_column='GroupID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    callintervalbegin = models.IntegerField(db_column='CallIntervalBegin', blank=True, null=True)  # Field name made lowercase.
    callintervalend = models.IntegerField(db_column='CallIntervalEnd', blank=True, null=True)  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=50, blank=True, null=True)  # Field name made lowercase.
    extradata = models.CharField(db_column='ExtraData', max_length=215, blank=True, null=True)  # Field name made lowercase.
    dealer_code = models.CharField(db_column='DEALER_CODE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    date_obs = models.CharField(db_column='DATE_OBS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    remont_zakaz = models.CharField(db_column='REMONT_ZAKAZ', max_length=100, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='PHONE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    vin = models.CharField(db_column='VIN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    vehicle_year = models.CharField(db_column='VEHICLE_YEAR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    client_type = models.CharField(db_column='CLIENT_TYPE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    master = models.CharField(db_column='MASTER', max_length=100, blank=True, null=True)  # Field name made lowercase.
    master_name = models.CharField(db_column='MASTER_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='GENDER', max_length=100, blank=True, null=True)  # Field name made lowercase.
    wave = models.CharField(db_column='WAVE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    consent = models.CharField(db_column='CONSENT', max_length=100, blank=True, null=True)  # Field name made lowercase.
    screenoutquestion = models.CharField(db_column='SCREENOUTQUESTION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dealername = models.CharField(db_column='DEALERNAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    respnum = models.CharField(db_column='RESPNUM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    compl_audio = models.CharField(db_column='COMPL_AUDIO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    localtime = models.CharField(db_column='LOCALTIME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dealercodewave = models.CharField(db_column='DEALERCODEWAVE', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SampleMta2020'
        verbose_name = 'Мерседес сервис малотоннажные 2020'
        verbose_name_plural = 'Мерседес сервис малотоннажные 2020'


class Survey(models.Model):
    closetime = models.DateTimeField(db_column='CloseTime', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    surveyname = models.CharField(db_column='SurveyName', primary_key=True, max_length=7)  # Field name made lowercase.
    surveyversion = models.CharField(db_column='SurveyVersion', max_length=1, blank=True, null=True)  # Field name made lowercase.
    surveytype = models.SmallIntegerField(db_column='SurveyType', blank=True, null=True)  # Field name made lowercase.
    diary = models.IntegerField(db_column='Diary')  # Field name made lowercase.
    interval = models.IntegerField(db_column='Interval', blank=True, null=True)  # Field name made lowercase.
    anonymous = models.BooleanField(db_column='Anonymous')  # Field name made lowercase.
    bidi = models.BooleanField(db_column='BiDi')  # Field name made lowercase.
    dialerparam = models.CharField(db_column='DialerParam', max_length=50, blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    enddatecati = models.DateTimeField(db_column='EndDateCATI', blank=True, null=True)  # Field name made lowercase.
    enddateoriginal = models.DateTimeField(db_column='EndDateOriginal', blank=True, null=True)  # Field name made lowercase.
    estimatedfailureduration = models.IntegerField(db_column='EstimatedFailureDuration', blank=True, null=True)  # Field name made lowercase.
    estimatedinterviewduration = models.IntegerField(db_column='EstimatedInterviewDuration', blank=True, null=True)  # Field name made lowercase.
    estimatedsuccessrate = models.IntegerField(db_column='EstimatedSuccessRate', blank=True, null=True)  # Field name made lowercase.
    fromaddress = models.CharField(db_column='FromAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fromname = models.CharField(db_column='FromName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    hideclear = models.BooleanField(db_column='HideClear')  # Field name made lowercase.
    hidecopyrightnotice = models.BooleanField(db_column='HideCopyrightNotice')  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastusedtextnr = models.IntegerField(db_column='LastUsedTextNr', blank=True, null=True)  # Field name made lowercase.
    link = models.CharField(db_column='Link', max_length=100, blank=True, null=True)  # Field name made lowercase.
    numberofinterviews = models.IntegerField(db_column='NumberOfInterviews', blank=True, null=True)  # Field name made lowercase.
    paymentversion = models.SmallIntegerField(db_column='PaymentVersion', blank=True, null=True)  # Field name made lowercase.
    queueid = models.CharField(db_column='QueueID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    replyaddress = models.CharField(db_column='ReplyAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    responsecodesnoreminders = models.CharField(db_column='ResponseCodesNoReminders', max_length=50, blank=True, null=True)  # Field name made lowercase.
    showclose = models.BooleanField(db_column='ShowClose')  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    startdatecati = models.DateTimeField(db_column='StartDateCATI', blank=True, null=True)  # Field name made lowercase.
    startdateoriginal = models.DateTimeField(db_column='StartdateOriginal', blank=True, null=True)  # Field name made lowercase.
    successfulcount = models.IntegerField(db_column='SuccessfulCount', blank=True, null=True)  # Field name made lowercase.
    successfulincrement = models.IntegerField(db_column='SuccessfulIncrement', blank=True, null=True)  # Field name made lowercase.
    surveydirect = models.SmallIntegerField(db_column='SurveyDirect', blank=True, null=True)  # Field name made lowercase.
    surveyid = models.CharField(db_column='SurveyID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    suspendable = models.BooleanField(db_column='Suspendable')  # Field name made lowercase.
    suspendtime = models.IntegerField(db_column='SuspendTime', blank=True, null=True)  # Field name made lowercase.
    suspendtimeanonymous = models.IntegerField(db_column='SuspendTimeAnonymous', blank=True, null=True)  # Field name made lowercase.
    suspendtimefirstscreen = models.IntegerField(db_column='SuspendTimeFirstScreen', blank=True, null=True)  # Field name made lowercase.
    switched = models.IntegerField(db_column='Switched', blank=True, null=True)  # Field name made lowercase.
    switchedremindinterval = models.IntegerField(db_column='SwitchedRemindInterval', blank=True, null=True)  # Field name made lowercase.
    switchedremindmax = models.IntegerField(db_column='SwitchedRemindMax', blank=True, null=True)  # Field name made lowercase.
    switchedtextnr = models.IntegerField(db_column='SwitchedTextNr', blank=True, null=True)  # Field name made lowercase.
    targetplanningcati = models.IntegerField(db_column='TargetPlanningCATI', blank=True, null=True)  # Field name made lowercase.
    excelsheet = models.CharField(db_column='ExcelSheet', max_length=256, blank=True, null=True)  # Field name made lowercase.
    projectnumber = models.CharField(db_column='ProjectNumber', max_length=256, blank=True, null=True)  # Field name made lowercase.
    fieldmanager = models.CharField(db_column='FieldManager', max_length=128, blank=True, null=True)  # Field name made lowercase.
    methodology = models.CharField(db_column='Methodology', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Survey'


class Samplertk06B(models.Model):
    interviewnumber = models.IntegerField(db_column='InterviewNumber', primary_key=True)  # Field name made lowercase.
    responsecode = models.IntegerField(db_column='ResponseCode', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    suspendimage = models.BinaryField(db_column='SuspendImage', blank=True, null=True)  # Field name made lowercase.
    numberofcontacts = models.IntegerField(db_column='NumberOfContacts', blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    contacttime = models.DateTimeField(db_column='ContactTime', blank=True, null=True)  # Field name made lowercase.
    channel = models.IntegerField(db_column='Channel', blank=True, null=True)  # Field name made lowercase.
    initialchannel = models.IntegerField(db_column='InitialChannel', blank=True, null=True)  # Field name made lowercase.
    systemdata = models.CharField(db_column='SystemData', max_length=10, blank=True, null=True)  # Field name made lowercase.
    appointmenttime = models.DateTimeField(db_column='AppointmentTime', blank=True, null=True)  # Field name made lowercase.
    appointmentname = models.CharField(db_column='AppointmentName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    telephonenumber = models.CharField(db_column='TelephoneNumber', max_length=17, blank=True, null=True)  # Field name made lowercase.
    interviewernumber = models.IntegerField(db_column='InterviewerNumber', blank=True, null=True)  # Field name made lowercase.
    targetinterviewer = models.IntegerField(db_column='TargetInterviewer', blank=True, null=True)  # Field name made lowercase.
    showdisplayfields = models.IntegerField(db_column='ShowDisplayFields', blank=True, null=True)  # Field name made lowercase.
    displayfield1 = models.CharField(db_column='DisplayField1', max_length=45, blank=True, null=True)  # Field name made lowercase.
    displayfield2 = models.CharField(db_column='DisplayField2', max_length=35, blank=True, null=True)  # Field name made lowercase.
    displayfield3 = models.CharField(db_column='DisplayField3', max_length=35, blank=True, null=True)  # Field name made lowercase.
    displayfield4 = models.CharField(db_column='DisplayField4', max_length=35, blank=True, null=True)  # Field name made lowercase.
    showsecondphonenumber = models.IntegerField(db_column='ShowSecondPhoneNumber', blank=True, null=True)  # Field name made lowercase.
    indicator2ndnumber = models.IntegerField(db_column='Indicator2ndNumber', blank=True, null=True)  # Field name made lowercase.
    secondphonenumber = models.CharField(db_column='SecondPhoneNumber', max_length=17, blank=True, null=True)  # Field name made lowercase.
    timedifference = models.IntegerField(db_column='TimeDifference', blank=True, null=True)  # Field name made lowercase.
    groupid = models.CharField(db_column='GroupID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    callintervalbegin = models.IntegerField(db_column='CallIntervalBegin', blank=True, null=True)  # Field name made lowercase.
    callintervalend = models.IntegerField(db_column='CallIntervalEnd', blank=True, null=True)  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=50, blank=True, null=True)  # Field name made lowercase.
    extradata = models.CharField(db_column='ExtraData', max_length=215, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='REGION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='CITY', max_length=100, blank=True, null=True)  # Field name made lowercase.
    package_name = models.CharField(db_column='PACKAGE_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    id_abonent = models.CharField(db_column='ID_ABONENT', max_length=100, blank=True, null=True)  # Field name made lowercase.
    order_num = models.CharField(db_column='ORDER_NUM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    city_quota = models.IntegerField(db_column='CITY_QUOTA', blank=True, null=True)  # Field name made lowercase.
    package_code1 = models.IntegerField(db_column='PACKAGE_CODE1', blank=True, null=True)  # Field name made lowercase.
    package_code2 = models.IntegerField(db_column='PACKAGE_CODE2', blank=True, null=True)  # Field name made lowercase.
    touchpoint = models.IntegerField(db_column='TOUCHPOINT', blank=True, null=True)  # Field name made lowercase.
    st = models.IntegerField(db_column='ST', blank=True, null=True)  # Field name made lowercase.
    macroreg = models.IntegerField(blank=True, null=True)
    quotacity1 = models.IntegerField(db_column='QUOTACITY1', blank=True, null=True)  # Field name made lowercase.
    quotacity2 = models.IntegerField(db_column='QUOTACITY2', blank=True, null=True)  # Field name made lowercase.
    quotacity3 = models.IntegerField(db_column='QUOTACITY3', blank=True, null=True)  # Field name made lowercase.
    lastdaycontact = models.CharField(db_column='Lastdaycontact', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tel_oldtime = models.IntegerField(blank=True, null=True)
    prior = models.IntegerField(blank=True, null=True)
    callcenter = models.IntegerField(db_column='CALLCENTER', blank=True, null=True)  # Field name made lowercase.
    totaldata = models.CharField(db_column='TOTALDATA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    callcenterdata = models.CharField(db_column='CALLCENTERDATA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    abonent = models.CharField(db_column='ABONENT', max_length=100, blank=True, null=True)  # Field name made lowercase.
    q_neg_res2_dd = models.CharField(db_column='q_NEG_RES2_dd', max_length=100, blank=True, null=True)  # Field name made lowercase.
    q_neg_res2_mm = models.CharField(db_column='q_NEG_RES2_mm', max_length=100, blank=True, null=True)  # Field name made lowercase.
    q_neg_res2_yyyy = models.CharField(db_column='q_NEG_RES2_yyyy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    q_neg_res2_hh = models.CharField(db_column='q_NEG_RES2_hh', max_length=100, blank=True, null=True)  # Field name made lowercase.
    q_neg_res2_min = models.CharField(db_column='q_NEG_RES2_min', max_length=100, blank=True, null=True)  # Field name made lowercase.
    q_neg_res2_com = models.CharField(db_column='q_NEG_RES2_com', max_length=650, blank=True, null=True)  # Field name made lowercase.
    q_csi = models.CharField(db_column='q_CSI', max_length=100, blank=True, null=True)  # Field name made lowercase.
    q_res = models.CharField(db_column='q_Res', max_length=100, blank=True, null=True)  # Field name made lowercase.
    q_nps = models.CharField(db_column='q_NPS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    q_nps_oe = models.CharField(db_column='q_NPS_OE', max_length=1500, blank=True, null=True)  # Field name made lowercase.
    q_csi_oe = models.CharField(db_column='q_CSI_OE', max_length=1500, blank=True, null=True)  # Field name made lowercase.
    q_neg_res_1 = models.CharField(db_column='q_NEG_RES_1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    q_neg_res_2 = models.CharField(db_column='q_NEG_RES_2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    q_neg_res_3 = models.CharField(db_column='q_NEG_RES_3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    q_neg_res1 = models.CharField(db_column='q_NEG_RES1', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SampleRtk06b'
