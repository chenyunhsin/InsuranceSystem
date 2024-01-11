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
