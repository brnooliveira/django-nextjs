from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .filters import JobFilter
from .models import Job
from .serializers import JobSerializer


@api_view(['GET'])
def get_all_jobs(request):
    filter = JobFilter(request.GET, queryset=Job.objects.all().order_by('id'))
    count = filter.qs.count()
    paginator = PageNumberPagination()
    paginator.page_size = 2
    queryset = paginator.paginate_queryset(filter.qs, request)
    serializer = JobSerializer(queryset, many=True)
    return Response({
        'jobs': serializer.data,
        'paginator': 2,
        'count': count
    })


@api_view(['GET'])
def get_one_job(request, pk):
    job = get_object_or_404(Job, id=pk)
    serializer = JobSerializer(job, many=False)

    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_job(request):
    request.data['user'] = request.user
    data = request.data
    job = Job.objects.create(**data)
    serializer = JobSerializer(job, many=False)

    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_job(request, pk):
    job = get_object_or_404(Job, id=pk)

    if job.user != request.user:
        return Response(
            {
                'message': 'You can not update this job!'
            },
            status=status.HTTP_403_FORBIDDEN
        )
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
    if job.user != request.user:
        return Response(
            {
                'message': 'You can not update this job!'
            },
            status=status.HTTP_403_FORBIDDEN
        )
    job.delete()

    return Response({'message': 'Job is deleted.'}, status=status.HTTP_200_OK)
