from django.shortcuts import render, redirect, get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Person
from .serializers import PersonSerializer
from .forms import PersonForm

# Create your views here.

def home(request):

    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PersonForm()

    people = Person.objects.all()
    form = PersonForm()

    context = {
        "people": people,
        "form": form,
    }

    return render(
        request, 
        "hello/home.html",
        context 
    )


def edit_person(request, id):
    person = Person.objects.get(id=id)
    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PersonForm(instance=person)

    context = {
        "form": form,
        "person": person,
    }
    return render(
        request, 
        "hello/edit_person.html",
        context)

def delete_person(request, id):
    person = Person.objects.get(id=id)
    if request.method == "POST":
        person.delete()
        return redirect("home")
    context = {
        "person": person,
    }
    return render(
        request, 
        "hello/delete_person.html",
        context)


@api_view(["GET", "POST"])
def peope_api(request):

    if request.method == "GET":
        
        people = Person.objects.all()

        serializer = PersonSerializer(
            people,
            many=True
        )
        return Response(serializer.data)

    if request.method == "POST":

        serializer = PersonSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
        )

@api_view(["GET", "PUT", "DELETE"])
def person_api(request, person_id):

    person = get_object_or_404(
        Person,
        id=person_id
    )

    if request.method == "GET":

        serializer = PersonSerializer(person)
        return Response(serializer.data)

    if request.method == "PUT":

        serializer = PersonSerializer(
            person,
            data=request.data
        )

        if serializer.is_valid:

            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    if request.method == "DELETE":

        person.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )

