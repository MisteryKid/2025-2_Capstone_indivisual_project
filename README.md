## 작동법 

# case 1 : 웹에서 1대의 터틀봇 자율주행 실행하기 
### 1번 tf 변환기 준비  
'''
ros2 run tf2_web_republisher tf2_web_republisher_node --ros-args -p use_sim_time:=true
'''
### 2번 웹이랑 연결 통로 열여주기  
ros2 launch rosbridge_server rosbridge_websocket_launch.xml use_sim_time:=true

### 가자보 
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py

### nav2 실행 
ros2 launch turtlebot3_navigation2 navigation2.launch.py map:=$HOME/map.yaml

*** 주의 ***
반드니 use_sim_time:=true로 설정해주기 

마지막으로 html파일 열어주기 
[ map.html ]

시현영상 
https://youtu.be/6kWB7nokbo0 

# case 2 : 3대의 터틀봇 방향키로 조절하기

### nav2 실행을 안하는 경우이므로 따로 map 서버 띄워주기 
ros2 run nav2_map_server map_server \
  --ros-args -p yaml_filename:=map.yaml
  
### 맵 서버 라이프 사이클 활성화해주기 
ros2 lifecycle set /map_server configure
ros2 lifecycle set /map_server activate

ros2 run tf2_web_republisher tf2_web_republisher_node --ros-args -p use_sim_time:=true
ros2 launch rosbridge_server rosbridge_websocket_launch.xml use_sim_time:=true

### 멀티 터틀봇 스폰해주기 
ros2 launch turtlebot3_navigation2 multi_nav2.launch.py map:=$HOME/map.yaml

마지막으로 html 파일 열어주면 됨 
multi_robot.html

시현영상 
https://youtu.be/mpTyTeeh50s
