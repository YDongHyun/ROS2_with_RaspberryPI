# ROS2_with_RaspberryPI

라즈베리파이의 하드웨어적 한계를 극복하기위해 ROS통신을 이용하여 복잡한 연산을 데스크탑에서 실행하도록 한다.
Ubuntu Server 20.04 설치 및 ROS2 설치

## 데스크탑 <-> 라즈베리 파이간 Topic 통신
![image](https://user-images.githubusercontent.com/80799025/189473484-649adf2d-2f66-40dc-bb62-135cd196317a.png)


## camera 실시간 송신
python과 opencv로 제작한 camera node를 실행한 결과 PI의 하드웨어적 한계때문에 초당 2프레임으로 Publish 한다.
따라서 picamera를 사용하여 노드를 제작한다.

-  우분투 20.04 32bit 설치. (64bit의 경우 mmal오류 발생)
-  아래 명령어를 복사하여 raspi-config를 설치한다.
```
$ wget http://mirrors.ustc.edu.cn/archive.raspberrypi.org/debian/pool/main/r/raspi-config/raspi-config_20201108_all.deb
$ sudo apt install lua5.1  libatopology2 libfftw3-single3 libsamplerate0 alsa-utils
$ sudo dpkg -i raspi-config_20201108_all.deb
```
- 32bit 설치시 ros2 설치 불가 -> ros2 32bit 미지원
