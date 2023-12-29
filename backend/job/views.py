from datetime import timezone
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .filters import JobFilter
from .models import CandidateApplied, Job
from .serializers import CandidateAppliedSerializer, JobSerializer


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
@permission_classes([IsAuthenticated])
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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def apply_to_job(request, pk):
    user = request.user
    job = get_object_or_404(Job, id=pk)

    if user.userprofile.resume == '':
        return Response({
            'error': 'Please upload your resume first.'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    if job.lastDate < timezone.now():
        return Response({
            'error': 'You can not apply to this job. Date is over!'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    already_applied = job.cadidateapplied_set.filter(user=user).exists()

    if already_applied:
        return Response({
            'error': 'You have alredy apply to this job'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    job_applied = CandidateApplied.objects.create(
        job = job,
        user = user,
        resume = user.userprofile.resume
    )

    return Response({
        'applied': True,
        'job_id': job_applied.id
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_current_user_applied_jobs(request):
    
    args = {
        'user_id': request.user.id
    }

    jobs = CandidateApplied.objects.filter(**args)

    serializer = CandidateAppliedSerializer(jobs, many=True)

    return Response(
        serializer.data
    )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def is_applied(request, pk):
    
    user = request.user

    job = get_object_or_404(Job, id=pk)

    applied = job.candidateapllied_set.filter(user=user).exists()

    return Response(applied)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_curent_user_jobs(request):

    args = {
        'user': request.user.id
    }

    jobs = Job.objects.filter(**args)

    serializer = JobSerializer(jobs, many=True)

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_candidates_applied(request, pk):
    
    user = request.user

    job = get_object_or_404(Job, id=pk)

    if job.user != user:
        return Response({
            'error': 'You can not access this job.'
        }, status=status.HTTP_403_FORBIDDEN)
    
    candidates = job.candidateapllied_set.all()

    serializer = CandidateAppliedSerializer(candidates, many=True)

    return Response(serializer.data)