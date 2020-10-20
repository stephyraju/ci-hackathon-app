from django.shortcuts import render
   
def teaminfo(request):
    """ Display the team name and list of members. """

    return render(request, "teaminfo.html")
