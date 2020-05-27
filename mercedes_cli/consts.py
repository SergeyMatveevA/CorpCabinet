import os

from sv.settings import MEDIA_ROOT

UPLOAD_MBR_DIR = os.path.join(MEDIA_ROOT, './media/mercedes/files/')

# Дата-мэп сырых данных к ребусовскому файлу кави второй фазы
CAWI_P2_REBUS = {
    'CLI01': 'Q_CLI01', 'CLI02': 'Q_CLI02', 'CLI03': 'Q_CLI03', 'CLI04': 'Q_CLI04', 'CS1': 'Q_CS1',
    'CS2[{_1}].q': 'Q_CS2_1', 'CS2[{_2}].q': 'Q_CS2_2', 'CS2[{_3}].q': 'Q_CS2_3', 'CS2[{_4}].q': 'Q_CS2_4',
    'CS4[{_1}].q': 'Q_CS4_1', 'CS4[{_2}].q': 'Q_CS4_2', 'CS4[{_3}].q': 'Q_CS4_3', 'CS4[{_4}].q': 'Q_CS4_4',
    'HIDDEN_CRM_dealer': 'Hidden_final_dealer', 'HIDDEN_CSI_Date': 'HIDDEN_ CSI_Date', 'HIDDEN_FIO': 'HIDDEN_Name',
    'HIDDEN_Gender': 'HIDDEN_GENDER', 'HIDDEN_Model': 'HIDDEN_ Model', 'HIDDEN_Salesman_code': 'HIDDEN_Salesman code',
    'HIDDEN_VIN': 'HIDDEN_ VIN', 'HIDDEN_email': 'HIDDEN_ e-mail', 'HIDDEN_phone': 'HIDDEN_ phone', 'RM2': 'v183',
    'RM3 (1/5)': 'RM3_1', 'RM3 (2/5)': 'RM3_2', 'RM3 (3/5)': 'RM3_3', 'RM3 (4/5)': 'RM3_4', 'RM3 (5/5)': 'RM3_5',
    'SB3 (1/6)': 'SB3_1', 'SB3 (2/6)': 'SB3_2', 'SB3 (3/6)': 'SB3_3', 'SB3 (4/6)': 'SB3_4', 'SB3 (5/6)': 'SB3_5',
    'SB3 (6/6)': 'SB3_6', 'SB3.oth_6': 'SB3_oth_6', 'VA01': 'VA1', 'VA02': 'VA2',
    'Respondent.Serial': 'Respondent_Serial', 'Q_SF01': 'v157', 'Q_SF02': 'SF02'
}

# Дата-мэп сырых данных к ребусовскому файлу кати второй фазы
CATI_P2_REBUS = {
    'INTNR': 'Respondent_Serial', 'HIDDEN_SURVEYS': 'HIDDEN_Survey', 'HIDDEN_PHASE': 'HIDDEN_phase',
    'HIDDEN_MODEL': 'HIDDEN_ Model', 'HIDDEN_VIN': 'HIDDEN_ VIN', 'TSB3C6': 'SB3_6_other',
    'CLI01': 'Q_CLI01', 'TCLI01_A': 'CLI01_a', 'CLI02': 'Q_CLI02', 'TCLI02_A': 'CLI02_a', 'CLI03': 'Q_CLI03',
    'TCLI03_A': 'CLI03_a', 'CLI04': 'Q_CLI04', 'TCLI04_A': 'CLI04a', 'CS1': 'Q_CS1', 'TCS1A': 'CS1a',
    'CS2_1': 'Q_CS2_1', 'CS2_2': 'Q_CS2_2', 'CS2_3': 'Q_CS2_3', 'CS2_4': 'Q_CS2_4', 'CS4_1': 'Q_CS4_1',
    'CS4_2': 'Q_CS4_2', 'CS4_3': 'Q_CS4_3', 'CS4_4': 'Q_CS4_4', 'RM2': 'v183', 'TCIPOS': 'CIPOS',
    'TCINEG': 'CINEG', 'TRP3': 'RP3', 'HIDDEN_CRM_DEALER': 'Hidden_final_dealer', 'Q_SF01': 'v157', 'Q_SF02': 'SF02'
}

# Пути к клиентским шаблонам
HQ_TEMPL_P1 = os.path.join('./mercedes_cli/docs/Data Input CSI Sales_2019_orig.xlsm')
HQ_TEMPL_P2 = os.path.join('./mercedes_cli/docs/Data Input CLI Phases 2 and 3_2019_orig.xlsm')

# Дата-мэп ребусовских файлов к клиентскому шаблону
REBUS_TO_HQ_P1 = {
    'sys_RespNum': 'Respondent_Serial', 'VIN': 'HIDDEN_ VIN', 'Current Dealership_name': 'gssn_code',
    'Current Dealership_outlet_number': 'gssn_label', 'CLI01': 'Q_CLI01', 'CLI02': 'Q_CLI02', 'CLI03': 'Q_CLI03',
    'CLI04': 'Q_CLI04', 'EV01_1 ': 'Q_EV01_1', 'EV01_2': 'Q_EV01_2', 'EV01_3': 'Q_EV01_3', 'EV01_4': 'Q_EV01_4',
    'TD01': 'Q_TD01', 'TD04': 'Q_TD04', 'VD01': 'Q_VD01', 'SF01': 'v157', 'SF02': 'Q_SF02'
}
REBUS_TO_HQ_P2 = {
    'sys_RespNum': 'Respondent_Serial', 'VIN': 'HIDDEN_ VIN', 'Current Dealership_name': 'gssn_code',
    'Current Dealership_outlet_number': 'gssn_label', 'Phase': 'HIDDEN_phase', 'CLI01': 'Q_CLI01', 'CLI02': 'Q_CLI02',
    'CLI03': 'Q_CLI03', 'CLI04': 'Q_CLI04', 'CS1': 'Q_CS1', 'CS2_1': 'Q_CS2_1', 'CS2_2': 'Q_CS2_2', 'CS2_3': 'Q_CS2_3',
    'CS2_4': 'Q_CS2_4', 'CS4_1': 'Q_CS4_1', 'CS4_2': 'Q_CS4_2', 'CS4_3': 'Q_CS4_3', 'CS4_4': 'Q_CS4_4', 'RM2': 'v183',
    'CS3': 'Q_CS3'
}

# малтипл вопроосы длля перекодировки
MULTIPLE_QUESTIONS = ('EV00_1', 'EV00_2', 'EV00_3', 'EV00_4', 'EV00_5', 'EV00_6', 'EV00_7', 'EV00_8', 'EV00_9',
                      'EV00_10', 'TD03_1', 'TD03_2', 'TD03_3', 'TD03_4', 'TD03_5', 'TD03_6', 'TD03_7', 'TD03_8',
                      'RM3_1', 'RM3_2', 'RM3_3', 'RM3_4', 'RM3_5', 'RM3_6', 'SB3_1', 'SB3_2', 'SB3_3', 'SB3_4', 'SB3_5',
                      'SB3_6'
)