class NipoRouter:
    """
    A router to control all database operations on models in the nipo.
    """
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'nipo_db':
            return 'nipo'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'nipo_db':
            return 'nipo'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'nipo_db' or \
           obj2._meta.app_label == 'nipo_db':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'nipo_db':
            return db == 'nipo'
        return None
