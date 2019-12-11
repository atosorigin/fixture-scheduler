from django.shortcuts import render
from django.http import HttpResponse
#from .models import Solution
from django.views.generic import TemplateView
from array import *
from main.models import League, Run

def homepage(request):
    return render(request = request,
                    template_name="main/home.html",
                    context={})

def search(request, page=1, filter=0):
    if page==2:
        runs=Run.runs.filter(league=League.leagues.filter(id=filter)[0])
        print(runs)
        return render(request = request,
                        template_name="main/search.html", context={'page':'2', 'runs':runs})
    elif page==3:
        leagues=League.leagues.all()
        return render(request = request,
                        template_name="main/search.html", context={"page":'3', 'run':leagues})
    else:
        leagues=League.leagues.all()
        return render(request = request,
                        template_name="main/search.html", context={'page':'1', 'leagues':leagues})



def fixtures(request):
    return render(request,"main/fixtures.html")


def view2(request):
    answer = "seriea 3023 "
    
    all_solutions = ""# Solution.objects.filter(solution__exact=answer)
    #solutions_list = Solution.objects.all().distinct()
    teams = ["Juventus", "Inter Milan", "Lazio", "Cagliari", "Roma", "Atlanta", "Napoli", "Parma", "Verona", "Fiorentina", "Torino", "Milan", "Udinese", "Sassuolo", "Bologna", "Sampdoria", "Lecce", "Genoa", "SPAL", "Brescia"]
    logos = ['https://cdn.freebiesupply.com/images/large/2x/juventus-logo-png-transparent.png',
    'https://c7.uihere.com/files/149/536/895/inter-milan-football-serie-a-a-c-milan-uefa-champions-league-football.jpg',
    'https://upload.wikimedia.org/wikipedia/en/thumb/e/e4/SS_Lazio.svg/1200px-SS_Lazio.svg.png',
    'https://upload.wikimedia.org/wikipedia/en/thumb/6/61/Cagliari_Calcio_1920.svg/1200px-Cagliari_Calcio_1920.svg.png',
    'https://upload.wikimedia.org/wikipedia/en/thumb/f/f7/AS_Roma_logo_%282017%29.svg/180px-AS_Roma_logo_%282017%29.svg.png',
    'https://upload.wikimedia.org/wikipedia/en/thumb/6/66/AtalantaBC.svg/1200px-AtalantaBC.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/S.S.C._Napoli_logo.svg/240px-S.S.C._Napoli_logo.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/4/4a/ParmaCalcio1913_logo-400x400.png',
    'https://upload.wikimedia.org/wikipedia/en/thumb/c/cc/Hellas_Verona_FC_logo.svg/1200px-Hellas_Verona_FC_logo.svg.png',
    'https://www.logofootball.net/wp-content/uploads/AC-Fiorentina-HD-Logo-750x750.png',
    'https://upload.wikimedia.org/wikipedia/en/thumb/2/2e/Torino_FC_Logo.svg/1200px-Torino_FC_Logo.svg.png',
    'https://cdn.freebiesupply.com/logos/large/2x/ac-milan-logo-png-transparent.png',
    'https://upload.wikimedia.org/wikipedia/en/f/f2/Udinese_calcio.png',
    'https://upload.wikimedia.org/wikipedia/ro/thumb/a/a3/US_Sassuolo_Calcio.svg/1200px-US_Sassuolo_Calcio.svg.png',
    'https://upload.wikimedia.org/wikipedia/en/d/db/Bologna_F.C._1909_logo.png',
    'https://upload.wikimedia.org/wikipedia/en/thumb/d/d2/U.C._Sampdoria_logo.svg/1200px-U.C._Sampdoria_logo.svg.png',
    'https://upload.wikimedia.org/wikipedia/it/a/a0/Leccestemma.png',
    'https://upload.wikimedia.org/wikipedia/ro/thumb/7/76/Genoa_CFC.svg/1200px-Genoa_CFC.svg.png',
    'https://upload.wikimedia.org/wikipedia/en/thumb/3/3c/Spal2013_logo.svg/1200px-Spal2013_logo.svg.png',
    'https://upload.wikimedia.org/wikipedia/fr/9/94/Brescia_Calcio_logo.png']
    
    active_team = ""
    weeks = ["week01", "week02", "week03", "week04", "week05", "week06", "week07", "week08", "week09", "week10", "week11", "week12", "week13", "week14", "week15", "week16", "week17", "week18", "week19", "week20", "week21", "week22", "week23", "week24", "week25", "week26", "week27", "week28", "week29", "week30", "week31", "week32", "week33", "week34", "week35", "week36", "week37", "week38"]

    home_teams = []
    away_teams = []
    urls = []
    existing_teams = []

    score = 100
    explain = []
 

    for x in range(0, len(all_solutions)):
        active_team = teams[all_solutions[x].team - 1]
        checker = 1

        for y in range(0, len(existing_teams)):
            if active_team == existing_teams[y]:
                checker = 0

        if checker == 1:
            if all_solutions[x].week01 > 0:
                home_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                temp = all_solutions[x].week01 - 1
                away_teams.append(teams[temp])
                urls.append(logos[temp])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])

                if active_team == "Bologna":
                    score = score - 23
                    explain.append("DATE REQUEST CONFLICT : Bologna playing at home 25/08/2019 (Week 01)")
                if active_team == "Brescia":
                    score = score - 23
                    explain.append("DATE REQUEST CONFLICT : Brescia playing at home 25/08/2019 (Week 01)")
                if active_team == "Lecce":
                    score = score - 23
                    explain.append("DATE REQUEST CONFLICT : Lecce playing at home 25/08/2019 (Week 01)")

            else:
                temp = (all_solutions[x].week01 + 1) * -1
                home_teams.append(teams[temp])
                urls.append(logos[temp])

                away_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])

                if teams[temp] == "Bologna":
                    score = score - 23
                    explain.append("DATE REQUEST CONFLICT : Bologna playing at home 25/08/2019 (Week 01)")
                if teams[temp] == "Brescia":
                    score = score - 23
                    explain.append("DATE REQUEST CONFLICT : Brescia playing at home 25/08/2019 (Week 01)")
                if teams[temp] == "Lecce":
                    score = score - 23
                    explain.append("DATE REQUEST CONFLICT : Lecce playing at home 25/08/2019 (Week 01)")
    
    existing_teams = []

    for x in range(0, len(all_solutions)):
        active_team = teams[all_solutions[x].team - 1]
        checker = 1

        for y in range(0, len(existing_teams)):
            if active_team == existing_teams[y]:
                checker = 0

        if checker == 1:
            if all_solutions[x].week02 > 0:
                home_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                temp = all_solutions[x].week02 - 1
                away_teams.append(teams[temp])
                urls.append(logos[temp])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])

                if active_team == "Brescia":
                    score = score - 23
                    explain.append("DATE REQUEST CONFLICT : Brescia playing at home 01/09/2019 (Week 02)")
            else:
                temp = (all_solutions[x].week02 + 1) * -1
                home_teams.append(teams[temp])
                urls.append(logos[temp])

                away_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])

                if teams[temp] == "Brescia":
                    score = score - 23
                    explain.append("DATE REQUEST CONFLICT : Brescia playing at home 01/09/2019 (Week 02)")
    
    existing_teams = []

    for x in range(0, len(all_solutions)):
        active_team = teams[all_solutions[x].team - 1]
        checker = 1

        for y in range(0, len(existing_teams)):
            if active_team == existing_teams[y]:
                checker = 0

        if checker == 1:
            if all_solutions[x].week03 > 0:
                home_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                temp = all_solutions[x].week03 - 1
                away_teams.append(teams[temp])
                urls.append(logos[temp])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
            else:
                temp = (all_solutions[x].week03 + 1) * -1
                home_teams.append(teams[temp])
                urls.append(logos[temp])

                away_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
    
    existing_teams = []

    
    for x in range(0, len(all_solutions)):
        active_team = teams[all_solutions[x].team - 1]
        checker = 1

        for y in range(0, len(existing_teams)):
            if active_team == existing_teams[y]:
                checker = 0

        if checker == 1:
            if all_solutions[x].week04 > 0:
                home_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                temp = all_solutions[x].week04 - 1
                away_teams.append(teams[temp])
                urls.append(logos[temp])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
            else:
                temp = (all_solutions[x].week04 + 1) * -1
                home_teams.append(teams[temp])
                urls.append(logos[temp])

                away_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
    
    existing_teams = []
    
    for x in range(0, len(all_solutions)):
        active_team = teams[all_solutions[x].team - 1]
        checker = 1

        for y in range(0, len(existing_teams)):
            if active_team == existing_teams[y]:
                checker = 0

        if checker == 1:
            if all_solutions[x].week05 > 0:
                home_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                temp = all_solutions[x].week05 - 1
                away_teams.append(teams[temp])
                urls.append(logos[temp])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
            else:
                temp = (all_solutions[x].week05 + 1) * -1
                home_teams.append(teams[temp])
                urls.append(logos[temp])

                away_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
    
    existing_teams = []

    for x in range(0, len(all_solutions)):
        active_team = teams[all_solutions[x].team - 1]
        checker = 1

        for y in range(0, len(existing_teams)):
            if active_team == existing_teams[y]:
                checker = 0

        if checker == 1:
            if all_solutions[x].week06 > 0:
                home_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                temp = all_solutions[x].week06 - 1
                away_teams.append(teams[temp])
                urls.append(logos[temp])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
            else:
                temp = (all_solutions[x].week06 + 1) * -1
                home_teams.append(teams[temp])
                urls.append(logos[temp])

                away_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
    
    existing_teams = []

    for x in range(0, len(all_solutions)):
        active_team = teams[all_solutions[x].team - 1]
        checker = 1

        for y in range(0, len(existing_teams)):
            if active_team == existing_teams[y]:
                checker = 0

        if checker == 1:
            if all_solutions[x].week07 > 0:
                home_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                temp = all_solutions[x].week07 - 1
                away_teams.append(teams[temp])
                urls.append(logos[temp])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
            else:
                temp = (all_solutions[x].week07 + 1) * -1
                home_teams.append(teams[temp])
                urls.append(logos[temp])

                away_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
    
    existing_teams = []

    for x in range(0, len(all_solutions)):
        active_team = teams[all_solutions[x].team - 1]
        checker = 1

        for y in range(0, len(existing_teams)):
            if active_team == existing_teams[y]:
                checker = 0

        if checker == 1:
            if all_solutions[x].week08 > 0:
                home_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                temp = all_solutions[x].week08 - 1
                away_teams.append(teams[temp])
                urls.append(logos[temp])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
            else:
                temp = (all_solutions[x].week08 + 1) * -1
                home_teams.append(teams[temp])
                urls.append(logos[temp])

                away_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
    
    existing_teams = []


    for x in range(0, len(all_solutions)):
        active_team = teams[all_solutions[x].team - 1]
        checker = 1

        for y in range(0, len(existing_teams)):
            if active_team == existing_teams[y]:
                checker = 0

        if checker == 1:
            if all_solutions[x].week09 > 0:
                home_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                temp = all_solutions[x].week09 - 1
                away_teams.append(teams[temp])
                urls.append(logos[temp])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
            else:
                temp = (all_solutions[x].week09 + 1) * -1
                home_teams.append(teams[temp])
                urls.append(logos[temp])

                away_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
    
    existing_teams = []


    for x in range(0, len(all_solutions)):
        active_team = teams[all_solutions[x].team - 1]
        checker = 1

        for y in range(0, len(existing_teams)):
            if active_team == existing_teams[y]:
                checker = 0

        if checker == 1:
            if all_solutions[x].week10 > 0:
                home_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                temp = all_solutions[x].week10 - 1
                away_teams.append(teams[temp])
                urls.append(logos[temp])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
            else:
                temp = (all_solutions[x].week10 + 1) * -1
                home_teams.append(teams[temp])
                urls.append(logos[temp])

                away_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
    
    existing_teams = []

    for x in range(0, len(all_solutions)):
        active_team = teams[all_solutions[x].team - 1]
        checker = 1

        for y in range(0, len(existing_teams)):
            if active_team == existing_teams[y]:
                checker = 0

        if checker == 1:
            if all_solutions[x].week11 > 0:
                home_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                temp = all_solutions[x].week11 - 1
                away_teams.append(teams[temp])
                urls.append(logos[temp])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
            else:
                temp = (all_solutions[x].week11 + 1) * -1
                home_teams.append(teams[temp])
                urls.append(logos[temp])

                away_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
    
    existing_teams = []

    for x in range(0, len(all_solutions)):
        active_team = teams[all_solutions[x].team - 1]
        checker = 1

        for y in range(0, len(existing_teams)):
            if active_team == existing_teams[y]:
                checker = 0

        if checker == 1:
            if all_solutions[x].week12 > 0:
                home_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                temp = all_solutions[x].week12 - 1
                away_teams.append(teams[temp])
                urls.append(logos[temp])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
            else:
                temp = (all_solutions[x].week12 + 1) * -1
                home_teams.append(teams[temp])
                urls.append(logos[temp])

                away_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
    
    existing_teams = []

    for x in range(0, len(all_solutions)):
        active_team = teams[all_solutions[x].team - 1]
        checker = 1

        for y in range(0, len(existing_teams)):
            if active_team == existing_teams[y]:
                checker = 0

        if checker == 1:
            if all_solutions[x].week13 > 0:
                home_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                temp = all_solutions[x].week13 - 1
                away_teams.append(teams[temp])
                urls.append(logos[temp])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
            else:
                temp = (all_solutions[x].week13 + 1) * -1
                home_teams.append(teams[temp])
                urls.append(logos[temp])

                away_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
    
    existing_teams = []

    for x in range(0, len(all_solutions)):
        active_team = teams[all_solutions[x].team - 1]
        checker = 1

        for y in range(0, len(existing_teams)):
            if active_team == existing_teams[y]:
                checker = 0

        if checker == 1:
            if all_solutions[x].week14 > 0:
                home_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                temp = all_solutions[x].week14 - 1
                away_teams.append(teams[temp])
                urls.append(logos[temp])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
            else:
                temp = (all_solutions[x].week14 + 1) * -1
                home_teams.append(teams[temp])
                urls.append(logos[temp])

                away_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
    
    existing_teams = []

    for x in range(0, len(all_solutions)):
        active_team = teams[all_solutions[x].team - 1]
        checker = 1

        for y in range(0, len(existing_teams)):
            if active_team == existing_teams[y]:
                checker = 0

        if checker == 1:
            if all_solutions[x].week15 > 0:
                home_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                temp = all_solutions[x].week15 - 1
                away_teams.append(teams[temp])
                urls.append(logos[temp])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
            else:
                temp = (all_solutions[x].week15 + 1) * -1
                home_teams.append(teams[temp])
                urls.append(logos[temp])

                away_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
    
    existing_teams = []

    for x in range(0, len(all_solutions)):
        active_team = teams[all_solutions[x].team - 1]
        checker = 1

        for y in range(0, len(existing_teams)):
            if active_team == existing_teams[y]:
                checker = 0

        if checker == 1:
            if all_solutions[x].week16 > 0:
                home_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                temp = all_solutions[x].week16 - 1
                away_teams.append(teams[temp])
                urls.append(logos[temp])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
            else:
                temp = (all_solutions[x].week16 + 1) * -1
                home_teams.append(teams[temp])
                urls.append(logos[temp])

                away_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
    
    existing_teams = []

    for x in range(0, len(all_solutions)):
        active_team = teams[all_solutions[x].team - 1]
        checker = 1

        for y in range(0, len(existing_teams)):
            if active_team == existing_teams[y]:
                checker = 0

        if checker == 1:
            if all_solutions[x].week17 > 0:
                home_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                temp = all_solutions[x].week17 - 1
                away_teams.append(teams[temp])
                urls.append(logos[temp])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
            else:
                temp = (all_solutions[x].week17 + 1) * -1
                home_teams.append(teams[temp])
                urls.append(logos[temp])

                away_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
    
    existing_teams = []
    
    for x in range(0, len(all_solutions)):
        active_team = teams[all_solutions[x].team - 1]
        checker = 1

        for y in range(0, len(existing_teams)):
            if active_team == existing_teams[y]:
                checker = 0

        if checker == 1:
            if all_solutions[x].week18 > 0:
                home_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                temp = all_solutions[x].week18 - 1
                away_teams.append(teams[temp])
                urls.append(logos[temp])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
            else:
                temp = (all_solutions[x].week18 + 1) * -1
                home_teams.append(teams[temp])
                urls.append(logos[temp])

                away_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
    
    existing_teams = []

    for x in range(0, len(all_solutions)):
        active_team = teams[all_solutions[x].team - 1]
        checker = 1

        for y in range(0, len(existing_teams)):
            if active_team == existing_teams[y]:
                checker = 0

        if checker == 1:
            if all_solutions[x].week19 > 0:
                home_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                temp = all_solutions[x].week19 - 1
                away_teams.append(teams[temp])
                urls.append(logos[temp])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
            else:
                temp = (all_solutions[x].week19 + 1) * -1
                home_teams.append(teams[temp])
                urls.append(logos[temp])

                away_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
    
    existing_teams = []

    for x in range(0, len(all_solutions)):
        active_team = teams[all_solutions[x].team - 1]
        checker = 1

        for y in range(0, len(existing_teams)):
            if active_team == existing_teams[y]:
                checker = 0

        if checker == 1:
            if all_solutions[x].week20 > 0:
                home_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                temp = all_solutions[x].week20 - 1
                away_teams.append(teams[temp])
                urls.append(logos[temp])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
            else:
                temp = (all_solutions[x].week20 + 1) * -1
                home_teams.append(teams[temp])
                urls.append(logos[temp])

                away_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
    
    existing_teams = []

    for x in range(0, len(all_solutions)):
        active_team = teams[all_solutions[x].team - 1]
        checker = 1

        for y in range(0, len(existing_teams)):
            if active_team == existing_teams[y]:
                checker = 0

        if checker == 1:
            if all_solutions[x].week21 > 0:
                home_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                temp = all_solutions[x].week21 - 1
                away_teams.append(teams[temp])
                urls.append(logos[temp])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
            else:
                temp = (all_solutions[x].week21 + 1) * -1
                home_teams.append(teams[temp])
                urls.append(logos[temp])

                away_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
    
    existing_teams = []


    for x in range(0, len(all_solutions)):
        active_team = teams[all_solutions[x].team - 1]
        checker = 1

        for y in range(0, len(existing_teams)):
            if active_team == existing_teams[y]:
                checker = 0

        if checker == 1:
            if all_solutions[x].week22 > 0:
                home_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                temp = all_solutions[x].week22 - 1
                away_teams.append(teams[temp])
                urls.append(logos[temp])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
            else:
                temp = (all_solutions[x].week22 + 1) * -1
                home_teams.append(teams[temp])
                urls.append(logos[temp])

                away_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
    
    existing_teams = []


    for x in range(0, len(all_solutions)):
        active_team = teams[all_solutions[x].team - 1]
        checker = 1

        for y in range(0, len(existing_teams)):
            if active_team == existing_teams[y]:
                checker = 0

        if checker == 1:
            if all_solutions[x].week23 > 0:
                home_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                temp = all_solutions[x].week23 - 1
                away_teams.append(teams[temp])
                urls.append(logos[temp])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
            else:
                temp = (all_solutions[x].week23 + 1) * -1
                home_teams.append(teams[temp])
                urls.append(logos[temp])

                away_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
    
    existing_teams = []

    for x in range(0, len(all_solutions)):
        active_team = teams[all_solutions[x].team - 1]
        checker = 1

        for y in range(0, len(existing_teams)):
            if active_team == existing_teams[y]:
                checker = 0

        if checker == 1:
            if all_solutions[x].week24 > 0:
                home_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                temp = all_solutions[x].week24 - 1
                away_teams.append(teams[temp])
                urls.append(logos[temp])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
            else:
                temp = (all_solutions[x].week24 + 1) * -1
                home_teams.append(teams[temp])
                urls.append(logos[temp])

                away_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
    
    existing_teams = []

    for x in range(0, len(all_solutions)):
        active_team = teams[all_solutions[x].team - 1]
        checker = 1

        for y in range(0, len(existing_teams)):
            if active_team == existing_teams[y]:
                checker = 0

        if checker == 1:
            if all_solutions[x].week25 > 0:
                home_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                temp = all_solutions[x].week25 - 1
                away_teams.append(teams[temp])
                urls.append(logos[temp])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
            else:
                temp = (all_solutions[x].week25 + 1) * -1
                home_teams.append(teams[temp])
                urls.append(logos[temp])

                away_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
    
    existing_teams = []

    for x in range(0, len(all_solutions)):
        active_team = teams[all_solutions[x].team - 1]
        checker = 1

        for y in range(0, len(existing_teams)):
            if active_team == existing_teams[y]:
                checker = 0

        if checker == 1:
            if all_solutions[x].week26 > 0:
                home_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                temp = all_solutions[x].week26 - 1
                away_teams.append(teams[temp])
                urls.append(logos[temp])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
            else:
                temp = (all_solutions[x].week26 + 1) * -1
                home_teams.append(teams[temp])
                urls.append(logos[temp])

                away_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
    
    existing_teams = []

    for x in range(0, len(all_solutions)):
        active_team = teams[all_solutions[x].team - 1]
        checker = 1

        for y in range(0, len(existing_teams)):
            if active_team == existing_teams[y]:
                checker = 0

        if checker == 1:
            if all_solutions[x].week27 > 0:
                home_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                temp = all_solutions[x].week27 - 1
                away_teams.append(teams[temp])
                urls.append(logos[temp])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
            else:
                temp = (all_solutions[x].week27 + 1) * -1
                home_teams.append(teams[temp])
                urls.append(logos[temp])

                away_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
    
    existing_teams = []

    for x in range(0, len(all_solutions)):
        active_team = teams[all_solutions[x].team - 1]
        checker = 1

        for y in range(0, len(existing_teams)):
            if active_team == existing_teams[y]:
                checker = 0

        if checker == 1:
            if all_solutions[x].week28 > 0:
                home_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                temp = all_solutions[x].week28 - 1
                away_teams.append(teams[temp])
                urls.append(logos[temp])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
            else:
                temp = (all_solutions[x].week28 + 1) * -1
                home_teams.append(teams[temp])
                urls.append(logos[temp])

                away_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
    
    existing_teams = []

    for x in range(0, len(all_solutions)):
        active_team = teams[all_solutions[x].team - 1]
        checker = 1

        for y in range(0, len(existing_teams)):
            if active_team == existing_teams[y]:
                checker = 0

        if checker == 1:
            if all_solutions[x].week29 > 0:
                home_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                temp = all_solutions[x].week29 - 1
                away_teams.append(teams[temp])
                urls.append(logos[temp])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
            else:
                temp = (all_solutions[x].week29 + 1) * -1
                home_teams.append(teams[temp])
                urls.append(logos[temp])

                away_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
    
    existing_teams = []

    for x in range(0, len(all_solutions)):
        active_team = teams[all_solutions[x].team - 1]
        checker = 1

        for y in range(0, len(existing_teams)):
            if active_team == existing_teams[y]:
                checker = 0

        if checker == 1:
            if all_solutions[x].week30 > 0:
                home_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                temp = all_solutions[x].week30 - 1
                away_teams.append(teams[temp])
                urls.append(logos[temp])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
            else:
                temp = (all_solutions[x].week30 + 1) * -1
                home_teams.append(teams[temp])
                urls.append(logos[temp])

                away_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
    
    existing_teams = []

    for x in range(0, len(all_solutions)):
        active_team = teams[all_solutions[x].team - 1]
        checker = 1

        for y in range(0, len(existing_teams)):
            if active_team == existing_teams[y]:
                checker = 0

        if checker == 1:
            if all_solutions[x].week31 > 0:
                home_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                temp = all_solutions[x].week31 - 1
                away_teams.append(teams[temp])
                urls.append(logos[temp])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
            else:
                temp = (all_solutions[x].week31 + 1) * -1
                home_teams.append(teams[temp])
                urls.append(logos[temp])

                away_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
    
    existing_teams = []

    for x in range(0, len(all_solutions)):
        active_team = teams[all_solutions[x].team - 1]
        checker = 1

        for y in range(0, len(existing_teams)):
            if active_team == existing_teams[y]:
                checker = 0

        if checker == 1:
            if all_solutions[x].week32 > 0:
                home_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                temp = all_solutions[x].week32 - 1
                away_teams.append(teams[temp])
                urls.append(logos[temp])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
            else:
                temp = (all_solutions[x].week32 + 1) * -1
                home_teams.append(teams[temp])
                urls.append(logos[temp])

                away_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
    
    existing_teams = []

    for x in range(0, len(all_solutions)):
        active_team = teams[all_solutions[x].team - 1]
        checker = 1

        for y in range(0, len(existing_teams)):
            if active_team == existing_teams[y]:
                checker = 0

        if checker == 1:
            if all_solutions[x].week33 > 0:
                home_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                temp = all_solutions[x].week33 - 1
                away_teams.append(teams[temp])
                urls.append(logos[temp])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
            else:
                temp = (all_solutions[x].week33 + 1) * -1
                home_teams.append(teams[temp])
                urls.append(logos[temp])

                away_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
    
    existing_teams = []

    for x in range(0, len(all_solutions)):
        active_team = teams[all_solutions[x].team - 1]
        checker = 1

        for y in range(0, len(existing_teams)):
            if active_team == existing_teams[y]:
                checker = 0

        if checker == 1:
            if all_solutions[x].week34 > 0:
                home_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                temp = all_solutions[x].week34 - 1
                away_teams.append(teams[temp])
                urls.append(logos[temp])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
            else:
                temp = (all_solutions[x].week34 + 1) * -1
                home_teams.append(teams[temp])
                urls.append(logos[temp])

                away_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
    
    existing_teams = []

    for x in range(0, len(all_solutions)):
        active_team = teams[all_solutions[x].team - 1]
        checker = 1

        for y in range(0, len(existing_teams)):
            if active_team == existing_teams[y]:
                checker = 0

        if checker == 1:
            if all_solutions[x].week35 > 0:
                home_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                temp = all_solutions[x].week35 - 1
                away_teams.append(teams[temp])
                urls.append(logos[temp])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
            else:
                temp = (all_solutions[x].week35 + 1) * -1
                home_teams.append(teams[temp])
                urls.append(logos[temp])

                away_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
    
    existing_teams = []

    for x in range(0, len(all_solutions)):
        active_team = teams[all_solutions[x].team - 1]
        checker = 1

        for y in range(0, len(existing_teams)):
            if active_team == existing_teams[y]:
                checker = 0

        if checker == 1:
            if all_solutions[x].week36 > 0:
                home_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                temp = all_solutions[x].week36 - 1
                away_teams.append(teams[temp])
                urls.append(logos[temp])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
            else:
                temp = (all_solutions[x].week36 + 1) * -1
                home_teams.append(teams[temp])
                urls.append(logos[temp])

                away_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
    
    existing_teams = []

    for x in range(0, len(all_solutions)):
        active_team = teams[all_solutions[x].team - 1]
        checker = 1

        for y in range(0, len(existing_teams)):
            if active_team == existing_teams[y]:
                checker = 0

        if checker == 1:
            if all_solutions[x].week37 > 0:
                home_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                temp = all_solutions[x].week37 - 1
                away_teams.append(teams[temp])
                urls.append(logos[temp])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
            else:
                temp = (all_solutions[x].week37 + 1) * -1
                home_teams.append(teams[temp])
                urls.append(logos[temp])

                away_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
    
    existing_teams = []

    for x in range(0, len(all_solutions)):
        active_team = teams[all_solutions[x].team - 1]
        checker = 1

        for y in range(0, len(existing_teams)):
            if active_team == existing_teams[y]:
                checker = 0

        if checker == 1:
            if all_solutions[x].week38 > 0:
                home_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                temp = all_solutions[x].week38 - 1
                away_teams.append(teams[temp])
                urls.append(logos[temp])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
            else:
                temp = (all_solutions[x].week38 + 1) * -1
                home_teams.append(teams[temp])
                urls.append(logos[temp])

                away_teams.append(active_team)
                urls.append(logos[all_solutions[x].team - 1])

                existing_teams.append(active_team)
                existing_teams.append(teams[temp])
    
    existing_teams = []

    return render(request = request,
                    template_name="main/view2.html",
                    context={"tutorials":Tutorial.objects.all, "homegames": home_teams, "awaygames": away_teams, "urls": urls, "score": score, "explain": explain})


def fixtures(request):
    return render(request = request,
                    template_name="main/fixtures.html",
                    context={"tutorials":Tutorial.objects.all})

                    
def pairings(request):
    return render(request,"main/pairings.html")

def finalpairings(request):
    return render(request,"main/finalpairings.html")
    
def teamDateRequests(request):
    return render(request,"main/teamDateRequests.html")

def testing(request):
    return render(request,"main/testing.html")

    
