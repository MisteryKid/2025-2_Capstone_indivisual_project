import rclpy
from rclpy.node import Node
from tf2_ros import Buffer, TransformListener
# [핵심 수정] .msg가 아니라 .action에서 가져옵니다.
from tf2_web_republisher_interfaces.action import TFSubscription 
from geometry_msgs.msg import TransformStamped
import time

class SimpleTFServer(Node):
    def __init__(self):
        super().__init__('tf2_web_republisher')
        
        # 1. TF(로봇 위치)를 듣는 귀를 엽니다.
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

        # 2. 웹사이트가 보내는 요청(/goal)을 듣습니다.
        # ROS 2에서는 Action이 .action 모듈 안에 Goal, Feedback 클래스를 가집니다.
        self.subscription = self.create_subscription(
            TFSubscription.Goal,  # [수정] TFSubscriptionActionGoal -> TFSubscription.Goal
            'tf2_web_republisher/goal',
            self.goal_callback,
            10)
        
        # 3. 웹사이트에게 답장(/feedback)을 보낼 입을 엽니다.
        self.publisher_ = self.create_publisher(
            TFSubscription.Feedback, # [수정] TFSubscriptionActionFeedback -> TFSubscription.Feedback
            'tf2_web_republisher/feedback',
            10)

        self.get_logger().info('=== 웹 전용 TF 서버가 시작되었습니다! (표준 모드) ===')
        self.active_goals = {} 

    def goal_callback(self, msg):
        # msg는 이제 TFSubscription.Goal 타입입니다.
        source_frame = msg.source_frame
        target_frame = msg.target_frame
        
        # goal_id가 없을 경우를 대비해 안전하게 가져옵니다.
        # (Rosbridge가 보내는 JSON에 따라 goal_id가 속성으로 안 붙을 수도 있음)
        goal_id = getattr(msg, 'goal_id', None)
        
        key = (source_frame, target_frame)
        self.get_logger().info(f'요청 받음: {target_frame} -> {source_frame}')

        if key not in self.active_goals:
            self.active_goals[key] = self.create_timer(
                0.1, 
                lambda: self.publish_tf(source_frame, target_frame, goal_id)
            )

    def publish_tf(self, source, target, goal_id):
        try:
            trans = self.tf_buffer.lookup_transform(source, target, rclpy.time.Time())
            
            # [수정] 피드백 메시지 생성 방식 변경
            feedback_msg = TFSubscription.Feedback()
            
            # transforms 필드 채우기
            feedback_msg.feedback.transforms = [trans]
            
            # goal_id가 있다면 다시 붙여주기 (속성이 존재할 때만)
            if goal_id and hasattr(feedback_msg, 'status'):
                 feedback_msg.status.goal_id = goal_id
            if hasattr(feedback_msg, 'header'):
                 feedback_msg.header.frame_id = source

            self.publisher_.publish(feedback_msg)
            
        except Exception as e:
            pass

def main(args=None):
    rclpy.init(args=args)
    node = SimpleTFServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()