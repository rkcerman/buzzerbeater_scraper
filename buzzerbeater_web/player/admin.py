from django.contrib import admin

from .models import Boxscores, BoxscoreStats, Matches, PlayByPlays, Shots, Teams, PlayerSkills, Players

admin.site.register(Players)
admin.site.register(Boxscores)
admin.site.register(BoxscoreStats)
admin.site.register(Matches)
admin.site.register(PlayByPlays)
admin.site.register(Shots)
admin.site.register(Teams)
admin.site.register(PlayerSkills)
