from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """

    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        # append a group for "Administration" & "Applications"
        if context['request'].user.username == 'admin':
            cust_exclude = ('django.contrib.*',)
        else:
            cust_exclude = ('django.contrib.*', 'arrangement.*')

        print(cust_exclude)
        self.children.append(modules.Group(
            _('Group: Administration & Applications'),
            column=1,
            collapsible=True,
            children = [
                modules.AppList(
                    _('Administration'),
                    column=1,
                    collapsible=False,
                    models=('django.contrib.*',),
                ),
                modules.AppList(
                    _('Applications'),
                    column=1,
                    css_classes=('collapse closed',),
                    exclude=cust_exclude,
                )
            ]
        ))
        groups = [group.name for group in context['request'].user.groups.all()]
        if 'ipsos' in groups:
            self.children.append(modules.LinkList(
                title='Личный кабинет',
                column=3,
                children=(
                    {
                        'title': 'Статусы интервью (Статистика использования базы)',
                        'url': '/cabinet/dialing_sample',
                        'description': 'Стасистика использования базы',
                    },
                    {
                        'title': 'Статусы звонков (Статистика дозвона)',
                        'url': '/cabinet/dialing_contact_log',
                        'description': 'Стасистика обзвона',
                    },
                    {
                        'title': 'Квоты (Стратификация)',
                        'url': '/cabinet/stratification',
                        'description': 'Квоты (Стратификация)',
                    },
                    {
                        'title': 'Мониторинг работы интервьюеров',
                        'url': '/cabinet/fieldwork_control',
                        'description': 'Мониторинг работы интервьюеров',
                    },
                    {
                        'title': 'Справка',
                        'url': '/cabinet/help',
                        'description': 'Справка',
                    },
                    {
                        'title': 'Оставить обратную связь',
                        'url': 'arrangement/feedback/add/',
                        'description': 'Оставить обратную связь',
                    },
                )
            ))

