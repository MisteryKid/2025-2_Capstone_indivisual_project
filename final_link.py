import os
import shutil
import sys

# 경로 설정 (사용자 환경에 맞게 자동 탐색)
base_path = os.path.expanduser("~/capstone_ws/install/tf2_web_republisher_interfaces/local/lib/python3.10/dist-packages")

real_pkg = os.path.join(base_path, "tf2_web_republisher_interfaces")
fake_pkg = os.path.join(base_path, "tf2_web_republisher")

print("🔧 최종 연결 작업을 시작합니다...")

# 1. 아까 만든 '가짜 폴더'가 있다면 과감히 삭제합니다. (이게 에러의 원흉입니다)
if os.path.exists(fake_pkg) and not os.path.islink(fake_pkg):
    print(f"🗑️ 불량 가짜 패키지 삭제 중: {fake_pkg}")
    shutil.rmtree(fake_pkg)
elif os.path.islink(fake_pkg):
    print("🔗 기존 바로가기 제거 중...")
    os.unlink(fake_pkg)

# 2. '바로가기(Symlink)'를 생성합니다.
# 이제 tf2_web_republisher를 부르면 원본(interfaces)이 응답합니다.
try:
    os.symlink(real_pkg, fake_pkg)
    print(f"✅ 바로가기 생성 완료: {fake_pkg} -> {real_pkg}")
except FileExistsError:
    print("⚠️ 이미 바로가기가 존재합니다.")

# 3. 원본 패키지 안에 'msg' 폴더와 '호환성 코드'를 심습니다.
# 바로가기를 통해 원본이 호출되므로, 원본 안에 호환성 코드가 있어야 합니다.
target_msg_dir = os.path.join(real_pkg, "msg")
os.makedirs(target_msg_dir, exist_ok=True)

target_init_file = os.path.join(target_msg_dir, "__init__.py")

# goal_id 에러와 import 에러를 동시에 잡는 코드
compat_code = """
from tf2_web_republisher_interfaces.action import TFSubscription

# === [호환성 패치] ===
# ROS 2 메시지 형식을 지키면서 goal_id만 유연하게 받아주는 클래스 정의
class FlexibleGoal(TFSubscription.Goal):
    def __init__(self, *args, **kwargs):
        # goal_id나 header가 들어오면 따로 빼내고, 나머지만 부모에게 전달
        self.goal_id = kwargs.pop('goal_id', None)
        self.header = kwargs.pop('header', None)
        super().__init__(*args, **kwargs)

    # Rosbridge가 타입을 검사할 때 "나는 원래 그 녀석 맞아요"라고 속이기 위한 메타데이터
    @classmethod
    def get_fields_and_field_types(cls):
        return TFSubscription.Goal.get_fields_and_field_types()

# 웹사이트가 찾는 이름들을 모두 이 FlexibleGoal로 연결
TFSubscription_Goal = FlexibleGoal
TFSubscriptionGoal = FlexibleGoal
TFSubscriptionActionGoal = FlexibleGoal

TFSubscription_Feedback = TFSubscription.Feedback
TFSubscriptionFeedback = TFSubscription.Feedback
TFSubscriptionActionFeedback = TFSubscription.Feedback

TFSubscription_Result = TFSubscription.Result
TFSubscriptionResult = TFSubscription.Result
TFSubscriptionActionResult = TFSubscription.Result
# =====================
"""

with open(target_init_file, "w") as f:
    f.write(compat_code)

print("✅ 호환성 코드 주입 완료.")

# 4. 캐시 삭제 (필수)
print("🧹 찌꺼기 파일(Cache) 청소 중...")
os.system(f"find {base_path} -name '__pycache__' -type d -exec rm -r {{}} +")

print("\n🎉 모든 준비가 끝났습니다!")
print("👉 터미널을 모두 끄고 다시 시작하세요.")
