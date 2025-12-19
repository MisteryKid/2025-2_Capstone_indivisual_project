import os
import sys
from ament_index_python.packages import get_package_prefix
import shutil

# 1. 패키지 위치 찾기
package_name = 'tf2_web_republisher_interfaces'
try:
    install_path = get_package_prefix(package_name)
    found_path = None
    for root, dirs, files in os.walk(install_path):
        if package_name in dirs and 'msg' in os.listdir(os.path.join(root, package_name)):
            target_dir = os.path.join(root, package_name, 'msg')
            found_path = os.path.join(target_dir, '__init__.py')
            break
    
    if not found_path:
        print("❌ 파일을 못 찾겠습니다.")
        sys.exit(1)

    print(f"✅ 수정할 파일 위치: {found_path}")

    # 2. 파일 내용 완전 교체 (강력한 덮어쓰기)
    # goal_id 에러를 막기 위해 'FlexibleGoal'이라는 넉넉한 클래스를 정의합니다.
    new_content = """
from tf2_web_republisher_interfaces.action import TFSubscription

# === [CAPSTONE FINAL FIX] ===
# ROS 2 메시지는 엄격해서(slots) 없는 필드(goal_id)를 넣으면 에러가 납니다.
# 그래서 상속을 통해 '무엇이든 받아주는 넉넉한 클래스'를 만듭니다.

class FlexibleGoal(TFSubscription.Goal):
    def __init__(self, *args, **kwargs):
        # 생성자에서 들어오는 goal_id를 에러 없이 받아줍니다.
        self.goal_id = kwargs.pop('goal_id', None)
        self.header = kwargs.pop('header', None)
        super().__init__(*args, **kwargs)

# 웹사이트가 찾는 이름들을 이 'FlexibleGoal'로 연결합니다.
TFSubscription_Goal = FlexibleGoal
TFSubscriptionGoal = FlexibleGoal
TFSubscriptionActionGoal = FlexibleGoal

# 나머지는 원래대로 연결
TFSubscription_Result = TFSubscription.Result
TFSubscription_Feedback = TFSubscription.Feedback
TFSubscriptionResult = TFSubscription.Result
TFSubscriptionFeedback = TFSubscription.Feedback
TFSubscriptionActionResult = TFSubscription.Result
TFSubscriptionActionFeedback = TFSubscription.Feedback
# === [CAPSTONE FIX END] ===
"""

    with open(found_path, 'w') as f:
        f.write(new_content)
    
    print("🎉 파일 수정 완료! (FlexibleGoal 적용됨)")

    # 3. 캐시 삭제 (가장 중요)
    print("🧹 파이썬 기억(Cache) 지우는 중...")
    os.system(f"find {install_path} -name '__pycache__' -type d -exec rm -r {{}} +")
    print("✨ 완료! 이제 모든 창을 껐다 켜세요.")

except Exception as e:
    print(f"❌ 에러 발생: {e}")
