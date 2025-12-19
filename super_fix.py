import os
import shutil
from ament_index_python.packages import get_package_prefix

# 목표: 
# 1. tf2_web_republisher_interfaces (원본) 수정
# 2. tf2_web_republisher (복제본) 생성 및 수정

def patch_init_file(file_path):
    """__init__.py 파일에 만능 클래스를 주입하는 함수"""
    
    # 이미 패치된 내용이 있다면 지우고 다시 씁니다.
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    # 기존 내용 중 필요한 import만 남기고 다 지웁니다 (충돌 방지)
    clean_lines = [line for line in lines if "CAPSTONE" not in line and "FlexibleGoal" not in line]
    
    patch_code = """
# === [CAPSTONE SUPER FIX START] ===
from tf2_web_republisher_interfaces.action import TFSubscription

# 1. 만능 Goal 클래스 (goal_id, header 등 없는 필드가 와도 에러 안 나게 처리)
class FlexibleGoal(TFSubscription.Goal):
    def __init__(self, *args, **kwargs):
        self.goal_id = kwargs.pop('goal_id', None)
        self.header = kwargs.pop('header', None)
        super().__init__(*args, **kwargs)

# 2. 이름 연결 (웹사이트가 찾는 모든 이름을 이 만능 클래스로 연결)
TFSubscription_Goal = FlexibleGoal
TFSubscriptionGoal = FlexibleGoal
TFSubscriptionActionGoal = FlexibleGoal

TFSubscription_Result = TFSubscription.Result
TFSubscriptionResult = TFSubscription.Result
TFSubscriptionActionResult = TFSubscription.Result

TFSubscription_Feedback = TFSubscription.Feedback
TFSubscriptionFeedback = TFSubscription.Feedback
TFSubscriptionActionFeedback = TFSubscription.Feedback

# 3. msg 모듈 자체가 없는 경우를 대비해 자기 자신을 참조하게 함
msg = None 
# === [CAPSTONE SUPER FIX END] ===
"""
    with open(file_path, 'w') as f:
        f.writelines(clean_lines)
        f.write(patch_code)
    print(f"✅ 패치 완료: {file_path}")

try:
    # 1. 원본 패키지 위치 찾기 (local workspace 우선)
    # 보통 ~/capstone_ws/install/.../dist-packages/tf2_web_republisher_interfaces
    import tf2_web_republisher_interfaces
    origin_path = os.path.dirname(tf2_web_republisher_interfaces.__file__)
    print(f"📍 원본 위치 발견: {origin_path}")

    # 2. 원본 패키지의 msg/__init__.py 수정
    msg_init_path = os.path.join(origin_path, 'msg', '__init__.py')
    if os.path.exists(msg_init_path):
        patch_init_file(msg_init_path)
    else:
        print("⚠️ 원본 msg 폴더가 없습니다. 생성을 시도합니다.")
        os.makedirs(os.path.join(origin_path, 'msg'), exist_ok=True)
        with open(msg_init_path, 'w') as f: f.write("")
        patch_init_file(msg_init_path)

    # 3. [핵심] 가짜 패키지(tf2_web_republisher) 복제 생성
    # 이름 뒤에 _interfaces가 없는 폴더를 똑같이 만들어줍니다.
    parent_dir = os.path.dirname(origin_path)
    fake_pkg_path = os.path.join(parent_dir, 'tf2_web_republisher')
    
    if os.path.exists(fake_pkg_path):
        print(f"♻️ 기존 가짜 패키지 삭제 후 재생성: {fake_pkg_path}")
        shutil.rmtree(fake_pkg_path)
    
    shutil.copytree(origin_path, fake_pkg_path)
    print(f"📦 가짜 패키지 복제 완료: {fake_pkg_path}")

    # 4. 복제된 패키지도 똑같이 패치 확인
    fake_msg_init = os.path.join(fake_pkg_path, 'msg', '__init__.py')
    patch_init_file(fake_msg_init)

    # 5. 캐시 삭제 (필수)
    print("🧹 파이썬 캐시(기억) 삭제 중...")
    os.system(f"find {parent_dir} -name '__pycache__' -type d -exec rm -r {{}} +")

    print("\n🎉 모든 수리가 끝났습니다!")
    print("👉 이제 Rosbridge와 Python 서버를 껐다가 다시 켜세요.")
    print("👉 반드시 'source install/setup.bash'를 한 터미널에서 실행해야 합니다!")

except Exception as e:
    print(f"\n❌ 에러 발생: {e}")
    print("워크스페이스를 source 하지 않았을 수 있습니다.")
    print("source install/setup.bash 후 다시 시도하세요.")
