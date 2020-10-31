from rest_framework import generics
from polls.models import Question
from .serializers import QuestionSerializer

class QuestionApiView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer