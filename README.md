# ROS2_with_RaspberryPI

라즈베리파이의 하드웨어적 한계를 극복하기위해 ROS통신을 이용하여 복잡한 연산을 데스크탑에서 실행하도록 한다.
Ubuntu Server 20.04 설치 및 ROS2 설치

## 데스크탑 <-> 라즈베리 파이간 Topic 통신
![image](https://user-images.githubusercontent.com/80799025/189473484-649adf2d-2f66-40dc-bb62-135cd196317a.png)


## camera 실시간 송신
python으로 제작한 camera node를 실행한 결과 PI의 하드웨어적 한계때문에 초당 2프레임으로 Publish 하였다.
c++을 이용하
