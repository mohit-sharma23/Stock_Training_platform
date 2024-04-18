from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from django.utils import timezone
from django_apscheduler.models import DjangoJobExecution
from django.conf import settings
import logging
from yahoo_fin import stock_info
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from Stock_Game.models import Ratings,Buy,Stock,Join,Room
import sys


logger = logging.getLogger(__name__)

def my_job():
  #  print(" from my job")
  #  allrooms=Room.objects.all()
   allrooms=Room.objects.filter(id=1)
   for room in allrooms:
      allplayers=Join.objects.filter(room=room)
      #  print(allplayers)
      k=[]
      for player in allplayers:
        p=[]
        buy1 = Buy.objects.filter(reg_user_id=player.reg_user_id).filter(reg_room_id=player.room)
        # print(buy1)
        sum = player.user_money
        k2 = -99999
        # print(len(buy1))
        p1="Not bought yet"
        if(len(buy1)>0):
            for j in buy1:
                # print(player.reg_user_id.user.username)
                quote = stock_info.get_live_price(j.reg_stock_id.nse_code + ".NS")
                if k2 < quote * j.no_of_shares:
                    p1 = j.reg_stock_id.stock_name
                sum += (quote * j.no_of_shares)
        if(p1 !='Not bought yet'):
          p.append(player)
          p.append(int(sum))
          # print(p1)
          p.append(p1)
          # print(p)
          k.append(p)
      k.sort(key=lambda x: x[1], reverse=True)
      p2 = []
      k3 = 1
      for i in k:
          h1 = dict()
          h1['rank'] = k3
          h1['name'] = i[0]
          h1['sum'] = i[1]
          h1['Stock'] = i[2]
          user=i
          print(user)
          p2.append(h1)
          rating=Ratings.objects.filter(reg_user_id=i[0].reg_user_id).filter(reg_room_id=room)
          if(len(rating)>0):
            rating=Ratings(reg_user_id=i[0].reg_user_id,reg_room_id=room,ratings=k3,sum=i[1],top_stock=i[2])
            rating.save()
          else:
            rating.ratings=k3
            rating.sum=i[1]
            rating.top_stock=i[2]
            rating.save()
          k3+=1
      print(p2)
      pass



def deactivate_expired_accounts():
    # today = timezone.now().
    print("Hello")


# class Command(BaseCommand):
#   help = "Runs APScheduler."

#   def handle(self, *args, **options):
#     scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
#     scheduler.add_jobstore(DjangoJobStore(), "default")

#     scheduler.add_job(
#       my_job,
#       trigger=CronTrigger(second="*/10"),  # Every 10 seconds
#       id="my_job",  # The `id` assigned to each job MUST be unique
#       max_instances=1,
#       replace_existing=True,
#     )
#     logger.info("Added job 'my_job'.")

#     try:
#       logger.info("Starting scheduler...")
#       scheduler.start()
#     except KeyboardInterrupt:
#       logger.info("Stopping scheduler...")
#       scheduler.shutdown()
#       logger.info("Scheduler shut down successfully!")


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    # run this job every 24 hours
    scheduler.add_job(
      my_job,
      trigger=CronTrigger(second=20),  # Every 10 seconds
      id="my_job",  # The `id` assigned to each job MUST be unique
      max_instances=1,
      replace_existing=True,
    )
    logger.info("Added job 'my_job'.")    
    register_events(scheduler)
    scheduler.start()
    print("Scheduler started...", file=sys.stdout)