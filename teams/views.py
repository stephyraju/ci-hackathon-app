from django.shortcuts import render
   
def view_all_teams(request):
    """ Display the team name and list of members. """

    return render(request, "allteams.html")
