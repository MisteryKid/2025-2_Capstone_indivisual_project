import os
import sys

# 우리가 고쳐야 할 두 군데 경로를 찾습니다.
# 1. 원본 (interfaces)
# 2. 아까 만든 복사본 (tf2_web_republisher)

base_path = os.path.expanduser("~/capstone_ws/install/tf2_web_republisher_interfaces/local/lib/python3.10/dist-packages")

# 고쳐야 할 대상 폴더들
targets = [
    os.path.join(base_path, "tf2_web_republisher_interfaces", "msg", "__init__.py"),
    os.path.join(base_path, "tf2_web_republisher", "msg", "__init__.py")
]

# 올바른 파일 내용 (들여쓰기 완벽 교정)
correct_content = """from tf2_web_republisher_interfaces.action import TFSubscription

# 1. 만능 Goal 클래스
class FlexibleGoal(TFSubscription.Goal):
    def __init__(self, *args, **kwargs):
        self.goal_id = kwargs.pop('goal_id', None)
        self.header = kwargs.pop('header', None)
        super().__init__(*args, **kwargs)

# 2. 이름 연결
TFSubscription_Goal = FlexibleGoal
TFSubscriptionGoal = FlexibleGoal
TFSubscriptionActionGoal = FlexibleGoal

TFSubscription_Result = TFSubscription.Result
TFSubscriptionResult = TFSubscription.Result
TFSubscriptionActionResult = TFSubscription.Result

TFSubscription_Feedback = TFSubscription.Feedback
TFSubscriptionFeedback = TFSubscription.Feedback
TFSubscriptionActionFeedback = TFSubscription.Feedback
"""

print("🔧 들여쓰기 수리 시작...")

for file_path in targets:
    # 경로가 실제로 존재하는지 확인 (복사본이 없을 수도 있으니까)
    dir_name = os.path.dirname(file_path)
    if os.path.exists(dir_name):
        try:
            with open(file_path, "w") as f:
                f.write(correct_content)
            print(f"✅ 수정 완료: {file_path}")
        except Exception as e:
            print(f"❌ 실패 ({file_path}): {e}")
    else:
        print(f"⚠️ 경로 없음 (패스): {dir_name}")

# 캐시 삭제
print("🧹 캐시 삭제 중...")
os.system(f"find {base_path} -name '__pycache__' -type d -exec rm -r {{}} +")
print("✨ 수리 끝! 다시 실행해보세요.")
