from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.request import Request

@api_view(['GET'])
def get_policyholder(request, code):
    context = {'status': False}
    # 使用 get_object_or_404 確保當前的 code 存在於資料庫中
    '''
    policyholder = get_object_or_404(Policyholder, code=code)
    
    data = {
        'code': policyholder.code,
        'name': policyholder.name,
        'registration_date': policyholder.registration_date.strftime('%Y-%m-%d'),
        'introducer_code': policyholder.introducer_code,
    }
    '''
    return JsonResponse(context, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_policyholder_top_list(request, code):
    context = {'status': True}
    '''
    top_list = get_top_list_for_policyholder(code)
    
    data = {
        'top_list': top_list,
        # 其他欄位...
    }
    '''
    return JsonResponse(context, status=status.HTTP_200_OK)
