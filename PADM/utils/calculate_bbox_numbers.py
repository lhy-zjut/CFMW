import os

# 设定图像尺寸
IMAGE_WIDTH = 1024
IMAGE_HEIGHT = 768

def process_file(file_path):
    """ 处理单个文件，计算大物体和小物体的比例 """
    large_count = 0
    small_count = 0
    
    with open(file_path, 'r') as f:
        for line in f:
            values = line.strip().split()
            if len(values) != 5:
                continue  # 跳过格式不正确的行
            
            # 解析数据
            label, x1, y1, x2, y2 = values
            
            # 判断是整数坐标还是浮点数（占比坐标）
            try:
                if "." in x1 or "." in y1 or "." in x2 or "." in y2:
                    # 如果包含小数点，则按比例转换为整数坐标
                    x1, y1, x2, y2 = map(float, (x1, y1, x2, y2))
                    x1 = int(x1 * IMAGE_WIDTH)
                    y1 = int(y1 * IMAGE_HEIGHT)
                    x2 = int(x2 * IMAGE_WIDTH)
                    y2 = int(y2 * IMAGE_HEIGHT)
                else:
                    # 直接转换为整数
                    x1, y1, x2, y2 = map(int, (x1, y1, x2, y2))
            except ValueError:
                continue  # 如果转换失败，跳过此行
            
            # 计算 bounding box 的面积
            area = (x2 - x1) * (y2 - y1)

            # 统计大小物体
            if area >= 2500:
                large_count += 1
            else:
                small_count += 1

    return large_count, small_count

def process_folder(folder_path):
    """ 处理文件夹内所有数据文件，计算总体大物体和小物体的比例 """
    total_large = 0
    total_small = 0
    file_count = 0

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        
        if os.path.isfile(file_path):
            large, small = process_file(file_path)
            total_large += large
            total_small += small
            file_count += 1

    total_objects = total_large + total_small
    if total_objects == 0:
        print("⚠️ 没有找到有效的物体数据！")
        return
    
    large_ratio = total_large / total_objects * 100
    small_ratio = total_small / total_objects * 100
    
    print(f"📊 统计结果（共 {file_count} 个文件）：")
    print(f"🔹 大物体（面积≥2500）：{total_large}，占比 {large_ratio:.2f}%")
    print(f"🔸 小物体（面积<2500）：{total_small}，占比 {small_ratio:.2f}%")

# 设置你的数据文件夹路径
folder_path = "/mnt/data/lhy/SWVI/labels"  # 修改为你的文件夹路径
process_folder(folder_path)