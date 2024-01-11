from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.request import Request
from policyholders.models import Policyholder
from policyholders.functions import get_left_right_tree_data
@api_view(['GET'])
def get_policyholder(request, code) -> JsonResponse:
    context = {'status': False}
    try:
        policyholder = Policyholder.objects.get(code=code)
    except ObjectDoesNotExist:
        context['msg'] = f"policyholder code: {code} not exist"
        return JsonResponse(context, status=status.HTTP_404_NOT_FOUND)
   
    if policyholder.introducer:
        data = {
            'code': policyholder.code,
            'name': policyholder.name,
            'registration_date': policyholder.registration_date.strftime('%Y-%m-%d'),
            'introducer_code': policyholder.introducer.code,
        }
    else:
        # 第一位保人，沒有介紹人
        data = {
            'code': policyholder.code,
            'name': policyholder.name,
            'registration_date': policyholder.registration_date.strftime('%Y-%m-%d'),
            'introducer_code': None,
        }
    # 搜尋直接，最多14
    direct_policyholders = Policyholder.objects.filter(introducer=policyholder).order_by("registration_date")
    direct_policyholders_ids = direct_policyholders.values_list('id', flat=True)
    indirect_policyholders= Policyholder.objects.filter(introducer_id__in=direct_policyholders_ids).order_by("registration_date")
    l,r = get_left_right_tree_data(policyholder,direct_policyholders,indirect_policyholders)
    context['root'] = data
    context['l'] = l
    context['r'] = r
    context['status'] = True
    return JsonResponse(context, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_policyholder_top_list(request, code) -> JsonResponse:
    context = {'status': False}
    try:
        policyholder = Policyholder.objects.get(code=code)
    except ObjectDoesNotExist:
        context['msg'] = f"policyholder code: {code} not exist"
        return JsonResponse(context, status=status.HTTP_404_NOT_FOUND)
    if policyholder.introducer is None:
        context['msg'] = f"policyholder code: {code} is first policyholder"
        return JsonResponse(context, status=status.HTTP_400_BAD_REQUEST)
    target_user = policyholder.introducer
    if target_user.introducer:
        data = {
            'code': target_user.code,
            'name': target_user.name,
            'registration_date': target_user.registration_date.strftime('%Y-%m-%d'),
            'introducer_code': target_user.introducer.code,
        }
    else:
        # 第一位保人，沒有介紹人
        data = {
            'code': target_user.code,
            'name': target_user.name,
            'registration_date': target_user.registration_date.strftime('%Y-%m-%d'),
            'introducer_code': None,
        }
    
   
    direct_policyholders = Policyholder.objects.filter(introducer=target_user).order_by("registration_date")
    direct_policyholders_ids = direct_policyholders.values_list('id', flat=True)
    indirect_policyholders= Policyholder.objects.filter(introducer_id__in=direct_policyholders_ids).order_by("registration_date")
    l,r = get_left_right_tree_data(policyholder,direct_policyholders,indirect_policyholders)
    context['root'] = data
    context['l'] = l
    context['r'] = r
    context['status'] = True
    return JsonResponse(context, status=status.HTTP_200_OK)
