from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "This command tells me that we loves me"

    def add_arguments(self, parser):
        parser.add_argument(
            "--times", help="how many times",
        )

    def handle(self, *args, **options):
        # print(args, options)
        # print("i love you")
        times = options.get("times")

        for t in range(0, int(times)):
            # print("i love you")
            # self.stdout.write(self.style.SUCCESS("I LOVE YOU"))
            self.stdout.write(self.style.WARNING("I LOVE YOU"))
            # self.stdout.write(self.style.SUCCESS("I LOVE YOU"))
