from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import NoteSerializer
from .models import Note


# Create your views here.

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def get_routes(request):
    routes = [
        {
            'Endpoint': '/notes',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note'
        },
        {
            'Endpoint': '/notes/create',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates a new note with data sent in the request body'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Updates a note with data sent in the request body'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)


@api_view(['GET'])
def get_notes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_note(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def create_note(request):
    data = request.data
    note = Note.objects.create(
        body=data['body']
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def update_note(request, pk):
    data = request.data
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_note(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('Note was deleted')
