import os

from sv.settings import MEDIA_ROOT

TOUCH_POINTS = (
    (1, 'anonymous'),
)
RTK_REGIONS = (
    ('1', 'anonymous'),
)

COMPL_PROCESSING = (
    ('anonymous', 'anonymous'),
)

COMPL_RESULT = (
    ('anonymous', 'anonymous'),
)

STATE = (
    ('anonymous', 'anonymous'),
)

AUDIO_UPLOAD_RTK = os.path.join(MEDIA_ROOT, './media/rtk/audio/')
