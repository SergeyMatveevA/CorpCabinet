class YourlsRouter:
    """
    A router to control all database operations on models in the auth yourls.
    """
    def db_for_read(self, model, **hints):
        if '2' in model._meta.label and model._meta.app_label == 'yourls':
            return 'yourls_general'
        elif model._meta.app_label == 'yourls':
            return 'yourls_mbr'
        return None

    def db_for_write(self, model, **hints):
        if '2' in model._meta.label and model._meta.app_label == 'yourls':
            return 'yourls_general'
        elif model._meta.app_label == 'yourls':
            return 'yourls_mbr'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'yourls' or obj2._meta.app_label == 'yourls':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'yourls' and '2' in model_name:
            return db == 'yourls_general'
        elif app_label == 'yourls':
            return db == 'yourls_mbr'
        return None

