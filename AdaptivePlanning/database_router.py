from django.conf import settings

class DatabaseAppsRouter(object):
     def db_for_read(self,model, **hints):
        if model._meta.app_label == 'AdaptivePlanning':
            return 'train'
        return None
     def db_for_write(self,model, **hints):
        if model._meta.app_label == 'AdaptivePlanning':
            return 'train'
        return None
     def allow_relation(self,obj1, obj2, **hints):
        if obj1._meta.app_label == 'AdaptivePlanning' and \
           obj2._meta.app_label == 'AdaptivePlanning':
           return True
        return None
     def allow_syncdb(self,db, model):       
        if db == 'train':
            if model._meta.app_label == 'AdaptivePlanning':
                return True
        elif model._meta.app_label == 'AdaptivePlanning':
            return False
        return None
