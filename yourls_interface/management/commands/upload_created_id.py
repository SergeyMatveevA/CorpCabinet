from django.core.management import BaseCommand

from yourls.models import YourlsUrl, Yourls2Url
from yourls_interface.models import YourlsID


class Command(BaseCommand):
    """Записать в базу уже созданные в yourls id"""

    def handle(self, *args, **options):
        mbr_links = YourlsUrl.objects.all()
        created_ids = [YourlsID(yourls_id=link.keyword, use_in_mbr_engine=True) for link in mbr_links]
        general_links = Yourls2Url.objects.all()
        common_ids = list(set([link.keyword for link in mbr_links]) & set([link.keyword for link in general_links]))
        for link in general_links:
            if link.keyword not in common_ids:
                created_ids.append(YourlsID(yourls_id=link.keyword, use_in_general_engine=True))
        YourlsID.objects.bulk_create(created_ids)
        YourlsID.objects.filter(yourls_id__in=common_ids).update(use_in_general_engine=True, id_type=2)
