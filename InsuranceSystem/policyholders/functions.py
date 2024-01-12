from collections import deque

from policyholders.serializers import PolicyholderSerializer
def get_left_right_tree_data(root_user,direct_users,indirect_users) :
    # 直接優先，再排間接，照時間排序
    direct__selected = list(direct_users[:14])
    remaining_count = 14 - len(direct__selected)
    inderect_users_selected = list(indirect_users[:remaining_count])
    data_selected = direct__selected+list(inderect_users_selected[:remaining_count])
    # 將節點轉換為序列化的資料
    serialized_data = PolicyholderSerializer(data_selected, many=True).data
    for idx,user in enumerate(serialized_data):
        if idx<len(direct__selected):
            user['is_direct'] = True
        else:
            user['is_direct'] = False

    l = [user for idx, user in enumerate(serialized_data) if idx in {0, 2, 3, 6, 7, 8, 9}]
    r = [user for idx, user in enumerate(serialized_data) if idx in {1, 4, 5, 10, 11, 12, 13}]
    return l, r
def get_left_right_tree_data_time_order(root_user,direct_users,indirect_users) :
    # 時間優先
    direct__selected = list(direct_users[:14])
    inderect_users_selected = list(indirect_users[:14])
    
    # 將節點轉換為序列化的資料
    serialized_data_direct = PolicyholderSerializer(direct__selected, many=True).data
    serialized_data_indirect = PolicyholderSerializer(inderect_users_selected, many=True).data
    for _,user in enumerate(serialized_data_direct):
        user['is_direct'] = True
        
    for _,user in enumerate(serialized_data_indirect):
        user['is_direct'] = False
    combined_data = serialized_data_direct+serialized_data_indirect
    sorted_combined_data = sorted(combined_data, key=lambda x: x['registration_date'])[:14]
    l = [user for idx, user in enumerate(sorted_combined_data) if idx in {0, 2, 3, 6, 7, 8, 9}]
    r = [user for idx, user in enumerate(sorted_combined_data) if idx in {1, 4, 5, 10, 11, 12, 13}]
    return l, r
