import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
django.setup()

from app.models import Game, Genre

sandbox = Genre(title="Sandbox")
adventure = Genre(title="Adventure")
sandbox.save()
adventure.save()

sandbox = Genre.objects.get(id=1)
adventure = Genre.objects.get(id=2)

minecraft = Game(name="Minecraft", release_date="2008-08-20", rating=10.1)
minecraft.save()
minecraft.genres.add(sandbox)
minecraft.genres.add(adventure)
minecraft.save()


factorio = Game(name="Factorio", release_date="2008-08-20", rating=9.0)
factorio.save()
factorio.genres.add(sandbox)
factorio.save()

dead_cells = Game(name="Dead Cells", release_date="2008-08-20", rating=9.5)
dead_cells.save()
dead_cells.genres.add(adventure)
dead_cells.save()