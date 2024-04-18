from django.apps import AppConfig


class StockGameConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Stock_Game'
    def ready(self):
        from scheduler import scheduler
        # scheduler.start()
# class schedulerConfig(AppConfig):
#         name = 'scheduler'
#         def ready(self):
#             from scheduler import scheduler
#             scheduler.start()