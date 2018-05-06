# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand

from worker import sched


class Command(BaseCommand):
    help = 'run sched'

    def handle(self, *args, **options):
        sched.run()
