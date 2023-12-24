from django.shortcuts import get_object_or_404
from job.filters import JobFilter
from job.models import Job
from job.serializers import JobSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


@api_view(['GET'])
def getAllJobs(request):
    filterset = JobFilter(request.GET, queryset=Job.objects.all().order_by('id'))
    count = filterset.qs.count()
    paginator = PageNumberPagination()
    paginator.page_size = 2
    queryset = paginator.paginate_queryset(filterset.qs, request)
    serializer = JobSerializer(queryset, many=True)
    return Response({
        'jobs': serializer.data,
        'paginator': 2,
        'count': count
    })


@api_view(['GET'])
def getOneJob(request, pk):
    job = get_object_or_404(Job, id=pk)
    serializer = JobSerializer(job, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def createJob(request):
    data = request.data
    job = Job.objects.create(**data)
    serializer = JobSerializer(job, many=False)

    return Response(serializer.data)


@api_view(['PUT'])
def updateJob(request, pk):
    job = get_object_or_404(Job, id=pk)
    job.description = request.data['description']
    job.email = request.data['email']
    job.address = request.data['address']
    job.job_type = request.data['job_type']
    job.education = request.data['education']
    job.industry = request.data['industry']
    job.experience = request.data['experience']
    job.salary = request.data['salary']
    job.positions = request.data['positions']
    job.company = request.data['company']

    job.save()

    serializer = JobSerializer(job, many=False)

    return Response(serializer.data)


@api_view(['DELETE'])
def delete_job(request, pk):
    job = get_object_or_404(Job, id=pk)
    job.delete()

    return Response({'message': 'Job is deleted.'}, status=status.HTTP_200_OK)
